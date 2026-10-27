from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SILVER = Path(r"C:\GIAD\GIAD-M3_datos_sinteticos_v10_silver")
DEFAULT_OUTPUT = PROJECT_ROOT / "validation" / "results" / "S01" / "csv_checks.json"
DEFAULT_MANIFEST = PROJECT_ROOT / "validation" / "results" / "S01" / "source_manifest.json"

DATA_FILES = {
    "DATA-001": ("official", "andinalog_iot_telemetry_silver.csv"),
    "DATA-002": ("official", "andinalog_productos_silver.csv"),
    "DATA-003": ("official", "andinalog_flota_silver.csv"),
    "DATA-004": ("official", "andinalog_inventory_tracking_silver.csv"),
    "DATA-005": ("official", "andinalog_warehouse_costs_silver.csv"),
    "DATA-006": ("provenance", "GIAD-M3_v10_auditoria_bronze_silver.csv"),
    "DATA-007": ("contrast", "andinalog_wms_orders_silver.csv"),
}

AUX_FILES = {
    "clientes": "andinalog_clientes_silver.csv",
    "drivers": "andinalog_hr_drivers_silver.csv",
}

EXPECTED = {
    "DATA-001": (191710, 15),
    "DATA-002": (120, 7),
    "DATA-003": (100, 6),
    "DATA-004": (7782, 12),
    "DATA-005": (144, 5),
    "DATA-007": (30000, 16),
}

KEY_FIELDS = {
    "DATA-001": [("viaje_id", "minutos_desde_despacho"), ("viaje_id", "timestamp")],
    "DATA-002": [("producto_id",)],
    "DATA-003": [("camion_id",)],
    "DATA-004": [("lote_id",), ("movimiento_id",)],
    "DATA-005": [("centro_distribucion", "periodo_mes")],
    "DATA-007": [("order_id",)],
}

OFFICIAL_SILVER = {
    "andinalog_iot_telemetry_silver.csv",
    "andinalog_productos_silver.csv",
    "andinalog_flota_silver.csv",
    "andinalog_inventory_tracking_silver.csv",
    "andinalog_warehouse_costs_silver.csv",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        rows = list(reader)
    return header, rows


def file_metadata(path: Path) -> dict:
    stat = path.stat()
    return {
        "path": str(path),
        "exists": path.exists(),
        "size_bytes": stat.st_size,
        "last_write_time": datetime.fromtimestamp(stat.st_mtime).astimezone().isoformat(),
        "sha256": sha256(path),
    }


def empty_counts(header: list[str], rows: list[dict[str, str]]) -> dict[str, int]:
    result = {}
    for field in header:
        result[field] = sum(1 for row in rows if not (row.get(field) or "").strip())
    return result


def key_checks(rows: list[dict[str, str]], fields: tuple[str, ...]) -> dict:
    keys = [tuple((row.get(field) or "") for field in fields) for row in rows]
    duplicate_count = len(keys) - len(set(keys))
    empty_keys = sum(1 for key in keys if any(not value.strip() for value in key))
    return {
        "fields": list(fields),
        "unique": duplicate_count == 0 and empty_keys == 0,
        "rows": len(keys),
        "distinct": len(set(keys)),
        "duplicates": duplicate_count,
        "empty_keys": empty_keys,
    }


def source_summary(source_id: str, role: str, path: Path) -> tuple[dict, list[str], list[dict[str, str]]]:
    header, rows = read_csv(path)
    metadata = file_metadata(path)
    summary = {
        "id": source_id,
        "role": role,
        **metadata,
        "rows": len(rows),
        "columns": len(header),
        "header": header,
        "empty_cells": empty_counts(header, rows),
        "key_checks": [key_checks(rows, fields) for fields in KEY_FIELDS.get(source_id, [])],
    }
    return summary, header, rows


def compare_count(source_id: str, summary: dict) -> list[dict]:
    expected = EXPECTED.get(source_id)
    if not expected:
        return []
    expected_rows, expected_columns = expected
    problems = []
    if summary["rows"] != expected_rows:
        problems.append({
            "source": source_id,
            "field": "rows",
            "expected": expected_rows,
            "actual": summary["rows"],
        })
    if summary["columns"] != expected_columns:
        problems.append({
            "source": source_id,
            "field": "columns",
            "expected": expected_columns,
            "actual": summary["columns"],
        })
    return problems


def key_problems(source_id: str, summary: dict) -> list[dict]:
    problems = []
    for check in summary["key_checks"]:
        if check["duplicates"] or check["empty_keys"]:
            problems.append({
                "source": source_id,
                "field": "key:" + "+".join(check["fields"]),
                "expected": "unique and non-empty",
                "actual": {
                    "duplicates": check["duplicates"],
                    "empty_keys": check["empty_keys"],
                },
            })
    return problems


def wms_checks(
    wms_rows: list[dict[str, str]],
    telemetry_rows: list[dict[str, str]],
    fleet_rows: list[dict[str, str]],
    inventory_rows: list[dict[str, str]],
    driver_rows: list[dict[str, str]],
    client_rows: list[dict[str, str]],
) -> dict:
    wms_by_order = {row["order_id"]: row for row in wms_rows}
    telemetry_by_order = {row["order_id"]: row for row in telemetry_rows}
    fleet_by_camion = {row["camion_id"]: row for row in fleet_rows}
    inventory_by_lote = {row["lote_id"]: row for row in inventory_rows}
    client_by_id = {row["cliente_id"]: row for row in client_rows}
    driver_by_month = {(row["chofer_id"], row["periodo_mes"][:7]): row for row in driver_rows}

    wms_orders = set(wms_by_order)
    telemetry_orders = set(telemetry_by_order)
    covered_orders = wms_orders & telemetry_orders
    without_telemetry = wms_orders - telemetry_orders

    order_camiones = defaultdict(set)
    for row in telemetry_rows:
        order_camiones[row["order_id"]].add(row["camion_id"])
    camion_conflicts = {
        order: sorted(camiones)
        for order, camiones in order_camiones.items()
        if len(camiones) > 1
    }

    center_base_matches = 0
    center_base_missing = 0
    center_base_mismatch = []
    for order_id in covered_orders:
        wms = wms_by_order[order_id]
        camiones = order_camiones.get(order_id, set())
        if len(camiones) != 1:
            center_base_missing += 1
            continue
        fleet = fleet_by_camion.get(next(iter(camiones)))
        if not fleet:
            center_base_missing += 1
            continue
        if wms["centro_distribucion"] == fleet["centro_distribucion_base"]:
            center_base_matches += 1
        else:
            center_base_mismatch.append(order_id)

    lote_matches = 0
    lote_missing = 0
    lote_mismatch = []
    for row in wms_rows:
        inventory = inventory_by_lote.get(row["lote_id"])
        if not inventory:
            lote_missing += 1
            continue
        if inventory["centro_distribucion"] == row["centro_distribucion"]:
            lote_matches += 1
        else:
            lote_mismatch.append(row["order_id"])

    driver_matches = 0
    driver_missing = 0
    driver_mismatch = []
    for row in wms_rows:
        key = (row["chofer_id"], row["fecha_despacho"][:7])
        driver = driver_by_month.get(key)
        if not driver:
            driver_missing += 1
            continue
        if driver["centro_distribucion"] == row["centro_distribucion"]:
            driver_matches += 1
        else:
            driver_mismatch.append(row["order_id"])

    client_matches = 0
    client_missing = 0
    client_mismatch = []
    for row in wms_rows:
        client = client_by_id.get(row["cliente_id"])
        if not client:
            client_missing += 1
            continue
        if client["zona_despacho"] == row["centro_distribucion"]:
            client_matches += 1
        else:
            client_mismatch.append(row["order_id"])

    return {
        "wms_rows": len(wms_rows),
        "wms_orders": len(wms_orders),
        "telemetry_orders": len(telemetry_orders),
        "covered_orders": len(covered_orders),
        "coverage_of_telemetry_orders": f"{len(covered_orders)} de {len(telemetry_orders)}",
        "wms_orders_without_telemetry": len(without_telemetry),
        "center_base": {
            "matches": center_base_matches,
            "expected": len(covered_orders),
            "missing": center_base_missing,
            "mismatches": center_base_mismatch[:20],
        },
        "lote_center": {
            "matches": lote_matches,
            "expected": len(wms_rows),
            "missing": lote_missing,
            "mismatches": lote_mismatch[:20],
        },
        "driver_month_center": {
            "matches": driver_matches,
            "expected": len(wms_rows),
            "missing": driver_missing,
            "mismatches": driver_mismatch[:20],
        },
        "client_zone_center": {
            "matches": client_matches,
            "expected": len(wms_rows),
            "missing": client_missing,
            "mismatches": client_mismatch[:20],
        },
        "order_camion_conflicts": camion_conflicts,
    }


def telemetry_observations(
    telemetry_rows: list[dict[str, str]],
    product_rows: list[dict[str, str]],
) -> dict:
    product_by_id = {row["producto_id"]: row for row in product_rows}
    orders = defaultdict(list)
    trips = defaultdict(list)
    for row in telemetry_rows:
        orders[row["order_id"]].append(row)
        trips[row["viaje_id"]].append(row)

    multi_orders = {
        order_id: rows
        for order_id, rows in orders.items()
        if len({row["particion_modelo"] for row in rows}) > 1
    }
    multi_trips = {
        viaje_id: rows
        for viaje_id, rows in trips.items()
        if len({row["particion_modelo"] for row in rows}) > 1
    }

    boundary_rows = []
    missing_products = 0
    flagged_by_trip = Counter()
    boundary_by_trip = Counter()
    for row in telemetry_rows:
        product = product_by_id.get(row["producto_id"])
        if not product:
            missing_products += 1
            continue
        flag = int(row["desviacion_termica_flag"])
        if flag:
            flagged_by_trip[row["viaje_id"]] += 1
        try:
            temperature = float(row["temperatura_cabina_c"])
            required = float(product["temperatura_conservacion_requerida_c"])
            tolerance = float(product["tolerancia_temperatura_c"])
        except (TypeError, ValueError):
            continue
        difference = abs(temperature - required)
        if flag and difference <= tolerance:
            boundary_rows.append({
                "viaje_id": row["viaje_id"],
                "order_id": row["order_id"],
                "producto_id": row["producto_id"],
                "temperatura_cabina_c": temperature,
                "required": required,
                "tolerance": tolerance,
                "difference": round(difference, 6),
            })
            boundary_by_trip[row["viaje_id"]] += 1

    boundary_trips = set(boundary_by_trip)
    dependent_trips = sorted(
        viaje_id
        for viaje_id in boundary_trips
        if boundary_by_trip[viaje_id] == flagged_by_trip[viaje_id]
    )
    boundary_distribution = Counter(
        (row["required"], row["tolerance"], row["temperatura_cabina_c"])
        for row in boundary_rows
    )

    multi_order_rows = [row for rows in multi_orders.values() for row in rows]
    multi_trip_rows = [row for rows in multi_trips.values() for row in rows]
    telemetry_products = {row["producto_id"] for row in telemetry_rows}
    catalog_refrigerated = {
        row["producto_id"]
        for row in product_rows
        if row["categoria_logistica"] in {"Refrigerado", "Congelado"}
    }

    return {
        "orders_with_two_partitions": len(multi_orders),
        "order_rows_with_two_partitions": len(multi_order_rows),
        "order_positives_with_two_partitions": sum(
            int(row["desviacion_proximos_60min_flag"]) for row in multi_order_rows
        ),
        "trips_with_two_partitions": len(multi_trips),
        "trip_rows_with_two_partitions": len(multi_trip_rows),
        "trip_positives_with_two_partitions": sum(
            int(row["desviacion_proximos_60min_flag"]) for row in multi_trip_rows
        ),
        "boundary_reads": len(boundary_rows),
        "boundary_percent": round(len(boundary_rows) / len(telemetry_rows) * 100, 4),
        "boundary_trips": len(boundary_trips),
        "boundary_dependent_trips": dependent_trips,
        "boundary_distribution": [
            {
                "required": key[0],
                "tolerance": key[1],
                "temperature": key[2],
                "count": count,
            }
            for key, count in sorted(boundary_distribution.items())
        ],
        "telemetry_products": len(telemetry_products),
        "catalog_refrigerated_frozen": len(catalog_refrigerated),
        "products_in_telemetry_not_refrigerated_frozen": sorted(
            telemetry_products - catalog_refrigerated
        )[:20],
        "missing_product_references": missing_products,
    }


def inventory_observations(inventory_rows: list[dict[str, str]]) -> dict:
    missing_exit = sum(1 for row in inventory_rows if not (row.get("fecha_salida") or "").strip())
    balance_mismatch = 0
    for row in inventory_rows:
        try:
            if int(row["cantidad_ingreso"]) != int(row["cantidad_salida"]) + int(row["cantidad_merma"]):
                balance_mismatch += 1
        except (TypeError, ValueError):
            balance_mismatch += 1
    return {
        "rows": len(inventory_rows),
        "rows_without_exit": missing_exit,
        "balance_mismatches": balance_mismatch,
    }


def provenance_checks(
    audit_rows: list[dict[str, str]],
    source_summaries: dict[str, dict],
    source_ids: dict[str, str],
) -> dict:
    audit_by_silver = {row["archivo_silver"]: row for row in audit_rows}
    official_records = []
    row_count_checks = []
    for source_id in ["DATA-001", "DATA-002", "DATA-003", "DATA-004", "DATA-005"]:
        filename = source_ids[source_id]
        record = audit_by_silver.get(filename)
        if record:
            official_records.append(record)
            actual_rows = source_summaries[source_id]["rows"]
            actual_columns = source_summaries[source_id]["columns"]
            row_count_checks.append({
                "source": source_id,
                "file": filename,
                "data006_filas_silver": int(record["filas_silver"]),
                "actual_rows": actual_rows,
                "data006_columnas_silver": int(record["columnas_silver"]),
                "actual_columns": actual_columns,
                "rows_match": int(record["filas_silver"]) == actual_rows,
                "columns_match": int(record["columnas_silver"]) == actual_columns,
            })
        else:
            official_records.append({"source": source_id, "file": filename, "missing": True})
    wms_record = audit_by_silver.get("andinalog_wms_orders_silver.csv")
    return {
        "data006_rows": len(audit_rows),
        "official_records_found": len([record for record in official_records if not record.get("missing")]),
        "official_records": official_records,
        "wms_record": wms_record,
        "wms_record_counted_as_official": False,
        "row_count_checks": row_count_checks,
    }


def manifest_check(manifest_path: Path) -> dict:
    if not manifest_path.exists():
        return {"status": "not-run", "reason": "manifest not found"}
    manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    changed = []
    missing = []
    for source in manifest.get("sources", []):
        path = Path(source["path"])
        if not path.exists():
            missing.append(source["id"])
            continue
        if sha256(path) != source["sha256"]:
            changed.append(source["id"])
    return {
        "status": "pass" if not changed and not missing else "fail",
        "checked": len(manifest.get("sources", [])),
        "changed": changed,
        "missing": missing,
    }


def discrepancy_list(
    source_summaries: dict[str, dict],
    wms: dict,
    telemetry: dict,
    inventory: dict,
    provenance: dict,
) -> list[dict]:
    discrepancies = []
    for source_id, summary in source_summaries.items():
        discrepancies.extend(compare_count(source_id, summary))
        discrepancies.extend(key_problems(source_id, summary))
    for name, expected in [("center_base", "matches"), ("lote_center", "matches"), ("driver_month_center", "matches"), ("client_zone_center", "matches")]:
        block = wms[name]
        if block["matches"] != block["expected"] or block["missing"] or block["mismatches"]:
            discrepancies.append({
                "source": "WMS",
                "field": name,
                "expected": block["expected"],
                "actual": block["matches"],
                "missing": block["missing"],
                "mismatches": block["mismatches"],
            })
    if wms["covered_orders"] != wms["telemetry_orders"]:
        discrepancies.append({
            "source": "WMS",
            "field": "coverage_of_telemetry_orders",
            "expected": wms["telemetry_orders"],
            "actual": wms["covered_orders"],
        })
    for field, expected in [
        ("telemetry_orders", 8000),
        ("covered_orders", 8000),
        ("wms_orders_without_telemetry", 22000),
    ]:
        actual = wms[field]
        if actual != expected:
            discrepancies.append({
                "source": "WMS",
                "field": field,
                "expected": expected,
                "actual": actual,
            })
    if wms["order_camion_conflicts"]:
        discrepancies.append({
            "source": "WMS",
            "field": "order_camion_conflicts",
            "expected": 0,
            "actual": len(wms["order_camion_conflicts"]),
        })
    expected_observations = {
        "orders_with_two_partitions": 14,
        "order_rows_with_two_partitions": 339,
        "order_positives_with_two_partitions": 43,
        "boundary_reads": 26,
        "boundary_trips": 26,
        "boundary_dependent_trips": 0,
    }
    for field, expected in expected_observations.items():
        actual = telemetry[field]
        if field == "boundary_dependent_trips":
            actual = len(actual)
        if actual != expected:
            discrepancies.append({
                "source": "DATA-001",
                "field": field,
                "expected": expected,
                "actual": actual,
            })
    for field, expected in [("balance_mismatches", 0), ("rows_without_exit", 0)]:
        actual = inventory[field]
        if actual != expected:
            discrepancies.append({
                "source": "DATA-004",
                "field": field,
                "expected": expected,
                "actual": actual,
            })
    for field, expected in [("data006_rows", 33), ("data006_columns", 10), ("official_records_found", 5)]:
        actual = (
            source_summaries["DATA-006"]["columns"]
            if field == "data006_columns"
            else provenance[field]
        )
        if actual != expected:
            discrepancies.append({
                "source": "DATA-006",
                "field": field,
                "expected": expected,
                "actual": actual,
            })
    for check in provenance["row_count_checks"]:
        if not check.get("rows_match", False):
            discrepancies.append({
                "source": "DATA-006",
                "field": check["source"] + ".rows",
                "expected": check["actual_rows"],
                "actual": check["data006_filas_silver"],
            })
        if not check.get("columns_match", False):
            discrepancies.append({
                "source": "DATA-006",
                "field": check["source"] + ".columns",
                "expected": check["actual_columns"],
                "actual": check["data006_columnas_silver"],
            })
    return discrepancies


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--silver", type=Path, default=DEFAULT_SILVER)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    args = parser.parse_args()

    source_summaries = {}
    source_rows = {}
    source_headers = {}
    source_ids = {}
    for source_id, (role, filename) in DATA_FILES.items():
        path = args.silver / filename
        source_ids[source_id] = filename
        summary, header, rows = source_summary(source_id, role, path)
        source_summaries[source_id] = summary
        source_rows[source_id] = rows
        source_headers[source_id] = header

    aux = {}
    for name, filename in AUX_FILES.items():
        path = args.silver / filename
        header, rows = read_csv(path)
        aux[name] = {"path": str(path), "header": header, "rows": rows}

    wms = wms_checks(
        source_rows["DATA-007"],
        source_rows["DATA-001"],
        source_rows["DATA-003"],
        source_rows["DATA-004"],
        aux["drivers"]["rows"],
        aux["clientes"]["rows"],
    )
    telemetry = telemetry_observations(source_rows["DATA-001"], source_rows["DATA-002"])
    inventory = inventory_observations(source_rows["DATA-004"])
    provenance = provenance_checks(source_rows["DATA-006"], source_summaries, source_ids)
    p01 = manifest_check(args.manifest)
    discrepancies = discrepancy_list(source_summaries, wms, telemetry, inventory, provenance)

    p02 = {
        "status": "pass" if not discrepancies else "fail",
        "discrepancies": discrepancies,
    }
    p06 = {
        "status": "pass" if wms["covered_orders"] == wms["telemetry_orders"] and not wms["order_camion_conflicts"] else "review",
        "wms_loaded": False,
        "method": "Cruces en memoria con csv; ninguna fuente WMS se cargó en Power BI.",
    }

    result = {
        "generated_at": datetime.now().astimezone().isoformat(),
        "hito": "S01",
        "task": "T02",
        "spec_version": "0.4",
        "plan_version": "0.2",
        "method": {
            "language": "Python",
            "library": "csv (stdlib)",
            "encoding": "utf-8-sig",
            "decimal_point": ".",
            "hash": "SHA-256",
            "source_mutation": "none",
        },
        "sources": source_summaries,
        "auxiliary_sources": {
            name: {
                "path": value["path"],
                "rows": len(value["rows"]),
                "columns": len(value["header"]),
                "header": value["header"],
            }
            for name, value in aux.items()
        },
        "inventory": inventory,
        "telemetry": telemetry,
        "provenance": provenance,
        "wms": wms,
        "checks": {"P01": p01, "P02": p02, "P06": p06},
        "discrepancies": discrepancies,
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "output": str(args.output),
        "p01": p01,
        "p02_status": p02["status"],
        "discrepancies": len(discrepancies),
        "wms_coverage": wms["coverage_of_telemetry_orders"],
        "wms_without_telemetry": wms["wms_orders_without_telemetry"],
        "official_records": provenance["official_records_found"],
        "boundary_reads": telemetry["boundary_reads"],
        "multi_order_rows": telemetry["order_rows_with_two_partitions"],
    }, ensure_ascii=False, indent=2))
    return 0 if not discrepancies else 2


if __name__ == "__main__":
    raise SystemExit(main())

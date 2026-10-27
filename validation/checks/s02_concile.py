#!/usr/bin/env python3
"""T10: conciliación final de S02 sin modificar los artefactos auditados."""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import unicodedata
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import openpyxl
import pypdfium2 as pdfium
from pptx import Presentation

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "validation" / "results" / "S02" / "conciliation.json"

SPEC = ROOT / "specs" / "002-s02-architecture" / "spec.md"
CONTENT_JSON = ROOT / "work" / "S02" / "content.json"
CONTENT_MD = ROOT / "work" / "S02" / "content.md"
XLSX = ROOT / "deliverables" / "tracking" / "M4_Equipo06_Proyecto_Integrador_v2.xlsx"
PPTX = ROOT / "deliverables" / "S02" / "M4_Equipo06_S02_Arquitectura.pptx"
PDF = ROOT / "deliverables" / "S02" / "M4_Equipo06_S02_Arquitectura.pdf"
PBIP = ROOT / "powerbi" / "AndinaLog_03B.pbip"
INITIAL_MANIFEST = ROOT / "validation" / "results" / "S02" / "initial_manifest.json"
SOURCE_MANIFEST = ROOT / "validation" / "results" / "S01" / "source_manifest.json"
MODEL_DIR = ROOT / "powerbi" / "AndinaLog_03B.SemanticModel" / "definition"
REFERENCES = ROOT / "references"

EXPECTED = {
    "spec": {
        "size": 28474,
        "sha256": "A91958C34BADCF6E5AAF3D0F063AC94C3FE458436A9C30AF6AE1362FD626598A",
    },
    "content_json": {
        "size": 13094,
        "sha256": "A7C3A75D43841B72E542F7A05F7B6FC882F7DA8316EF8689B8A92205BF1C7882",
    },
    "content_md": {
        "size": 9375,
        "sha256": "00109A5D0F03A7C3E6892D3C2FCBDA978845A24F05FFD4875A122EE360C427BC",
    },
    "xlsx": {
        "size": 39510,
        "sha256": "31C7E81FE2A21C2BD9DDE76C01B25198DEADA0283F28A46AA4015AFA0734B24D",
    },
    "pptx": {
        "size": 43872,
        "sha256": "26324855E2864A636C0390D725FA34787269DE5A9F2893031602B97B16AB325D",
    },
    "pdf": {
        "size": 237204,
        "sha256": "07516A56C643334AD59F8AEBD6FB67757E954196D736181BCE771ABFCB201A42",
    },
}

FIELD_ORDER = [
    "archivo",
    "granularidad",
    "identificador_unico",
    "frecuencia",
    "propietario",
    "riesgo",
    "control_propuesto",
]

EXPECTED_FILES = [
    "andinalog_iot_telemetry_silver.csv",
    "andinalog_productos_silver.csv",
    "andinalog_flota_silver.csv",
    "andinalog_inventory_tracking_silver.csv",
    "andinalog_warehouse_costs_silver.csv",
]

KPI_FORMULA_FRAGMENTS = [
    ["viajes con al menos una lectura marcada", "viajes observados", "100"],
    ["lecturas marcadas", "lecturas observadas", "100"],
    ["cantidad_merma", "cantidad_ingreso", "100"],
    ["lotes con salida posterior al día de vencimiento", "lotes salidos", "100"],
    ["promedio de dias_en_almacen"],
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def file_meta(path: Path) -> dict:
    data = path.read_bytes()
    return {"path": rel(path), "size_bytes": len(data), "sha256": sha256_bytes(data)}


def norm(value) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    text = text.replace("\ufeff", "").replace("\u00a0", " ").replace("\u200b", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"')
    text = text.replace("’", "'").replace("–", "-").replace("—", "-")
    text = text.replace("`", "").replace("**", "").replace("→", "->")
    text = re.sub(r"[ \t\f\v]+", " ", text)
    text = re.sub(r"\s*\n\s*", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text.casefold()


def has(term: str, text: str) -> bool:
    return norm(term) in norm(text)


def all_has(terms: list[str], text: str) -> bool:
    return all(has(term, text) for term in terms)


def table_after(text: str, marker: str, header_token: str) -> tuple[list[str], list[list[str]]]:
    at = text.find(marker)
    if at < 0:
        raise ValueError(f"No se encontró el marcador: {marker}")
    lines = text[at:].splitlines()
    start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("|") and header_token.casefold() in stripped.casefold():
            start = i
            break
    if start is None:
        raise ValueError(f"No se encontró la tabla con encabezado {header_token!r} tras {marker!r}")
    block = []
    for line in lines[start:]:
        stripped = line.strip()
        if stripped.startswith("|"):
            block.append(stripped)
        elif block:
            break
    if not block:
        raise ValueError(f"Tabla vacía para {header_token!r}")
    parsed = [[cell.strip() for cell in row.strip("|").split("|")] for row in block]
    header = parsed[0]
    rows = []
    for row in parsed[1:]:
        if row and all(set(cell) <= set("-: ") for cell in row):
            continue
        rows.append(row)
    return header, rows


def refs_manifest() -> tuple[list[dict], str]:
    items = []
    for path in sorted(REFERENCES.rglob("*")):
        if path.is_file():
            data = path.read_bytes()
            items.append({"path": rel(path), "size_bytes": len(data), "sha256": sha256_bytes(data)})
    payload = "\n".join(f"{item['path']}|{item['sha256']}" for item in items).encode("utf-8")
    return items, sha256_bytes(payload)


def find_row(rows: list[dict], item: str) -> dict | None:
    wanted = norm(item)
    for row in rows:
        if norm(row["item"]) == wanted:
            return row
    return None


def main() -> int:
    started = utc_now()
    before = {
        "spec": file_meta(SPEC),
        "content_json": file_meta(CONTENT_JSON),
        "content_md": file_meta(CONTENT_MD),
        "xlsx": file_meta(XLSX),
        "pptx": file_meta(PPTX),
        "pdf": file_meta(PDF),
        "pbip": file_meta(PBIP),
    }
    refs_before, refs_digest_before = refs_manifest()

    spec_text = SPEC.read_text(encoding="utf-8")
    spec_md = SPEC.read_text(encoding="utf-8")
    content = json.loads(CONTENT_JSON.read_text(encoding="utf-8"))
    content_md = CONTENT_MD.read_text(encoding="utf-8")
    initial = json.loads(INITIAL_MANIFEST.read_text(encoding="utf-8"))
    source_manifest = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))

    wb = openpyxl.load_workbook(XLSX, data_only=False)
    ws_map = wb["S02 Mapa Silver"]
    ws_kpi = wb["Fichas KPI"]
    xlsx_map = [
        {"fields": dict(zip(FIELD_ORDER, [ws_map.cell(r, c).value for c in range(1, 8)]))}
        for r in range(7, 12)
    ]
    xlsx_kpi = [
        {
            "name": ws_kpi.cell(r, 1).value,
            "level": ws_kpi.cell(r, 3).value,
            "formula": ws_kpi.cell(r, 4).value,
            "unit": ws_kpi.cell(r, 5).value,
        }
        for r in range(7, 12)
    ]
    xlsx_formula_count = sum(
        1
        for ws in wb.worksheets
        for row in ws.iter_rows()
        for cell in row
        if isinstance(cell.value, str) and cell.value.startswith("=")
    )
    xlsx_dv_count = sum(len(ws.data_validations.dataValidation) for ws in wb.worksheets)
    xlsx_cf_ranges = sum(len(ws.conditional_formatting) for ws in wb.worksheets)
    xlsx_cf_rules = sum(
        len(cf.rules) for ws in wb.worksheets for cf in ws.conditional_formatting
    )
    xlsx_merged = sum(len(ws.merged_cells.ranges) for ws in wb.worksheets)

    prs = Presentation(PPTX)
    pptx_slides = list(prs.slides)
    pptx_texts = []
    for slide in pptx_slides:
        parts = []
        for shape in slide.shapes:
            if hasattr(shape, "text") and shape.text:
                parts.append(shape.text)
        pptx_texts.append("\n".join(parts))
    pptx_tables = {}
    for index, slide in enumerate(pptx_slides, start=1):
        tables = []
        for shape in slide.shapes:
            if getattr(shape, "has_table", False):
                tables.append(
                    [[cell.text for cell in row.cells] for row in shape.table.rows]
                )
        pptx_tables[index] = tables
    pptx_map_tables = [pptx_tables[3][0], pptx_tables[4][0]]
    pptx_map_rows = []
    for table in pptx_map_tables:
        for row in table[1:]:
            if len(row) == 7:
                pptx_map_rows.append({"fields": dict(zip(FIELD_ORDER, row))})
    pptx_map_flat = [cell for table in pptx_map_tables for row in table for cell in row]
    with zipfile.ZipFile(PPTX) as archive:
        pptx_slide1_xml_sha = sha256_bytes(archive.read("ppt/slides/slide1.xml"))

    pdf = pdfium.PdfDocument(str(PDF))
    pdf_texts = [pdf[i].get_textpage().get_text_range() for i in range(len(pdf))]
    pdf_sizes = [list(pdf[i].get_size()) for i in range(len(pdf))]
    pdf.close()
    pdf_page1 = pdf_texts[0]
    pdf_map_pages = {2: pdf_texts[1], 3: pdf_texts[2]}
    pdf_map_text = "\n".join(pdf_map_pages.values())

    model_tables = sorted((MODEL_DIR / "tables").glob("*.tmdl"))
    model_text = "\n".join(
        path.read_text(encoding="utf-8") for path in model_tables + [MODEL_DIR / "model.tmdl"]
    )
    model_measure_count = len(re.findall(r"(?m)^\s*measure\s+", model_text))
    model_relationship_count = len(re.findall(r"(?m)^\s*relationship\s+", model_text))

    spec_map_header, spec_map_rows_raw = table_after(spec_md, "## Anexo A", "Archivo / tabla")
    spec_map = []
    for row in spec_map_rows_raw:
        if len(row) != 7:
            continue
        spec_map.append({"fields": dict(zip(FIELD_ORDER, row))})
    spec_kpi_rows = table_after(spec_md, "## Anexo B", "Fórmula en palabras")[1]
    spec_kpis = [
        {
            "id": int(row[0]),
            "name": row[1],
            "level": row[2],
            "formula": row[3],
            "unit": row[4],
        }
        for row in spec_kpi_rows
        if len(row) >= 5 and row[0].isdigit()
    ]
    spec_pending_rows = table_after(spec_md, "### 8.3", "Estado al cierre")[1]
    spec_pending = [
        {"item": row[0], "status": row[1], "responsible": row[2], "milestone": row[3]}
        for row in spec_pending_rows
        if len(row) == 4
    ]

    md_map_rows = table_after(content_md, "## Mapa Silver", "Archivo / tabla")[1]
    md_map = []
    for row in md_map_rows:
        if len(row) == 8:
            md_map.append({"id": row[0], "fields": dict(zip(FIELD_ORDER, row[1:]))})
    md_kpi_rows = table_after(content_md, "## KPI tácticos", "Fórmula en palabras")[1]
    md_kpis = [
        {
            "id": int(row[0]),
            "name": row[1],
            "level": row[2],
            "formula": row[3],
            "unit": row[4],
        }
        for row in md_kpi_rows
        if len(row) >= 5 and row[0].isdigit()
    ]
    md_pending_rows = table_after(content_md, "## Pendientes", "Estado al cierre")[1]
    md_pending = [
        {"item": row[0], "status": row[1], "responsible": row[2], "milestone": row[3]}
        for row in md_pending_rows
        if len(row) == 4
    ]

    content_map = content["map"]["rows"]
    content_kpis = content["kpis"]
    content_pending = content["pending"]
    content_blocks = {block["id"]: block for block in content["slide_blocks"]}

    spec_by_file = {norm(row["fields"]["archivo"]): row for row in spec_map}
    content_by_file = {norm(row["fields"]["archivo"]): row for row in content_map}
    md_by_file = {norm(row["fields"]["archivo"]): row for row in md_map}
    xlsx_by_file = {norm(row["fields"]["archivo"]): row for row in xlsx_map}
    pptx_by_file = {norm(row["fields"]["archivo"]): row for row in pptx_map_rows}
    file_to_id = {row["fields"]["archivo"]: row["id"] for row in content_map}

    post = {
        "spec": file_meta(SPEC),
        "content_json": file_meta(CONTENT_JSON),
        "content_md": file_meta(CONTENT_MD),
        "xlsx": file_meta(XLSX),
        "pptx": file_meta(PPTX),
        "pdf": file_meta(PDF),
        "pbip": file_meta(PBIP),
    }
    refs_after, refs_digest_after = refs_manifest()

    checks = []

    def add(
        cid: str,
        category: str,
        description: str,
        sources: list[dict],
        expected,
        observed,
        normalize: str,
        evidence,
        ok: bool,
    ) -> None:
        checks.append(
            {
                "id": cid,
                "category": category,
                "description": description,
                "sources": sources,
                "expected": expected,
                "observed": observed,
                "normalization": normalize,
                "evidence": evidence,
                "status": "PASS" if ok else "FAIL",
            }
        )

    # H: hashes and recorded integrity
    same_spec = before["spec"]["sha256"] == post["spec"]["sha256"] == EXPECTED["spec"]["sha256"]
    content_spec_sha = str(content["spec"]["sha256"]).upper()
    add(
        "T10-H01",
        "hashes",
        "La spec v0.4 conserva tamaño y SHA-256 antes y después; coincide con content.json.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "archivo completo"},
         {"path": "work/S02/content.json", "location": "spec.sha256"}],
        {"size_bytes": EXPECTED["spec"]["size"], "sha256": EXPECTED["spec"]["sha256"],
         "content_spec_sha256": EXPECTED["spec"]["sha256"], "before_equals_after": True},
        {"size_bytes": before["spec"]["size_bytes"], "sha256": before["spec"]["sha256"],
         "after_sha256": post["spec"]["sha256"], "content_spec_sha256": content_spec_sha,
         "before_equals_after": before["spec"]["sha256"] == post["spec"]["sha256"]},
        "SHA-256 y tamaño exactos",
        "validation/results/S02/conciliation.json; hashes.before/after.spec",
        same_spec and content_spec_sha == EXPECTED["spec"]["sha256"],
    )

    for cid, key, path_label in [
        ("T10-H02", "content_json", "work/S02/content.json"),
        ("T10-H03", "content_md", "work/S02/content.md"),
        ("T10-H04", "xlsx", "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx"),
        ("T10-H05", "pptx", "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx"),
        ("T10-H06", "pdf", "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf"),
    ]:
        expected = EXPECTED[key]
        same = (
            before[key]["sha256"] == post[key]["sha256"] == expected["sha256"]
            and before[key]["size_bytes"] == post[key]["size_bytes"] == expected["size"]
        )
        add(
            cid,
            "hashes",
            f"{path_label} conserva tamaño y SHA-256 antes y después.",
            [{"path": path_label, "location": "archivo completo"}],
            {"size_bytes": expected["size"], "sha256": expected["sha256"],
             "before_equals_after": True},
            {"size_bytes": before[key]["size_bytes"], "sha256": before[key]["sha256"],
             "after_size_bytes": post[key]["size_bytes"], "after_sha256": post[key]["sha256"],
             "before_equals_after": before[key]["sha256"] == post[key]["sha256"]},
            "SHA-256 y tamaño exactos",
            "validation/results/S02/conciliation.json; hashes.before/after." + key,
            same,
        )

    source_expected = {item["id"]: item for item in source_manifest["sources"]}
    source_observations = []
    for source_id, item in source_expected.items():
        path = Path(item["path"])
        if path.exists():
            actual = file_meta(path)
            ok = (
                actual["sha256"] == str(item["sha256"]).upper()
                and actual["size_bytes"] == item["size_bytes"]
            )
            source_observations.append(
                {"id": source_id, "path": item["path"], "ok": ok,
                 "expected_sha256": str(item["sha256"]).upper(),
                 "actual_sha256": actual["sha256"], "actual_size_bytes": actual["size_bytes"]}
            )
        else:
            source_observations.append(
                {"id": source_id, "path": item["path"], "ok": False, "error": "missing"}
            )
    initial_objects = {item["id"]: item for item in initial["objects"]}
    for source_id in ["SRC-201", "SRC-203", "PBIP"]:
        item = initial_objects[source_id]
        path = ROOT / item["path"]
        actual = file_meta(path)
        ok = (
            actual["sha256"] == str(item["sha256"]).upper()
            and actual["size_bytes"] == item["size_bytes"]
        )
        source_observations.append(
            {"id": source_id, "path": item["path"], "ok": ok,
             "expected_sha256": str(item["sha256"]).upper(),
             "actual_sha256": actual["sha256"], "actual_size_bytes": actual["size_bytes"]}
        )
    add(
        "T10-H07",
        "hashes",
        "Silver, referencias clave y PBIP mantienen sus huellas registradas; no se alteraron las fuentes.",
        [{"path": "validation/results/S01/source_manifest.json", "location": "sources[]"},
         {"path": "validation/results/S02/initial_manifest.json", "location": "objects[]"},
         {"path": "powerbi/AndinaLog_03B.pbip", "location": "archivo completo"}],
        {"all_recorded_hashes_equal": True, "source_count": len(source_observations)},
        {"all_recorded_hashes_equal": all(item["ok"] for item in source_observations),
         "source_count": len(source_observations),
         "mismatches": [item for item in source_observations if not item["ok"]]},
        "SHA-256 y tamaño exactos contra manifiestos",
        "validation/results/S02/conciliation.json; source_integrity",
        all(item["ok"] for item in source_observations),
    )
    add(
        "T10-H08",
        "hashes",
        "El árbol de references conserva el mismo manifiesto agregado antes y después.",
        [{"path": "references/", "location": "todos los archivos"}],
        {"file_count": len(refs_before), "aggregate_sha256": refs_digest_before,
         "before_equals_after": True},
        {"file_count_before": len(refs_before), "file_count_after": len(refs_after),
         "aggregate_sha256_before": refs_digest_before,
         "aggregate_sha256_after": refs_digest_after,
         "before_equals_after": refs_digest_before == refs_digest_after
         and len(refs_before) == len(refs_after)},
        "SHA-256 por archivo y agregado de rutas ordenadas",
        "validation/results/S02/conciliation.json; references_manifest",
        refs_digest_before == refs_digest_after and len(refs_before) == len(refs_after),
    )

    # D: decision and architecture
    decision = content["decision"]["sentence"]
    spec_quote = content["decision"]["spec_quote"]
    decision_ok = (
        all_has(
            ["jefatura de operaciones", "revisión semanal", "priorizar controles térmicos",
             "lotes o centros", "vencimiento y merma"],
            spec_md,
        )
        and has(spec_quote, spec_md)
        and all_has([decision], content_md)
        and all_has([decision], pptx_texts[1])
        and all_has([decision], pdf_page1)
        and decision.count(".") == 1
    )
    add(
        "T10-D01",
        "decision_architecture",
        "La decisión apoya a la Jefatura de Operaciones, es semanal y aparece una sola vez con el mismo significado en spec, contrato, PPTX y PDF.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§1.2"},
         {"path": "work/S02/content.json", "location": "decision.sentence"},
         {"path": "work/S02/content.md", "location": "## Decisión"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"}],
        {"sentence": decision, "one_sentence": True, "same_in_all": True},
        {"spec_quote_present": has(spec_quote, spec_md),
         "content_json_sentence": decision,
         "content_md_present": has(decision, content_md),
         "pptx_slide2_present": has(decision, pptx_texts[1]),
         "pdf_page1_present": has(decision, pdf_page1),
         "period_count": decision.count(".")},
        "Texto normalizado; se admite 'decide cada semana' frente a 'decide, con revisión semanal'",
        "evidence/S02/conciliation.md; T10-D01",
        decision_ok,
    )

    box_labels = ["1 · origen", "2 · tabla silver", "3 · power query", "4 · modelo semántico", "5 · indicador"]
    box_ok = (
        all_has(box_labels, pptx_texts[1])
        and all_has(box_labels, pdf_page1)
        and all_has(
            ["Origen", "Tabla Silver", "Power Query", "Modelo semántico", "Indicador"],
            "\n".join(block["label"] for block in content["slide_blocks"]),
        )
    )
    add(
        "T10-D02",
        "decision_architecture",
        "Las cinco cajas del flujo origen → Silver → Power Query → modelo → indicador están presentes.",
        [{"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"},
         {"path": "work/S02/content.json", "location": "slide_blocks[].label"}],
        {"labels": box_labels, "present_in": ["pptx_slide2", "pdf_page1", "content"]},
        {"pptx_slide2": all_has(box_labels, pptx_texts[1]),
         "pdf_page1": all_has(box_labels, pdf_page1),
         "content_labels": [block["label"] for block in content["slide_blocks"]]},
        "Texto normalizado; se toleran mayúsculas y saltos de línea",
        "evidence/S02/conciliation.md; T10-D02",
        box_ok,
    )

    origin_ok = (
        all_has(["no documentado por archivo"], spec_md)
        and all_has(["por acordar"], spec_md)
        and all_has(["no se atribuye erp, wms, tms ni telemetría"], spec_md)
        and all_has(["no documentado"], content_md)
        and all_has(["por acordar"], content_md)
        and all_has(["no se atribuye erp, wms, tms ni telemetría"], content_md)
        and all_has(["no documentado por archivo", "por acordar", "no se atribuye erp, wms, tms ni telemetría"], pptx_texts[1])
        and all_has(["no documentado por archivo", "por acordar", "no se atribuye erp, wms, tms ni telemetría"], pdf_page1)
        and norm(content["map"]["origin"]) == norm("No documentado / por acordar")
    )
    add(
        "T10-D03",
        "decision_architecture",
        "El origen se registra como no documentado/por acordar y no se atribuye ERP, WMS, TMS ni telemetría.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§3.3 y Anexo A"},
         {"path": "work/S02/content.json", "location": "map.origin"},
         {"path": "work/S02/content.md", "location": "## Mapa Silver"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"}],
        {"origin": "No documentado / por acordar",
         "attribution": "No se atribuye ERP, WMS, TMS ni telemetría"},
        {"content_map_origin": content["map"]["origin"],
         "spec_has_origin": all_has(["no documentado por archivo", "por acordar"], spec_md),
         "spec_has_no_attribution": has("no se atribuye erp, wms, tms ni telemetría", spec_md),
         "pptx_has_origin": all_has(["no documentado por archivo", "por acordar"], pptx_texts[1]),
         "pdf_has_origin": all_has(["no documentado por archivo", "por acordar"], pdf_page1)},
        "Texto normalizado",
        "evidence/S02/conciliation.md; T10-D03",
        origin_ok,
    )

    model_ok = (
        all_has(["cinco tablas import"], spec_md)
        and all_has(["0 relaciones", "0 medidas", "propuestas", "s06"], spec_md)
        and all_has(["5 tablas import", "0 relaciones", "0 medidas", "propuestas para s06"], pptx_texts[1])
        and all_has(["5 tablas import", "0 relaciones", "0 medidas", "propuestas para s06"], pdf_page1)
        and all_has(["5 tablas import", "0 relaciones", "0 medidas", "propuestas para s06"], content_md)
        and len(model_tables) == 5
        and model_measure_count == 0
        and model_relationship_count == 0
    )
    add(
        "T10-D04",
        "decision_architecture",
        "El estado actual del modelo (5 tablas, 0 relaciones, 0 medidas) se diferencia de la propuesta para S06.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§3.3"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"},
         {"path": "powerbi/AndinaLog_03B.SemanticModel/definition", "location": "TMDL"}],
        {"tables": 5, "relationships": 0, "measures": 0,
         "proposal_label": "dimensiones y relaciones propuestas para S06"},
        {"model_tables": len(model_tables), "model_table_names": [p.stem for p in model_tables],
         "model_measures": model_measure_count, "model_relationships": model_relationship_count,
         "pptx_model_present": all_has(["5 tablas import", "0 relaciones", "0 medidas", "propuestas para s06"], pptx_texts[1]),
         "pdf_model_present": all_has(["5 tablas import", "0 relaciones", "0 medidas", "propuestas para s06"], pdf_page1)},
        "Texto normalizado y conteo TMDL",
        "evidence/S02/conciliation.md; T10-D04; powerbi/.../definition",
        model_ok,
    )

    dcam = content["dcam"]
    dcam_ok = (
        all_has(["ausencia documentada", "no se declara resuelta", "dud-s02-07"], spec_md)
        and norm(dcam["state"]) == norm("Ausencia documentada")
        and dcam["resolved"] is False
        and all_has(["ausencia documentada", "no resuelta"], pptx_texts[1])
        and all_has(["ausencia documentada", "no resuelta"], pdf_page1)
        and all_has(["ausencia documentada", "no resuelta"], content_md)
    )
    add(
        "T10-D05",
        "decision_architecture",
        "La brecha DCAM se documenta como ausencia no resuelta, con DUD-S02-07 abierta.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§7, §8.3 y §9"},
         {"path": "work/S02/content.json", "location": "dcam"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"}],
        {"id": "DUD-S02-07", "state": "Ausencia documentada", "resolved": False,
         "message": "no resuelta"},
        {"spec_has_state": all_has(["ausencia documentada", "no se declara resuelta"], spec_md),
         "content_state": dcam["state"], "content_resolved": dcam["resolved"],
         "pptx_has_state": all_has(["ausencia documentada", "no resuelta"], pptx_texts[1]),
         "pdf_has_state": all_has(["ausencia documentada", "no resuelta"], pdf_page1)},
        "Texto normalizado y booleano content.dcam.resolved",
        "evidence/S02/conciliation.md; T10-D05",
        dcam_ok,
    )

    risk_terms = ["interpretar", "centro", "filtros", "conclusiones"]
    fact_terms = ["8.000"]
    control_terms = ["usos", "límites conocidos", "definición y validación"]
    complement_terms = ["propuestas"]
    pending_terms = ["grupo 06", "validador por acordar", "no resuelto"]
    d06_texts = [spec_md, content_md, pptx_texts[1], pdf_page1]
    risk_ok = all(all_has(risk_terms, text) for text in d06_texts)
    fact_ok = all(
        all_has(fact_terms, text)
        and any(has(term, text) for term in ["sin discrepancias", "no hallaron discrepancias", "no encontraron discrepancias"])
        and any(has(term, text) for term in ["no prueba", "no acredita", "no demuestra"])
        and has("significado", text)
        for text in d06_texts
    )
    control_ok = all(
        all_has(control_terms, text)
        and any(has(term, text) for term in ["solicitar", "solicitud"])
        for text in d06_texts
    )
    complement_ok = all(
        all_has(complement_terms, text)
        and any(has(term, text) for term in ["no usar centro_distribucion_base", "no usar el centro base"])
        and has("ruta", text)
        for text in d06_texts
    )
    pending_ok = all(all_has(pending_terms, text) for text in d06_texts)
    d06_ok = risk_ok and fact_ok and control_ok and complement_ok and pending_ok
    add(
        "T10-D06",
        "decision_architecture",
        "Riesgo, hecho observado, límite, control principal, control complementario y pendiente son coherentes entre soportes.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§7 y §8"},
         {"path": "work/S02/content.md", "location": "## Brecha DCAM"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"}],
        {"risk": risk_terms, "observed_fact": fact_terms + ["sin discrepancias|no hallaron discrepancias|no encontraron discrepancias"],
         "control": control_terms + ["solicitar|solicitud"],
         "complement": complement_terms + ["no usar centro_distribucion_base|no usar el centro base"],
         "pending": pending_terms},
        {"risk_ok": risk_ok, "fact_ok": fact_ok, "control_ok": control_ok,
         "complement_ok": complement_ok, "pending_ok": pending_ok},
        "Fragmentos normalizados; se admiten 'no prueba', 'no acredita' y 'no demuestra'",
        "evidence/S02/conciliation.md; T10-D06",
        d06_ok,
    )

    # M: Silver map
    m01_ok = (
        len(spec_map) == 5
        and len(content_map) == 5
        and len(md_map) == 5
        and len(xlsx_map) == 5
        and len(pptx_map_rows) == 5
        and all(len(row["fields"]) == 7 for row in spec_map + content_map + md_map + xlsx_map + pptx_map_rows)
        and [norm(row["fields"]["archivo"]) for row in spec_map] == [norm(f) for f in EXPECTED_FILES]
        and [norm(row["fields"]["archivo"]) for row in content_map] == [norm(f) for f in EXPECTED_FILES]
        and [norm(row["fields"]["archivo"]) for row in md_map] == [norm(f) for f in EXPECTED_FILES]
        and [norm(row["fields"]["archivo"]) for row in xlsx_map] == [norm(f) for f in EXPECTED_FILES]
        and [norm(row["fields"]["archivo"]) for row in pptx_map_rows] == [norm(f) for f in EXPECTED_FILES]
        and [row["id"] for row in content_map] == [f"DATA-00{i}" for i in range(1, 6)]
    )
    add(
        "T10-M01",
        "silver_map",
        "El mapa contiene exactamente DATA-001 a DATA-005, cinco filas y siete campos por fila.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo A"},
         {"path": "work/S02/content.json", "location": "map.rows"},
         {"path": "work/S02/content.md", "location": "## Mapa Silver"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "S02 Mapa Silver!A7:G11"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositivas 3-4"}],
        {"ids": ["DATA-001", "DATA-002", "DATA-003", "DATA-004", "DATA-005"],
         "rows": 5, "fields_per_row": 7, "files": EXPECTED_FILES},
        {"spec_rows": len(spec_map), "content_rows": len(content_map), "md_rows": len(md_map),
         "xlsx_rows": len(xlsx_map), "pptx_rows": len(pptx_map_rows),
         "content_ids": [row["id"] for row in content_map],
         "spec_files": [row["fields"]["archivo"] for row in spec_map]},
        "Conteo exacto y orden de archivos",
        "validation/results/S02/conciliation.json; T10-M01",
        m01_ok,
    )

    map_mismatches = []
    for file in EXPECTED_FILES:
        key = norm(file)
        if key not in spec_by_file or key not in content_by_file or key not in md_by_file or key not in xlsx_by_file or key not in pptx_by_file:
            map_mismatches.append({"file": file, "issue": "missing in one or more sources"})
            continue
        for field in FIELD_ORDER:
            values = {
                "spec": spec_by_file[key]["fields"][field],
                "content": content_by_file[key]["fields"][field],
                "content_md": md_by_file[key]["fields"][field],
                "xlsx": xlsx_by_file[key]["fields"][field],
                "pptx": pptx_by_file[key]["fields"][field],
            }
            normalized = {name: norm(value) for name, value in values.items()}
            if len(set(normalized.values())) != 1:
                map_mismatches.append({"file": file, "field": field, "values": values})
    add(
        "T10-M02",
        "silver_map",
        "Los siete campos de cada una de las cinco fuentes coinciden en spec, contrato, Excel y PPTX.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo A"},
         {"path": "work/S02/content.json", "location": "map.rows[].fields"},
         {"path": "work/S02/content.md", "location": "## Mapa Silver"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "S02 Mapa Silver!A7:G11"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositivas 3-4"}],
        {"rows": 5, "fields": 7, "comparisons": 35, "mismatches": []},
        {"comparisons": 35, "mismatches": map_mismatches},
        "Texto normalizado; sin coincidencia difusa",
        "validation/results/S02/conciliation.json; T10-M02",
        not map_mismatches,
    )

    pdf_map_mismatches = []
    for index, row in enumerate(content_map):
        page_number = 2 if index < 3 else 3
        page_text = pdf_map_pages[page_number]
        if not has(row["fields"]["archivo"], page_text):
            pdf_map_mismatches.append({"file": row["fields"]["archivo"], "page": page_number, "field": "archivo"})
        for field in FIELD_ORDER:
            if not has(row["fields"][field], page_text):
                pdf_map_mismatches.append({"file": row["fields"]["archivo"], "page": page_number, "field": field})
    pdf_map_ok = (
        len(pdf_texts) == 3
        and all_has(["mapa silver — 1/2"], pdf_map_pages[2])
        and all_has(["mapa silver — 2/2"], pdf_map_pages[3])
        and not pdf_map_mismatches
    )
    add(
        "T10-M03",
        "silver_map",
        "El PDF distribuye el mapa completo en 3+2 filas y conserva los siete campos de cada fuente.",
        [{"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "páginas 2-3"},
         {"path": "work/S02/content.json", "location": "map.rows"}],
        {"distribution": {"page_2": EXPECTED_FILES[:3], "page_3": EXPECTED_FILES[3:]},
         "fields": 7, "mismatches": []},
        {"page_count": len(pdf_texts),
         "page_2_heading": has("Mapa Silver — 1/2", pdf_map_pages[2]),
         "page_3_heading": has("Mapa Silver — 2/2", pdf_map_pages[3]),
         "mismatches": pdf_map_mismatches},
        "Texto PDF normalizado; saltos de línea colapsados",
        "validation/results/S02/conciliation.json; T10-M03",
        pdf_map_ok,
    )

    occurrence = {}
    for file in EXPECTED_FILES:
        xlsx_count = sum(1 for row in xlsx_map if norm(row["fields"]["archivo"]) == norm(file))
        pptx_count = sum(1 for row in pptx_map_rows if norm(row["fields"]["archivo"]) == norm(file))
        pdf_count = sum(1 for text in pdf_map_pages.values() if has(file, text))
        occurrence[file] = {"xlsx": xlsx_count, "pptx": pptx_count, "pdf": pdf_count}
    occurrence_ok = all(
        counts["xlsx"] == 1 and counts["pptx"] == 1 and counts["pdf"] == 1
        for counts in occurrence.values()
    )
    add(
        "T10-M04",
        "silver_map",
        "Cada fuente oficial aparece una sola vez en Excel, PPTX y PDF.",
        [{"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "S02 Mapa Silver!A7:A11"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "tablas de diapositivas 3-4"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "páginas 2-3"}],
        {file: {"xlsx": 1, "pptx": 1, "pdf": 1} for file in EXPECTED_FILES},
        occurrence,
        "Coincidencia exacta de nombre de archivo",
        "validation/results/S02/conciliation.json; T10-M04",
        occurrence_ok,
    )

    inventory_freq = content_by_file[norm("andinalog_inventory_tracking_silver.csv")]["fields"]["frecuencia"]
    inventory_ok = (
        all_has([inventory_freq], spec_md)
        and all_has([inventory_freq], content_md)
        and has(inventory_freq, xlsx_by_file[norm("andinalog_inventory_tracking_silver.csv")]["fields"]["frecuencia"])
        and has(inventory_freq, pptx_by_file[norm("andinalog_inventory_tracking_silver.csv")]["fields"]["frecuencia"])
        and has(inventory_freq, pdf_map_pages[3])
        and has("sin periodicidad fija", spec_md)
        and has("sin periodicidad fija", pdf_map_pages[3])
    )
    add(
        "T10-M05",
        "silver_map",
        "La frecuencia de inventario conserva el grano y la frase exactos en todos los soportes.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§3.2, RF-S02-03 y Anexo A"},
         {"path": "work/S02/content.json", "location": "map.rows[DATA-004].fields.frecuencia"},
         {"path": "work/S02/content.md", "location": "## Mapa Silver"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "S02 Mapa Silver!A10:G10"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 4"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 3"}],
        {"frequency": inventory_freq, "grain": "Un lote con ingreso, salida y merma en esta entrega"},
        {"frequency": inventory_freq,
         "spec_has_phrase": has(inventory_freq, spec_md),
         "content_md_has_phrase": has(inventory_freq, content_md),
         "xlsx_has_phrase": has(inventory_freq, xlsx_by_file[norm("andinalog_inventory_tracking_silver.csv")]["fields"]["frecuencia"]),
         "pptx_has_phrase": has(inventory_freq, pptx_by_file[norm("andinalog_inventory_tracking_silver.csv")]["fields"]["frecuencia"]),
         "pdf_has_phrase": has(inventory_freq, pdf_map_pages[3])},
        "Texto normalizado",
        "validation/results/S02/conciliation.json; T10-M05",
        inventory_ok,
    )

    spec_map_segment = spec_md.split("## Anexo A", 1)[1].split("**Nota fuera del mapa:**", 1)[0]
    wms_ok = (
        not has("wms", spec_map_segment)
        and not has("data-007", spec_map_segment)
        and not any(has("wms", row["fields"]["archivo"]) or has("data-007", row["fields"]["archivo"]) for row in content_map)
        and not has("wms", " ".join(str(cell) for row in xlsx_map for cell in row["fields"].values()))
        and not has("wms", " ".join(pptx_map_flat))
        and not has("wms", pdf_map_text)
        and content["wms_note"]["in_map"] is False
        and content["wms_note"]["loaded"] is False
        and content["wms_note"]["counts_as_official"] is False
        and has("data-007", spec_md)
        and has("no se cuenta como sexta fuente oficial", spec_md)
        and has("data-007", content_md)
        and has("no se cuenta como sexta fuente oficial", content_md)
    )
    add(
        "T10-M06",
        "silver_map",
        "WMS queda fuera del mapa y del modelo, solo como contraste no cargado; no cuenta como sexta fuente.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo A, nota fuera del mapa"},
         {"path": "work/S02/content.json", "location": "wms_note"},
         {"path": "work/S02/content.md", "location": "## Nota WMS separada"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "S02 Mapa Silver!A7:G11"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "tablas de diapositivas 3-4"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "páginas 2-3"}],
        {"in_map": False, "loaded": False, "counts_as_official": False,
         "map_artifacts_without_wms": True},
        {"spec_map_has_wms": has("wms", spec_map_segment),
         "spec_map_has_data_007": has("data-007", spec_map_segment),
         "wms_note": content["wms_note"],
         "xlsx_map_has_wms": has("wms", " ".join(str(cell) for row in xlsx_map for cell in row["fields"].values())),
         "pptx_map_has_wms": has("wms", " ".join(pptx_map_flat)),
         "pdf_map_has_wms": has("wms", pdf_map_text)},
        "Texto normalizado y banderas booleanas",
        "validation/results/S02/conciliation.json; T10-M06",
        wms_ok,
    )

    # K: KPI
    spec_names = [row["name"] for row in spec_kpis]
    content_names = [row["name"] for row in content_kpis]
    md_names = [row["name"] for row in md_kpis]
    xlsx_names = [row["name"] for row in xlsx_kpi]
    kpi_names_ok = (
        len(spec_names) == 5
        and len(content_names) == 5
        and len(md_names) == 5
        and len(xlsx_names) == 5
        and [norm(x) for x in spec_names] == [norm(x) for x in content_names]
        == [norm(x) for x in md_names] == [norm(x) for x in xlsx_names]
    )
    add(
        "T10-K01",
        "kpi",
        "Hay exactamente cinco KPI con el mismo nombre y orden en spec, contrato, Markdown y Excel.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo B"},
         {"path": "work/S02/content.json", "location": "kpis"},
         {"path": "work/S02/content.md", "location": "## KPI tácticos"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!A7:A11"}],
        {"count": 5, "names": content_names, "same_order": True},
        {"spec": spec_names, "content": content_names, "content_md": md_names, "xlsx": xlsx_names},
        "Texto normalizado; sin sinónimos ni coincidencia difusa",
        "validation/results/S02/conciliation.json; T10-K01",
        kpi_names_ok,
    )

    levels_ok = (
        all(norm(row["level"]) == norm("Táctico") for row in spec_kpis)
        and all(norm(row["level"]) == norm("Táctico") for row in content_kpis)
        and all(norm(row["level"]) == norm("Táctico") for row in md_kpis)
        and all(norm(row["level"]) == norm("Táctico") for row in xlsx_kpi)
    )
    add(
        "T10-K02",
        "kpi",
        "Los cinco KPI son tácticos y la decisión semanal justifica el nivel.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo B"},
         {"path": "work/S02/content.json", "location": "kpis[].level"},
         {"path": "work/S02/content.md", "location": "## KPI tácticos"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!C7:C11"}],
        {"level": "Táctico", "count": 5},
        {"spec_levels": [row["level"] for row in spec_kpis],
         "content_levels": [row["level"] for row in content_kpis],
         "md_levels": [row["level"] for row in md_kpis],
         "xlsx_levels": [row["level"] for row in xlsx_kpi]},
        "Texto normalizado",
        "validation/results/S02/conciliation.json; T10-K02",
        levels_ok,
    )

    formula_mismatches = []
    for index, fragments in enumerate(KPI_FORMULA_FRAGMENTS):
        sources = {
            "spec": spec_kpis[index]["formula"] if index < len(spec_kpis) else "",
            "content": content_kpis[index]["formula"] if index < len(content_kpis) else "",
            "content_md": md_kpis[index]["formula"] if index < len(md_kpis) else "",
            "xlsx": xlsx_kpi[index]["formula"] if index < len(xlsx_kpi) else "",
        }
        for name, formula in sources.items():
            missing = [fragment for fragment in fragments if not has(fragment, str(formula))]
            if missing:
                formula_mismatches.append({"kpi_index": index + 1, "source": name, "missing": missing, "formula": formula})
    units_ok = (
        len(spec_kpis) == 5 and len(content_kpis) == 5 and len(md_kpis) == 5 and len(xlsx_kpi) == 5
        and all(norm(spec_kpis[i]["unit"]) == norm(content_kpis[i]["unit"]) == norm(md_kpis[i]["unit"]) == norm(xlsx_kpi[i]["unit"]) for i in range(5))
        and [norm(row["unit"]) for row in content_kpis] == [norm(x) for x in ["Porcentaje", "Porcentaje", "Porcentaje", "Porcentaje", "Días"]]
    )
    add(
        "T10-K03",
        "kpi",
        "Cada KPI conserva fórmula en palabras y unidad, con el denominador indicado.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo B"},
         {"path": "work/S02/content.json", "location": "kpis[].formula/unit"},
         {"path": "work/S02/content.md", "location": "## KPI tácticos"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!D7:E11"}],
        {"formula_fragments": KPI_FORMULA_FRAGMENTS,
         "units": ["Porcentaje", "Porcentaje", "Porcentaje", "Porcentaje", "Días"],
         "mismatches": []},
        {"formula_mismatches": formula_mismatches,
         "units": [row["unit"] for row in content_kpis],
         "units_consistent": units_ok},
        "Fragmentos normalizados; 'dividido entre' y 'multiplicado por' equivalen a '/' y '×'",
        "validation/results/S02/conciliation.json; T10-K03",
        not formula_mismatches and units_ok,
    )

    dias_ok = (
        has("dias_en_almacen", spec_md)
        and has("dias_en_almacen", content_md)
        and has("dias_en_almacen", xlsx_kpi[4]["formula"] if len(xlsx_kpi) == 5 else "")
        and not has("días_en_almacen", spec_md)
        and not has("días_en_almacen", content_md)
        and not has("días_en_almacen", " ".join(str(row["formula"]) for row in xlsx_kpi))
    )
    add(
        "T10-K04",
        "kpi",
        "El identificador dias_en_almacen se conserva sin tilde; la tilde solo aparece en el nombre visible.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo B"},
         {"path": "work/S02/content.md", "location": "## KPI tácticos"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!D11"}],
        {"identifier": "dias_en_almacen", "accented_identifier_absent": True},
        {"spec_has_identifier": has("dias_en_almacen", spec_md),
         "content_md_has_identifier": has("dias_en_almacen", content_md),
         "xlsx_has_identifier": has("dias_en_almacen", xlsx_kpi[4]["formula"] if len(xlsx_kpi) == 5 else ""),
         "spec_has_accented_identifier": has("días_en_almacen", spec_md),
         "xlsx_has_accented_identifier": has("días_en_almacen", " ".join(str(row["formula"]) for row in xlsx_kpi))},
        "Texto normalizado; se distingue el nombre visible del identificador",
        "validation/results/S02/conciliation.json; T10-K04",
        dias_ok,
    )

    support = content["support_measure"]
    support_ok = (
        norm(support["name"]) == norm("Número de lotes vencidos")
        and support["is_kpi"] is False
        and has("medida de apoyo: número de lotes vencidos", spec_md)
        and has("no es kpi principal", spec_md)
        and has("número de lotes vencidos", content_md)
        and not any(has(support["name"], name) for name in spec_names)
        and not any(has(support["name"], name) for name in content_names)
        and not any(has(support["name"], name) for name in xlsx_names)
    )
    add(
        "T10-K05",
        "kpi",
        "El número de lotes vencidos se mantiene como medida de apoyo separada, no como KPI principal.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo B, medida de apoyo"},
         {"path": "work/S02/content.json", "location": "support_measure"},
         {"path": "work/S02/content.md", "location": "## Medida de apoyo"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!A7:A11"}],
        {"name": "Número de lotes vencidos", "is_kpi": False, "not_in_kpi_catalog": True},
        {"support_measure": support, "present_in_spec": has("medida de apoyo: número de lotes vencidos", spec_md),
         "present_in_kpi_names": [name for name in spec_names + content_names + xlsx_names if has(support["name"], name)]},
        "Texto normalizado y booleano support_measure.is_kpi",
        "validation/results/S02/conciliation.json; T10-K05",
        support_ok,
    )

    excluded = content["excluded_kpis"][0]
    merma_ok = (
        norm(excluded["name"]) == norm("Merma por valor")
        and has("merma por valor", spec_md)
        and has("no es kpi", spec_md)
        and has("merma por valor", content_md)
        and has("no es kpi", content_md)
        and not any(has("merma por valor", name) for name in spec_names + content_names + xlsx_names)
        and any(has("merma por valor", row["item"]) for row in content_pending)
    )
    add(
        "T10-K06",
        "kpi",
        "Merma por valor queda excluida del catálogo y registrada como pendiente, sin borrar su motivo.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "Anexo B y §8.3"},
         {"path": "work/S02/content.json", "location": "excluded_kpis"},
         {"path": "work/S02/content.md", "location": "## KPI excluidos"},
         {"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!A7:A11"}],
        {"name": "Merma por valor", "in_kpi_catalog": False, "pending_recorded": True},
        {"excluded": excluded, "present_in_kpi_names": [name for name in spec_names + content_names + xlsx_names if has("merma por valor", name)],
         "present_in_pending": any(has("merma por valor", row["item"]) for row in content_pending)},
        "Texto normalizado",
        "validation/results/S02/conciliation.json; T10-K06",
        merma_ok,
    )

    later_cells = []
    for row in range(7, 12):
        for col in [10] + list(range(15, 19)) + list(range(20, 27)):
            value = ws_kpi.cell(row, col).value
            if value not in (None, ""):
                later_cells.append({"cell": ws_kpi.cell(row, col).coordinate, "value": value})
    k07_ok = (
        not later_cells
        and model_measure_count == 0
        and content["claims"]["dax_executed"] is False
        and has("sin metas, umbrales ni dax en s02", spec_md)
        and has("metas y umbrales: s08", spec_md)
        and has("dax: s07", spec_md)
    )
    add(
        "T10-K07",
        "kpi",
        "No hay metas, umbrales, DAX ni responsables completados en S02; esas capas quedan para hitos posteriores.",
        [{"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "Fichas KPI!J7:Z11"},
         {"path": "specs/002-s02-architecture/spec.md", "location": "§3.3 y Anexo B"},
         {"path": "work/S02/content.json", "location": "claims.dax_executed"},
         {"path": "powerbi/AndinaLog_03B.SemanticModel/definition", "location": "TMDL"}],
        {"later_cells_empty": True, "model_measures": 0, "dax_executed": False},
        {"non_empty_later_cells": later_cells, "model_measures": model_measure_count,
         "dax_executed": content["claims"]["dax_executed"]},
        "Celdas vacías exactas y booleano de alcance",
        "validation/results/S02/conciliation.json; T10-K07",
        k07_ok,
    )

    # P: pending items and claims
    p01_ok = len(spec_pending) == 13 and all(
        all(norm(row[field]) for field in ["item", "status", "responsible", "milestone"])
        for row in spec_pending
    )
    add(
        "T10-P01",
        "pending",
        "La tabla de pendientes conserva trece filas con estado, responsable e hito.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"}],
        {"rows": 13, "fields": ["item", "status", "responsible", "milestone"]},
        {"rows": len(spec_pending), "items": [row["item"] for row in spec_pending]},
        "Conteo y campos no vacíos",
        "validation/results/S02/conciliation.json; T10-P01",
        p01_ok,
    )

    pending_mismatches = []
    if len(spec_pending) != len(content_pending):
        pending_mismatches.append({"issue": "row_count", "spec": len(spec_pending), "content": len(content_pending)})
    for spec_row, content_row in zip(spec_pending, content_pending):
        for field in ["item", "status", "responsible", "milestone"]:
            if norm(spec_row[field]) != norm(content_row[field]):
                pending_mismatches.append({"item": spec_row["item"], "field": field,
                                           "spec": spec_row[field], "content": content_row[field]})
    p02_ok = len(spec_pending) == len(content_pending) == len(md_pending) and not pending_mismatches
    add(
        "T10-P02",
        "pending",
        "La spec y el contrato conservan el mismo estado, responsable e hito para cada pendiente.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"},
         {"path": "work/S02/content.json", "location": "pending"},
         {"path": "work/S02/content.md", "location": "## Pendientes"}],
        {"rows": 13, "same_fields": True, "mismatches": []},
        {"spec_rows": len(spec_pending), "content_rows": len(content_pending),
         "md_rows": len(md_pending), "mismatches": pending_mismatches},
        "Texto normalizado, comparación campo a campo",
        "validation/results/S02/conciliation.json; T10-P02",
        p02_ok,
    )

    por_acordar_expectations = {
        "Metas y umbrales": ["responsible"],
        "Responsables empresariales de KPI": ["responsible"],
        "Roles y pruebas RLS": ["responsible"],
        "Merma por valor": ["responsible", "milestone"],
        "Origen de los sistemas y propietarios de las fuentes": ["responsible", "milestone"],
        "Frecuencia de actualización": ["responsible", "milestone"],
    }
    por_acordar_mismatches = []
    for item, fields in por_acordar_expectations.items():
        row = find_row(spec_pending, item)
        if row is None:
            por_acordar_mismatches.append({"item": item, "issue": "missing"})
            continue
        for field in fields:
            if not has("por acordar", row[field]):
                por_acordar_mismatches.append({"item": item, "field": field, "value": row[field]})
    add(
        "T10-P03",
        "pending",
        "Los pendientes sin respaldo conservan «Por acordar»; no se inventan responsables ni frecuencias.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"},
         {"path": "work/S02/content.json", "location": "pending"},
         {"path": "docs/decisions.md", "location": "PEN-017 a PEN-019"}],
        {"por_acordar_preserved": True, "mismatches": []},
        {"mismatches": por_acordar_mismatches,
         "items": list(por_acordar_expectations)},
        "Texto normalizado",
        "validation/results/S02/conciliation.json; T10-P03",
        not por_acordar_mismatches,
    )

    center = find_row(spec_pending, "Definición y validación de centro_distribucion y centro_distribucion_base")
    origin = find_row(spec_pending, "Origen de los sistemas y propietarios de las fuentes")
    frequency = find_row(spec_pending, "Frecuencia de actualización")
    p04_ok = (
        center is not None
        and origin is not None
        and frequency is not None
        and has("no resuelto", center["status"])
        and has("no resuelto", origin["status"])
        and has("no resuelta", frequency["status"])
    )
    add(
        "T10-P04",
        "pending",
        "Registrar un pendiente no lo resuelve: centro, origen y frecuencia siguen abiertos.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"},
         {"path": "work/S02/content.json", "location": "pending"},
         {"path": "docs/decisions.md", "location": "PEN-017 a PEN-019"}],
        {"center": "no resuelto", "origin": "no resuelto", "frequency": "no resuelta"},
        {"center": center, "origin": origin, "frequency": frequency},
        "Texto normalizado",
        "validation/results/S02/conciliation.json; T10-P04",
        p04_ok,
    )

    p05_ok = (
        center is not None
        and has("no resuelto", center["status"])
        and dcam["resolved"] is False
        and has("dud-s02-07", spec_md)
        and has("no se declara resuelta", spec_md)
        and all_has(["ausencia documentada", "no resuelta"], pptx_texts[1])
        and all_has(["ausencia documentada", "no resuelta"], pdf_page1)
    )
    add(
        "T10-P05",
        "pending",
        "La validación empresarial del centro sigue pendiente y la brecha DCAM no se declara resuelta.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3 y DUD-S02-07"},
         {"path": "work/S02/content.json", "location": "dcam"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositiva 2"},
         {"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "página 1"}],
        {"center_validation": "pendiente", "dcam_resolved": False},
        {"center_row": center, "dcam_resolved": dcam["resolved"],
         "pptx_open": all_has(["ausencia documentada", "no resuelta"], pptx_texts[1])},
        "Texto normalizado y booleano dcam.resolved",
        "validation/results/S02/conciliation.json; T10-P05",
        p05_ok,
    )

    p06_ok = (
        origin is not None
        and frequency is not None
        and has("no disponible", origin["status"])
        and has("no resuelto", origin["status"])
        and has("propietario por acordar", origin["responsible"])
        and has("por acordar", origin["milestone"])
        and has("por acordar", frequency["status"])
        and has("no resuelta", frequency["status"])
        and has("por acordar", frequency["responsible"])
        and has("por acordar", frequency["milestone"])
        and has("por acordar", spec_md)
        and has("por acordar", content_md)
    )
    add(
        "T10-P06",
        "pending",
        "Origen, propietarios y frecuencia de actualización siguen pendientes y marcados por acordar.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"},
         {"path": "work/S02/content.json", "location": "pending"},
         {"path": "docs/decisions.md", "location": "PEN-017 y PEN-018"}],
        {"origin": "no disponible; no resuelto", "owners": "por acordar",
         "frequency": "por acordar; no resuelta"},
        {"origin": origin, "frequency": frequency},
        "Texto normalizado",
        "validation/results/S02/conciliation.json; T10-P06",
        p06_ok,
    )

    session = find_row(spec_pending, "Sesión compartida de S02 (Rodrigo Tucuman)")
    p07_ok = (
        session is not None
        and has("no ejecutada ni declarada", session["status"])
        and has("rodrigo tucuman", session["responsible"])
        and content["claims"]["session_executed"] is False
        and not has("sesión ejecutada", spec_md)
        and not has("sesión ejecutada", content_md)
    )
    add(
        "T10-P07",
        "pending",
        "La sesión compartida no se declara ejecutada; Rodrigo Tucuman figura solo como designado.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"},
         {"path": "work/S02/content.json", "location": "pending y claims.session_executed"}],
        {"status": "No ejecutada ni declarada", "designated": "Rodrigo Tucuman",
         "executed_claim": False},
        {"session_row": session, "session_executed": content["claims"]["session_executed"],
         "spec_positive_claim": has("sesión ejecutada", spec_md)},
        "Texto normalizado; designación distinta de ejecución",
        "validation/results/S02/conciliation.json; T10-P07",
        p07_ok,
    )

    publication = find_row(spec_pending, "Publicación en Service")
    p08_ok = (
        publication is not None
        and has("prevista, no ejecutada", publication["status"])
        and content["claims"]["published"] is False
        and has("publicación en service", spec_md)
        and has("prevista, no ejecutada", spec_md)
    )
    add(
        "T10-P08",
        "pending",
        "La publicación en Service se registra como prevista y no ejecutada.",
        [{"path": "specs/002-s02-architecture/spec.md", "location": "§8.3"},
         {"path": "work/S02/content.json", "location": "pending y claims.published"}],
        {"status": "Prevista, no ejecutada", "published": False},
        {"publication_row": publication, "published": content["claims"]["published"]},
        "Texto normalizado y booleano claims.published",
        "validation/results/S02/conciliation.json; T10-P08",
        p08_ok,
    )

    # I: structural integrity
    i01_ok = (
        len(wb.sheetnames) == 12
        and xlsx_formula_count == 50
        and xlsx_dv_count == 11
        and xlsx_cf_ranges == 1
        and xlsx_cf_rules == 4
        and xlsx_merged == 19
        and any(str(rng) == "A3:AA3" for rng in ws_kpi.merged_cells.ranges)
        and ws_kpi.print_area in ("", None)
        and "A1:G11" in str(ws_map.print_area).replace("$", "").replace("'", "")
        and len(xlsx_map) == 5
    )
    add(
        "T10-I01",
        "integrity",
        "El Excel conserva 12 hojas, 50 fórmulas, 11 validaciones, 1 rango de formato condicional, 19 combinadas y el área de impresión del mapa.",
        [{"path": "deliverables/tracking/M4_Equipo06_Proyecto_Integrador_v2.xlsx", "location": "todas las hojas; S02 Mapa Silver; Fichas KPI"}],
        {"sheets": 12, "formulas": 50, "data_validations": 11, "cf_ranges": 1,
         "cf_rules": 4, "merged": 19, "kpi_header_merged": "A3:AA3",
         "kpi_print_area_empty": True, "map_print_area": "A1:G11"},
        {"sheets": len(wb.sheetnames), "formulas": xlsx_formula_count,
         "data_validations": xlsx_dv_count, "cf_ranges": xlsx_cf_ranges,
         "cf_rules": xlsx_cf_rules, "merged": xlsx_merged,
         "kpi_header_merged": any(str(rng) == "A3:AA3" for rng in ws_kpi.merged_cells.ranges),
         "kpi_print_area": ws_kpi.print_area, "map_print_area": ws_map.print_area},
        "Conteo y cadenas exactas",
        "validation/results/S02/conciliation.json; T10-I01",
        i01_ok,
    )

    pptx_slides_2_4 = "\n".join(pptx_texts[1:4])
    example_terms = ["acería", "aceria", "ejemplo", "laminación", "lam-01", "oee", "scada"]
    i02_ok = (
        len(pptx_slides) == 4
        and pptx_slide1_xml_sha == "0F944D0FB93C30E7CBAF0D7ED52D35900870A1E1E6BA20E31E0541D1770C7CC9"
        and not any(has(term, pptx_slides_2_4) for term in example_terms)
    )
    add(
        "T10-I02",
        "integrity",
        "El PPTX conserva cuatro diapositivas, la diapositiva 1 intacta y no replica el ejemplo de Acería en las diapositivas entregadas.",
        [{"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pptx", "location": "diapositivas 1-4; ppt/slides/slide1.xml"}],
        {"slide_count": 4, "slide1_xml_sha256": "0F944D0FB93C30E7CBAF0D7ED52D35900870A1E1E6BA20E31E0541D1770C7CC9",
         "example_terms_in_slides_2_4": 0},
        {"slide_count": len(pptx_slides), "slide1_xml_sha256": pptx_slide1_xml_sha,
         "example_terms_found": [term for term in example_terms if has(term, pptx_slides_2_4)]},
        "SHA-256 del XML y búsqueda textual",
        "validation/results/S02/conciliation.json; T10-I02",
        i02_ok,
    )

    pdf_size_ok = all(
        abs(width - 960.0) <= 0.5 and abs(height - 540.0) <= 0.5
        for width, height in pdf_sizes
    )
    pdf_no_example = not any(has(term, "\n".join(pdf_texts)) for term in example_terms)
    i03_ok = len(pdf_texts) == 3 and pdf_size_ok and pdf_no_example
    add(
        "T10-I03",
        "integrity",
        "El PDF tiene tres páginas 16:9 y no contiene el ejemplo de Acería.",
        [{"path": "deliverables/S02/M4_Equipo06_S02_Arquitectura.pdf", "location": "páginas 1-3"}],
        {"pages": 3, "page_size_pt": [960.0, 540.0], "example_terms": 0},
        {"pages": len(pdf_texts), "page_sizes_pt": pdf_sizes,
         "example_terms_found": [term for term in example_terms if has(term, "\n".join(pdf_texts))]},
        "Dimensiones con tolerancia de 0,5 pt; texto normalizado",
        "validation/results/S02/conciliation.json; T10-I03",
        i03_ok,
    )

    i04_ok = len(model_tables) == 5 and model_measure_count == 0 and model_relationship_count == 0
    add(
        "T10-I04",
        "integrity",
        "El modelo semántico actual conserva cinco tablas, cero medidas y cero relaciones.",
        [{"path": "powerbi/AndinaLog_03B.SemanticModel/definition", "location": "model.tmdl y tables/*.tmdl"}],
        {"tables": 5, "measures": 0, "relationships": 0},
        {"tables": len(model_tables), "table_names": [path.stem for path in model_tables],
         "measures": model_measure_count, "relationships": model_relationship_count},
        "Conteo TMDL",
        "validation/results/S02/conciliation.json; T10-I04",
        i04_ok,
    )

    finished = utc_now()
    failures = [check["id"] for check in checks if check["status"] == "FAIL"]
    all_pass = not failures
    report = {
        "schema_version": "1.0",
        "task": "T10",
        "phase": "Build",
        "subcase": "03B",
        "team": "Grupo 06",
        "scope": "Conciliación final de S02 sin modificar los artefactos auditados.",
        "started_at_utc": started,
        "finished_at_utc": finished,
        "tool": {
            "python": sys.version.split()[0],
            "openpyxl": openpyxl.__version__,
            "python_pptx": getattr(__import__("pptx"), "__version__", "unknown"),
            "pypdfium2": getattr(pdfium, "__version__", "unknown"),
            "com": False,
        },
        "hashes": {
            "before": before,
            "after": post,
            "expected": EXPECTED,
            "references": {
                "file_count_before": len(refs_before),
                "file_count_after": len(refs_after),
                "aggregate_sha256_before": refs_digest_before,
                "aggregate_sha256_after": refs_digest_after,
            },
        },
        "source_integrity": source_observations,
        "normalization": {
            "rules": [
                "NFKC",
                "espacios horizontales y saltos de línea colapsados",
                "casefold solo para comparar",
                "comillas tipográficas y guiones normalizados",
                "backticks y énfasis Markdown (**) retirados",
                "flecha → convertida a ->",
            ],
            "equivalences": [
                "spec 'decide, con revisión semanal' ~ entregables 'decide cada semana'; compactación admitida en T04 sin cambio de significado",
                "spec 'Cinco CSV oficiales' ~ diapositiva/PDF '5 fuentes oficiales'; mismo conjunto DATA-001 a DATA-005",
                "spec 'Interpretar incorrectamente' ~ diapositiva/PDF 'interpretar mal'; abreviatura sin cambio semántico",
                "Excel 'dividido entre'/'multiplicado por' ~ spec/contrato '/'/'×'; equivalencia aritmética",
                "etiquetas 'Hecho observado'/'Control principal'/'Control complementario' ~ 'Hecho'/'Control'/'Complemento'; compactación de espacio",
                "saltos de línea del PDF y del PPTX colapsados; no se altera el contenido",
            ],
            "fuzzy_matching": False,
        },
        "checks": checks,
        "summary": {
            "total": len(checks),
            "passed": len(checks) - len(failures),
            "failed": len(failures),
            "failures": failures,
        },
        "all_pass": all_pass,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"all_pass": all_pass, "summary": report["summary"], "output": rel(OUT)}, ensure_ascii=False))
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())

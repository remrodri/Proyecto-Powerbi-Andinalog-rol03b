#!/usr/bin/env python3
"""Valida el contrato de contenido de S02 (T02) y su versión Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT_JSON = ROOT / "work" / "S02" / "content.json"
CONTENT_MD = ROOT / "work" / "S02" / "content.md"
RESULTS = ROOT / "validation" / "results" / "S02" / "content_checks.json"

INVENTORY_FREQUENCY = (
    "Sin periodicidad fija: una fila por lote contiene las fechas de ingreso y "
    "salida; actualización por acordar"
)
ORIGIN = "No documentado / por acordar"

FORBIDDEN = [
    r"(?<!no )(?<!No )se ejecut[oó]",
    r"(?<!no )(?<!No )se ejecutaron",
    r"validaci[oó]n empresarial (?:ya )?(?:realizada|ejecutada)",
    r"sesi[oó]n (?:ya )?(?:realizada|ejecutada)",
    r"DAX (?:ya )?(?:implementado|probado|ejecutado)",
    r"RLS (?:ya )?(?:probado|verificado|aprobado)",
    r"publicad[oa] en (?:el )?Service",
]


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def walk_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield key
            yield from walk_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)


def flatten_text(value) -> str:
    return "\n".join(str(item) for item in walk_strings(value))


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def render_md(content: dict) -> str:
    lines = []
    meta = content["spec"]
    lines += [
        "# Contrato de contenido — S02",
        "",
        "## Metadatos",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Hito | {content['hit']} |",
        f"| Subcaso | {content['subcase']} |",
        f"| Equipo | {content['team']} |",
        f"| Tarea | {content['task']} |",
        f"| Versión del contrato | {content['schema_version']} |",
        f"| Spec | {meta['path']} v{meta['version']} |",
        f"| Aprobación de la spec | {meta['approved']} |",
        f"| Huella de la spec | {meta['sha256']} |",
        "",
        "## Decisión",
        "",
        f"> {content['decision']['sentence']}",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Decisor | {content['decision']['who']} |",
        f"| Decisión | {content['decision']['what']} |",
        f"| Frecuencia | {content['decision']['how_often']} |",
        f"| Fuente | {content['decision']['source']} |",
        f"| Cita de la spec | {content['decision']['spec_quote']} |",
        "",
        "## Bloques de la diapositiva 2",
        "",
        "| Bloque | Etiqueta | Texto |",
        "| --- | --- | --- |",
    ]
    for block in content["slide_blocks"]:
        lines.append(f"| {block['id']} | {block['label']} | {block['text']} |")

    lines += [
        "",
        "## Mapa Silver",
        "",
        f"Origen por archivo: **{content['map']['origin']}**",
        "",
        f"Alcance: {content['map']['scope']}. Filas: {content['map']['row_count']}.",
        "",
        "| ID | Archivo / tabla | Granularidad | Identificador único | Frecuencia | Propietario | Riesgo | Control propuesto |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for row in content["map"]["rows"]:
        fields = row["fields"]
        lines.append(
            "| {id} | {archivo} | {granularidad} | {identificador_unico} | "
            "{frecuencia} | {propietario} | {riesgo} | {control_propuesto} |".format(
                id=row["id"], **fields
            )
        )

    lines += [
        "",
        "## KPI tácticos",
        "",
        "| # | KPI | Nivel | Fórmula en palabras | Unidad | Denominador | Referencia | Nota |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for kpi in content["kpis"]:
        lines.append(
            f"| {kpi['id']} | {kpi['name']} | {kpi['level']} | {kpi['formula']} | "
            f"{kpi['unit']} | {kpi['denominator']} | {kpi['reference']} | {kpi['notes']} |"
        )

    support = content["support_measure"]
    lines += [
        "",
        "## Medida de apoyo",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| Nombre | {support['name']} |",
        f"| Valor | {support['value']} |",
        f"| Unidad | {support['unit']} |",
        f"| Es KPI principal | {'Sí' if support['is_kpi'] else 'No'} |",
        f"| Nota | {support['note']} |",
        "",
        "## KPI excluidos",
        "",
        "| KPI | Motivo | Hito |",
        "| --- | --- | --- |",
    ]
    for item in content["excluded_kpis"]:
        lines.append(f"| {item['name']} | {item['reason']} | {item['milestone']} |")

    dcam = content["dcam"]
    lines += [
        "",
        "## Brecha DCAM",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| ID | {dcam['gap_id']} |",
        f"| Brecha | {dcam['gap']} |",
        f"| Estado | {dcam['state']} |",
        f"| Resuelta | {'Sí' if dcam['resolved'] else 'No'} |",
        f"| Riesgo | {dcam['risk']} |",
        f"| Hecho observado | {dcam['observed_fact']} |",
        f"| Límite | {dcam['limit']} |",
        f"| Control principal | {dcam['primary_control']} |",
        f"| Control complementario | {dcam['complementary_control']} |",
        f"| Validación | {dcam['validation_status']} |",
        f"| Seguimiento | {dcam['follow_up']} |",
        f"| Evidencia | {dcam['evidence']} |",
        "",
        "## Pendientes",
        "",
        "| Pendiente | Estado al cierre de S02 | Responsable | Hito de tratamiento |",
        "| --- | --- | --- | --- |",
    ]
    for item in content["pending"]:
        lines.append(
            f"| {item['item']} | {item['status']} | {item['responsible']} | {item['milestone']} |"
        )

    wms = content["wms_note"]
    lines += [
        "",
        "## Nota WMS separada",
        "",
        "| Campo | Valor |",
        "| --- | --- |",
        f"| ID | {wms['id']} |",
        f"| Archivo | {wms['file']} |",
        f"| Rol | {wms['role']} |",
        f"| Grano | {wms['scope']} |",
        f"| En el mapa | {'Sí' if wms['in_map'] else 'No'} |",
        f"| Cargada | {'Sí' if wms['loaded'] else 'No'} |",
        f"| Cuenta como oficial | {'Sí' if wms['counts_as_official'] else 'No'} |",
        f"| Nota | {wms['note']} |",
        "",
        "## Declaraciones de alcance",
        "",
        "| Declaración | Valor |",
        "| --- | --- |",
    ]
    for key, value in content["claims"].items():
        lines.append(f"| {key} | {'Sí' if value else 'No'} |")
    lines.append("")
    return "\n".join(lines)


def table_after(lines: list[str], heading: str) -> tuple[list[str], list[list[str]]]:
    try:
        index = lines.index(heading)
    except ValueError as exc:
        raise ValueError(f"No se encontró la sección {heading!r}") from exc
    cursor = index + 1
    while cursor < len(lines) and not lines[cursor].startswith("|"):
        cursor += 1
    table: list[list[str]] = []
    while cursor < len(lines) and lines[cursor].startswith("|"):
        cells = [cell.strip() for cell in lines[cursor].strip().strip("|").split("|")]
        table.append(cells)
        cursor += 1
    if len(table) < 3:
        raise ValueError(f"Tabla insuficiente en {heading!r}")
    return table[0], table[2:]


def compare_table(
    parsed: list[list[str]], expected: list[list[str]], label: str, failures: list[str]
) -> None:
    if len(parsed) != len(expected):
        failures.append(f"{label}: filas Markdown {len(parsed)} != JSON {len(expected)}")
        return
    for index, (got, want) in enumerate(zip(parsed, expected), start=1):
        if len(got) != len(want):
            failures.append(f"{label} fila {index}: columnas {len(got)} != {len(want)}")
            continue
        for column, (left, right) in enumerate(zip(got, want), start=1):
            if normalize(left) != normalize(right):
                failures.append(
                    f"{label} fila {index} columna {column}: "
                    f"Markdown {left!r} != JSON {right!r}"
                )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-md", action="store_true", help="Regenera content.md desde JSON")
    args = parser.parse_args()

    checks = []
    failures = []

    def check(check_id: str, description: str, condition: bool, detail: str = "") -> None:
        checks.append(
            {
                "id": check_id,
                "description": description,
                "ok": bool(condition),
                "detail": detail,
            }
        )
        if not condition:
            failures.append(f"{check_id}: {description}" + (f" — {detail}" if detail else ""))

    if not CONTENT_JSON.exists():
        print(f"Falta {CONTENT_JSON}", file=sys.stderr)
        return 2
    content = load_json(CONTENT_JSON)
    text = flatten_text(content)

    if args.write_md:
        CONTENT_MD.write_text(render_md(content), encoding="utf-8", newline="\n")
    if not CONTENT_MD.exists():
        print(f"Falta {CONTENT_MD}; ejecuta con --write-md", file=sys.stderr)
        return 2
    markdown = CONTENT_MD.read_text(encoding="utf-8")

    check("C01", "Hito y spec correctos", content["hit"] == "S02" and content["spec"]["version"] == "0.4",
          f"hit={content['hit']}, version={content['spec']['version']}")
    check("C02", "Frase de decisión única con decisor y frecuencia",
          content["decision"]["sentence"].count(".") == 1
          and "Jefatura de Operaciones" in content["decision"]["sentence"]
          and "cada semana" in content["decision"]["sentence"],
          content["decision"]["sentence"])
    check("C03", "Cita de la spec conserva la revisión semanal",
          "con revisión semanal" in content["decision"]["spec_quote"]
          and content["decision"]["spec_quote"].endswith("(DEC-016)."))

    blocks = {block["id"]: block for block in content["slide_blocks"]}
    required_blocks = {
        "header", "decision", "origin", "silver", "power_query", "model",
        "indicator", "gap", "risk", "observed_fact", "limit",
        "primary_control", "complementary_control", "pending",
    }
    check("C04", "Bloques de diapositiva 2 completos y no vacíos",
          required_blocks.issubset(blocks)
          and all(block["text"].strip() for block in content["slide_blocks"])
          and len(blocks) == len(content["slide_blocks"]),
          f"bloques={len(blocks)}")
    check("C05", "El bloque Decisión coincide con la frase normativa",
          blocks.get("decision", {}).get("text") == content["decision"]["sentence"])

    rows = content["map"]["rows"]
    field_order = content["map"]["field_order"]
    check("C06", "Exactamente cinco filas DATA-001 a DATA-005",
          len(rows) == 5 and [row["id"] for row in rows] == [f"DATA-00{i}" for i in range(1, 6)],
          f"ids={[row['id'] for row in rows]}")
    check("C07", "Cada fila tiene exactamente siete campos del mapa",
          all(len(row["fields"]) == 7 and set(row["fields"]) == set(field_order) for row in rows),
          f"field_order={len(field_order)}")
    check("C08", "Origen por archivo no documentado / por acordar",
          content["map"]["origin"] == ORIGIN
          and all(row["origen"] == ORIGIN for row in rows))
    check("C09", "WMS queda fuera de las cinco filas del mapa",
          "wms" not in json.dumps(content["map"], ensure_ascii=False).lower()
          and content["wms_note"]["in_map"] is False,
          f"in_map={content['wms_note']['in_map']}")
    check("C10", "Frecuencia de Inventario literal",
          rows[3]["fields"]["frecuencia"] == INVENTORY_FREQUENCY,
          rows[3]["fields"]["frecuencia"])
    check("C11", "Propietarios y frecuencias sin respaldo quedan por acordar",
          all("por acordar" in row["fields"]["propietario"].lower() for row in rows)
          and all("por acordar" in row["fields"]["frecuencia"].lower() for row in rows))

    kpis = content["kpis"]
    kpi_names = [kpi["name"].casefold() for kpi in kpis]
    check("C12", "Exactamente cinco KPI tácticos",
          len(kpis) == 5 and all(kpi["level"] == "Táctico" for kpi in kpis),
          f"niveles={[kpi['level'] for kpi in kpis]}")
    check("C13", "Cada KPI declara fórmula, unidad y denominador",
          all(kpi["formula"].strip() and kpi["unit"].strip() and kpi["denominator"].strip()
              for kpi in kpis))
    check("C14", "Identificador dias_en_almacen exacto y sin tilde",
          "dias_en_almacen" in kpis[4]["formula"] and "dias_en_almacén" not in text)
    check("C15", "Medida de apoyo separada del catálogo de KPI",
          content["support_measure"]["is_kpi"] is False
          and content["support_measure"]["name"].casefold() not in kpi_names)
    check("C16", "Merma por valor fuera del catálogo de KPI",
          "merma por valor" not in kpi_names
          and any(item["name"].casefold() == "merma por valor" for item in content["excluded_kpis"]))

    dcam = content["dcam"]
    check("C17", "Brecha DCAM documentada y no resuelta",
          dcam["gap_id"] == "DUD-S02-07"
          and "ausencia documentada" in dcam["state"].lower()
          and dcam["resolved"] is False)
    check("C18", "Riesgo, hecho, límite y controles separados",
          dcam["risk"].startswith("Interpretar incorrectamente")
          and "8.000 viajes emparejados" in dcam["observed_fact"]
          and "no demuestra el significado empresarial" in dcam["limit"]
          and "centro_distribucion_base" in dcam["complementary_control"]
          and "dim_centro" in dcam["complementary_control"]
          and len({dcam[key] for key in (
              "risk", "observed_fact", "limit", "primary_control", "complementary_control"
          )}) == 5)

    pending = content["pending"]
    check("C19", "Pendientes con responsable e hito",
          len(pending) == 13
          and all(item["responsible"].strip() and item["milestone"].strip() for item in pending),
          f"pendientes={len(pending)}")
    session = next((item for item in pending if "Sesión compartida" in item["item"]), {})
    publication = next((item for item in pending if item["item"] == "Publicación en Service"), {})
    check("C20", "Sesión y publicación no se declaran ejecutadas",
          "No ejecutada" in session.get("status", "")
          and "no ejecutada" in publication.get("status", "").lower())

    check("C21", "Declaraciones de alcance en falso",
          all(value is False for value in content["claims"].values()),
          json.dumps(content["claims"], ensure_ascii=False))
    forbidden_hits = [pattern for pattern in FORBIDDEN if re.search(pattern, text, re.I)]
    check("C22", "Sin afirmaciones de ejecución no demostradas",
          not forbidden_hits, f"coincidencias={forbidden_hits}")
    check("C23", "Nota WMS separada, no cargada y sin contar como oficial",
          content["wms_note"]["loaded"] is False
          and content["wms_note"]["counts_as_official"] is False
          and "No forma parte del mapa" in content["wms_note"]["note"])

    rendered = render_md(content)
    check("C24", "content.md es la representación determinista de content.json",
          normalize(rendered) == normalize(markdown),
          f"json_chars={len(rendered)}, md_chars={len(markdown)}")

    md_failures: list[str] = []
    try:
        lines = markdown.splitlines()
        header, data = table_after(lines, "## Mapa Silver")
        expected_header = [
            "ID", "Archivo / tabla", "Granularidad", "Identificador único",
            "Frecuencia", "Propietario", "Riesgo", "Control propuesto",
        ]
        if header != expected_header:
            md_failures.append(f"Encabezado del mapa inesperado: {header}")
        expected_rows = [
            [row["id"]] + [row["fields"][key] for key in field_order] for row in rows
        ]
        compare_table(data, expected_rows, "Mapa", md_failures)

        header, data = table_after(lines, "## KPI tácticos")
        expected_rows = [[
            str(kpi["id"]), kpi["name"], kpi["level"], kpi["formula"], kpi["unit"],
            kpi["denominator"], kpi["reference"], kpi["notes"],
        ] for kpi in kpis]
        compare_table(data, expected_rows, "KPI", md_failures)

        header, data = table_after(lines, "## Pendientes")
        expected_rows = [[
            item["item"], item["status"], item["responsible"], item["milestone"],
        ] for item in pending]
        compare_table(data, expected_rows, "Pendientes", md_failures)
    except ValueError as exc:
        md_failures.append(str(exc))

    check("C25", "Tablas Markdown conservan el contenido material del JSON",
          not md_failures, " | ".join(md_failures[:5]))
    check("C26", "Literales obligatorios presentes también en Markdown",
          INVENTORY_FREQUENCY in markdown
          and ORIGIN in markdown
          and "dias_en_almacen" in markdown
          and "Número de lotes vencidos" in markdown,
          f"md_chars={len(markdown)}")

    summary = {
        "total": len(checks),
        "passed": sum(1 for item in checks if item["ok"]),
        "failed": sum(1 for item in checks if not item["ok"]),
    }
    result = {
        "task": "T02",
        "hit": "S02",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "files": {
            "content_json": str(CONTENT_JSON.relative_to(ROOT)).replace("\\", "/"),
            "content_md": str(CONTENT_MD.relative_to(ROOT)).replace("\\", "/"),
            "content_json_sha256": sha256_file(CONTENT_JSON),
            "content_md_sha256": sha256_file(CONTENT_MD),
        },
        "checks": checks,
        "summary": summary,
        "json_markdown": {
            "rendered_identical": next(item["ok"] for item in checks if item["id"] == "C24"),
            "rows_json": len(rows),
            "kpis_json": len(kpis),
            "fields_per_row": len(field_order),
            "pending_json": len(pending),
        },
    }
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for failure in failures:
        print(f"FAIL {failure}", file=sys.stderr)
    print(f"T02: {summary['passed']}/{summary['total']} checks; failed={summary['failed']}")
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())

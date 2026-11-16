#!/usr/bin/env python3
"""
build_definitive_diagram.py
Genera el Diagrama Definitivo de Bloques Funcionales Integral en HTML5 (con Semantic Zoom,
Inspector Completo del Catálogo, Buscador Global, Matriz 100% y Visor Mermaid Offline)
y sincroniza la suite Mermaid (.mmd/.md) y el Visor HTML Maestro.
"""

import json
import os
import re
from collections import Counter
from html import escape

from definitive_arch_data import (
    CANVAS_W,
    CANVAS_H,
    FRONTIER,
    ZONES,
    GUI_PLACEMENT,
    NODES,
    FLOWS,
    audit_geometry,
)
from build_mermaid_suite import (
    MERMAID_01,
    MERMAID_02,
    MERMAID_03,
    MERMAID_04,
    MERMAID_05,
    build_all_mermaid,
)

BASE_DIR = "/home/marco/Projects/NexoVitalis360"
CATALOG_JSON = "/home/marco/.gemini/antigravity-cli/brain/79aa52d5-a86f-4715-939d-0c53dd4679cb/scratch/catalogo_full_v2.json"

VISOR_DIR = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/VISOR_HTML_ARQUITECTURA_v01.00")
VISTA_LOGICA_DIR = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica")
COMPORTAMIENTO_DIR = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/02_Diagrama_Comportamiento")

OUT_HTML_VISOR = os.path.join(VISOR_DIR, "fig_definitivo_bloques_funcionales_integral.html")
OUT_HTML_VL = os.path.join(VISTA_LOGICA_DIR, "Figura_3_4_Bloques_Funcionales_Integral_Definitivo_v02.00.html")
OUT_HTML_COMP = os.path.join(COMPORTAMIENTO_DIR, "Figura_7_6_Bloques_Funcionales_Definitivo_v02.00.html")

EDU_TO_BLOCK = {
    "EDU-0014": "B1", "EDU-0021": "B1",
    "EDU-0023": "B2", "EDU-0029": "B2",
    "EDU-0016": "B3", "EDU-0017": "B3",
    "EDU-0008": "B4", "EDU-0012": "B4", "EDU-0013": "B4", "EDU-0018": "B4",
    "EDU-0019": "B5",
    "EDU-0020": "B6",
    "EDU-0010": "B7", "EDU-0015": "B7", "EDU-0025": "B7", "EDU-0027": "B7",
    "EDU-0028": "B7", "EDU-0030": "B7", "EDU-0032": "B7", "EDU-0035": "B7",
    "EDU-0033": "B8", "EDU-0034": "B8", "EDU-0036": "B8", "EDU-0037": "B8",
    "EDU-0038": "B9",
    "EDU-0009": "B10", "EDU-0011": "B10",
}

RNF_NODE_MAP = {
    "RNF-0001|Control de Acceso Clínico a Documentos": ["B0", "B7", "B10", "EP-03", "EP-04", "EXT-A4"],
    "RNF-0002|Encriptación de Datos Sensibles": ["B1", "B7", "B11", "B12"],
    "RNF-0003|Registro de Auditoría (Logs)": ["B0", "B4", "B9", "B10", "B11", "EP-04", "EXT-A4"],
    "RNF-0004|Algoritmo Anticolisión de Citas": ["B3", "B4", "B11"],
    "RNF-0004|Concurrencia de Citas": ["B3", "B4", "B11"],
    "RNF-0005|Tiempo de Respuesta en Búsqueda de Historias Clínicas": ["B1", "B7", "B11", "EP-03", "EXT-A3"],
    "RNF-0006|Renderizado de Alertas Visuales Inmediatas": ["B2", "B7", "B12", "EP-03", "EP-05", "EXT-A3"],
    "RNF-0007|Diseño Responsivo para Reprogramación": ["B4", "EP-01", "EP-02", "EXT-A1", "EXT-A2", "INFRA-STD"],
    "RNF-0008|Sincronización Automática de Enlaces de Videollamada": ["B5", "EP-05", "EXT-API1"],
    "RNF-0009|Automatización de Notificaciones por Mensajería": ["B6", "B12", "EP-06", "EXT-API2"],
    "RNF-0010|Restricción por Consentimiento Informado": ["B2", "B4", "B11", "EP-01", "EP-02"],
    "RNF-0011|Estructura de Persistencia de Datos Relacional": ["B4", "B8", "B9", "B11", "EXT-A4"],
    "RNF-0012|Tecnologías de Desarrollo Backend y Frontend": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B12", "EP-01", "EP-02", "EP-03", "EP-04", "INFRA-STD"],
    "RNF-0013|Mecanismo de Autenticación Desacoplada (JWT)": ["B0", "B10", "EP-01", "EP-02", "EP-03", "EP-04", "EP-05", "EXT-A1", "EXT-A2", "EXT-A3", "EXT-A4"],
    "RNF-0014|Cifrado de Datos en Tránsito": ["B0", "B5", "B8", "B10", "EP-01", "EP-02", "EP-03", "EP-04", "EP-05", "EP-06", "EXT-A1", "EXT-A2", "EXT-A3", "EXT-A4", "EXT-API1", "EXT-API2", "EXT-API3", "EXT-API4"],
    "RNF-0015|Tiempo de Respuesta de la API de Disponibilidad": ["B0", "B3", "B4", "B11", "EP-02", "EXT-A2"],
    "RNF-0016|Hardware y Sistema Operativo de Estaciones de Trabajo del Cliente": ["EXT-A2", "EXT-A3", "EXT-A4", "EP-02", "EP-03", "INFRA-STD"],
    "RNF-0017|Gestión de Memoria Virtual del SO y Paginación en Clientes": ["EXT-A2", "EXT-A3", "EP-02", "EP-03", "INFRA-STD"],
    "RNF-0018|Compatibilidad con Dispositivos Móviles Multi-Fabricante": ["EXT-A1", "EXT-A3", "EP-01", "INFRA-STD"],
    "RNF-0019|Motores de Navegadores Web e Interacción con el Sistema Operativo": ["B0", "B5", "EP-01", "EP-02", "EP-03", "EP-05", "EXT-A1", "EXT-A2", "EXT-A3", "EXT-A4", "INFRA-STD"],
    "RNF-0020|Hardware y Sistema Operativo de Servidores de Producción": ["B11", "B12", "INFRA-STD"],
    "RNF-0021|Herramienta Oficial de Modelado de Procesos (Bonita BPM / BPMN 2.0)": ["B2", "B4", "B8", "INFRA-STD"],
    "RNF-0022|Herramientas de Modelado Arquitectónico (OMG UML 2.5)": ["CTX-CAT", "INFRA-STD"],
    "RNF-0023|Interoperabilidad con Facturación Electrónica SUNAT (UBL 2.1)": ["B8", "EP-02", "EXT-API3"],
    "RNF-0024|Almacenamiento Seguro de Objetos para Documentos Clínicos y Vouchers": ["B2", "B7", "B8", "B9", "B12"],
    "RNF-0025|Topología de Red, Segmentación VPC y Firewall Perimetral": ["B0", "B10", "B11", "B12", "EP-06", "INFRA-STD"],
    "RNF-0026|Perfil y Competencias Técnicas del Equipo de Codificadores": ["B0", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "EP-01", "EP-02", "EP-03", "EP-04", "EP-05", "EP-06", "INFRA-STD", "CTX-CAT"],
    "RNF-0027|Arquitectura de Pizarra para Soporte a Decisiones Clínicas Pediátricas": ["B2", "B3", "B4", "B12", "EP-03", "EP-05"],
}


def load_enriched_catalog():
    with open(CATALOG_JSON, "r", encoding="utf-8") as f:
        raw = json.load(f)

    risks_ila = {}
    for row in raw["otros"][3]["rows"][1:]:
        if row and row[0]:
            risks_ila[row[0].strip()] = {
                "clave": row[0].strip(),
                "riesgo": row[1].strip() if len(row) > 1 else "",
                "prob": row[2].strip() if len(row) > 2 else "",
                "impacto": row[4].strip() if len(row) > 4 else "",
                "mitigacion": row[9].strip() if len(row) > 9 else "",
            }

    risks_esp = {}
    for row in raw["otros"][4]["rows"][1:]:
        if row and row[0]:
            risks_esp[row[0].strip()] = {
                "clave": row[0].strip(),
                "riesgo": row[1].strip() if len(row) > 1 else "",
                "mitigacion": row[9].strip() if len(row) > 9 else "",
            }

    esps_raw = raw.get("esps", {})
    esp_by_ila = {}
    for hcode, rec in esps_raw.items():
        if not rec.get("empty_in_doc") and rec.get("ila_ref"):
            esp_by_ila[rec["ila_ref"]] = rec

    pruebas_map = raw.get("pruebas_map", {})
    pruebas_tipos = raw.get("pruebas_tipos", {})

    educciones = []
    for e in raw["educciones"]:
        code = e.get("Código educción", "").strip()
        educciones.append({
            "codigo": code,
            "nombre": e.get("Nombre", "").strip(),
            "actor": e.get("Actor", "").strip(),
            "importancia": e.get("Importancia", "").strip(),
            "version": e.get("Versión", "").strip(),
            "descripcion": e.get("Descripción", "").strip(),
            "bloque": EDU_TO_BLOCK[code],
        })

    ilaciones = []
    for idx, il in enumerate(raw["ilaciones"]):
        code = il.get("Código ilación", "").strip()
        edu_code = il.get("Código educción", "").strip()
        if edu_code == "EDU-00019":
            edu_code = "EDU-0019"
        block_id = EDU_TO_BLOCK[edu_code]
        blob = json.dumps(il, ensure_ascii=False)
        tbs = sorted(set(re.findall(r"TB_[A-Z0-9_]+", blob)))
        if edu_code == "EDU-0013" and not tbs:
            tbs = ["TB_CITAS", "TB_HORARIOS", "TB_HISTORIAL_CITAS", "TB_REPROGRAMACIONES*"]
        if edu_code == "EDU-0019" and not tbs:
            tbs = ["TB_CITAS", "TB_ENLACES_VIDEOCONFERENCIA*"]
        guis = sorted(set(re.findall(r"GUI-[0-9A-Za-z_-]+", blob)))
        mdls = sorted(set(re.findall(r"MDL[_-][0-9A-Za-z_-]+", blob)))

        esp_rec = esp_by_ila.get(code)
        esp_key = esp_rec["heading_code"] if esp_rec else f"ESP-{idx+1:04d}"
        esp_art = esp_rec.get("Código de artefactos asociados", "").strip() if esp_rec else ""
        esp_proc = esp_rec.get("Procedimiento", "").strip() if esp_rec else ""
        m_trig = re.search(r"CAPTURA_EVENTO\s*\(([^)]+)\)", esp_proc)
        esp_trigger = m_trig.group(1).strip() if m_trig else ""
        pr_rec = pruebas_map.get(esp_key)

        ilaciones.append({
            "codigo": code,
            "nombre": il.get("Nombre", "").strip(),
            "edu": edu_code,
            "bloque": block_id,
            "actor": il.get("Actor", "").strip(),
            "importancia": il.get("Importancia", "").strip(),
            "precondicion": il.get("Precondición", "").strip(),
            "procedimiento": il.get("Procedimiento", "").strip(),
            "postcondicion": il.get("Postcondición", "").strip(),
            "tbs": tbs,
            "guis": guis,
            "mdls": mdls,
            "esp_code": esp_key,
            "esp_empty": (esp_rec is None),
            "esp_trigger": esp_trigger,
            "esp_artefactos": esp_art,
            "esp_pre": esp_rec.get("Precondición", "").strip() if esp_rec else "",
            "esp_proc": esp_proc,
            "esp_post": esp_rec.get("Postcondición", "").strip() if esp_rec else "",
            "prueba_clave": pr_rec.get("clave", "") if pr_rec else "",
            "prueba_desc": pr_rec.get("descripcion", "") if pr_rec else "",
            "prueba_tipo": pr_rec.get("tipo", "") if pr_rec else "",
            "prueba_tipo_desc": pruebas_tipos.get(pr_rec.get("tipo", ""), "") if pr_rec else "",
            "riesgo_ila": risks_ila.get(code),
            "riesgo_esp": risks_esp.get(esp_key),
        })

    rnfs = []
    for idx, r in enumerate(raw["rnfs"]):
        code = r.get("Código", "").strip()
        name = r.get("Nombre", "").strip()
        key = f"{code}|{name}"
        nodes = RNF_NODE_MAP[key]
        disp_code = code
        if code == "RNF-0004" and "Algoritmo" in name:
            disp_code = "RNF-0004 (Anticolisión)"
        elif code == "RNF-0004" and "Concurrencia" in name:
            disp_code = "RNF-0004 (Concurrencia)"
        rnfs.append({
            "uid": f"RNF_REC_{idx+1:02d}",
            "codigo": code,
            "display_code": disp_code,
            "nombre": name,
            "atributo": r.get("Atributo de calidad", "").strip(),
            "importancia": r.get("Importancia", "").strip(),
            "descripcion": r.get("Descripción", "").strip(),
            "comentario": "" if r.get("Comentario", "Ninguno").strip() == "Ninguno" else r.get("Comentario", "").strip(),
            "nodos": nodes,
        })

    placement_by_gui = {p["gui"]: p for p in GUI_PLACEMENT}
    guis = []
    for g in raw["gui_sections"]:
        title = g["gui"]
        m_edu = re.search(r"EDU-(\d+)", title)
        m_gui = re.search(r"(GUI-\d+)", title)
        edu_ref = f"EDU-{int(m_edu.group(1)):04d}" if m_edu else ""
        gui_code = m_gui.group(1) if m_gui else ""
        pl = placement_by_gui.get(gui_code, {})
        is_blank = "(en blanco)" in title.lower()
        block_id = pl.get("bloque") or EDU_TO_BLOCK.get(edu_ref, "CTX-CAT")
        guis.append({
            "gui_code": gui_code,
            "titulo": title,
            "nombre_corto": pl.get("titulo", ""),
            "ep": pl.get("ep", ""),
            "edu": edu_ref,
            "bloque": block_id,
            "en_blanco": is_blank,
            "modales": g["modales"],
        })

    assert len(educciones) == 27
    assert len(ilaciones) == 108
    assert len(rnfs) == 28
    assert len(guis) == 28

    return {
        "organizaciones": [{"codigo": o.get("Código"), "nombre": o.get("Nombre")} for o in raw["organizaciones"]],
        "actores_catalogo": [{"codigo": a.get("Código"), "rol": a.get("Rol"), "tipo": a.get("Tipo"), "comentario": a.get("Comentario")} for a in raw["actores"]],
        "expertos": raw.get("expertos", []),
        "educciones": educciones,
        "ilaciones": ilaciones,
        "rnfs": rnfs,
        "guis": guis,
        "gui_placement": GUI_PLACEMENT,
        "esps_resumen": {
            "total_headings": len(esps_raw),
            "filled": sum(1 for v in esps_raw.values() if not v.get("empty_in_doc")),
            "empty_headings": [k for k, v in sorted(esps_raw.items()) if v.get("empty_in_doc")],
        },
        "pruebas_map": list(pruebas_map.values()),
        "pruebas_tipos": pruebas_tipos,
    }


def _split_svg_subpaths(path_str):
    """Divide múltiples comandos M... en subrutas independientes para renderizar puntas de flecha en cada destino."""
    parts = [p.strip() for p in re.split(r"(?=M\s)", path_str.strip()) if p.strip()]
    return parts


def render_svg_flows():
    """Genera las capas SVG de flechas + áreas de clic anchas transparentes."""
    out = []
    for f in FLOWS:
        fid = escape(f["id"])
        src = escape(f["src"])
        dst = escape(f["dst"])
        is_async = f["kind"] == "async"
        stroke_dash = ' stroke-dasharray="8,5"' if is_async else ""
        base_width = "2.4" if is_async else "2.8"
        subpaths = _split_svg_subpaths(f["path"])

        out.append(f'<g class="flow-edge-group" data-flow="{fid}" data-src="{src}" data-dst="{dst}">')
        is_bidir = bool(f.get("bidir"))
        for idx, sp in enumerate(subpaths):
            need_arrow = not (f["id"] == "F29" and idx > 0)
            marker_end = ' marker-end="url(#arrow)"' if need_arrow else ""
            marker_start = ' marker-start="url(#arrow)"' if (is_bidir and idx == 0) else ""
            out.append(
                f'  <path class="flow-line" d="{sp}" stroke="#000000" stroke-width="{base_width}"'
                f'{stroke_dash} fill="none"{marker_start}{marker_end} />'
            )
            out.append(
                f'  <path class="flow-hit" d="{sp}" stroke="transparent" stroke-width="14" fill="none" />'
            )
        out.append("</g>")
    return "\n        ".join(out)


def render_flow_pills():
    """Genera las píldoras interactivas con texto macro/detalle progresivo."""
    out = []
    for f in FLOWS:
        fid = escape(f["id"])
        px, py = f["pill"]
        core = escape(f["core"])
        detail = escape(f["detail"])
        src = escape(f["src"])
        dst = escape(f["dst"])
        out.append(
            f'<div class="flow-pill" data-flow="{fid}" data-src="{src}" data-dst="{dst}" '
            f'style="left: {px}px; top: {py}px;">'
            f'<span class="pill-core">{core}</span>'
            f'<span class="pill-detail">{detail}</span>'
            f'</div>'
        )
    return "\n      ".join(out)


def render_zones():
    """Genera los recuadros de zonas de despliegue (Zona 1 Cliente/EP, Zona 2 DMZ, Zona 4 Datos)."""
    out = []
    for z in ZONES:
        zx, zy, zw, zh = z["rect"]
        out.append(
            f'<div class="zone-box" style="left:{zx}px; top:{zy}px; width:{zw}px; height:{zh}px;">'
            f'<span class="zone-badge">{escape(z["label"])}</span>'
            f'</div>'
        )
    return "\n      ".join(out)


def render_node_cards(catalog):
    """Genera las tarjetas interactivas DOM respetando el paradigma B&W + Sharp Edges."""
    edu_by_blk = {}
    for e in catalog["educciones"]:
        edu_by_blk.setdefault(e["bloque"], []).append(e)
    ila_by_blk = {}
    for il in catalog["ilaciones"]:
        ila_by_blk.setdefault(il["bloque"], []).append(il)
    rnf_by_node = {}
    for r in catalog["rnfs"]:
        for nid in r["nodos"]:
            rnf_by_node.setdefault(nid, []).append(r)

    out = []
    for n in NODES:
        nid = n["id"]
        x, y, w, h = n["rect"]
        kind_cls = {
            "hub": "card-hub",
            "entry": "card-entry",
            "ext": "card-ext",
            "dashed": "card-dashed",
            "legend": "card-dashed",
            "normal": "",
        }.get(n["kind"], "")

        edus = edu_by_blk.get(nid, [])
        ilas = ila_by_blk.get(nid, [])
        rnfs = rnf_by_node.get(nid, [])

        tag_parts = [escape(n["capa"])]
        if edus:
            tag_parts.append(f"{len(edus)} EDU")
        if ilas:
            tag_parts.append(f"{len(ilas)} ILA/ESP")
        if rnfs:
            tag_parts.append(f"{len(rnfs)} RNF")
        if n["apis"]:
            tag_parts.append(f"{len(n['apis'])} API")
        if n["tbs"]:
            tag_parts.append(f"{len(n['tbs'])} TB/S3")
        tag_str = " • ".join(tag_parts)

        gui_strip_html = ""
        if n.get("gui_strip"):
            gui_strip_html = f'\n        <div class="box-gui-strip">{escape(n["gui_strip"])}</div>'

        lines_html = "\n          ".join(f"<p>• {line}</p>" if not line.startswith("<") else f"<p>{line}</p>" for line in n["summary_lines"])

        out.append(
            f'<div class="box-card {kind_cls}" id="node-{escape(nid)}" data-node="{escape(nid)}" data-capa="{escape(n["capa"])}" '
            f'style="left: {x}px; top: {y}px; width: {w}px; height: {h}px;">\n'
            f'        <div class="macro-badge">{escape(n["code"])}</div>\n'
            f'        <div class="box-title">{escape(n["title"])}</div>\n'
            f'        <div class="box-subtitle">{escape(n["subtitle"])}</div>\n'
            f'        <span class="box-tag">{tag_str}</span>{gui_strip_html}\n'
            f'        <div class="box-content">\n'
            f'          {lines_html}\n'
            f'        </div>\n'
            f'      </div>'
        )
    return "\n\n      ".join(out)


def build_html_document(catalog):
    """Ensambla el archivo HTML5 definitivo autocontenido con todo el catálogo embebido."""
    mapped_edus = {e["codigo"] for e in catalog["educciones"]}
    mapped_ilas = {i["codigo"] for i in catalog["ilaciones"]}
    mapped_rnfs = {r["uid"] for r in catalog["rnfs"]}
    assert len(mapped_edus) == 27 and len(mapped_ilas) == 108 and len(mapped_rnfs) == 28

    app_data = {
        "nodes": NODES,
        "flows": FLOWS,
        "frontier": FRONTIER,
        "zones": ZONES,
        "catalog": catalog,
        "mermaid": {
            "m1": {"title": "1. Arquitectura Definitiva Integral (Zonas + EP + 5 Capas)", "code": MERMAID_01.strip()},
            "m5": {"title": "5. Mapa Entry Points (EP-01..06) & Ubicación de 28 GUIs", "code": MERMAID_05.strip()},
            "m2": {"title": "2. Contratos API REST / WSS / Hooks y Gateways", "code": MERMAID_02.strip()},
            "m3": {"title": "3. Matriz Completa RNF-0001..RNF-0027", "code": MERMAID_03.strip()},
            "m4": {"title": "4. Pizarra (RNF-0027) + Tuberías & Lotes (Plantilla 8)", "code": MERMAID_04.strip()},
        },
    }
    json_payload = json.dumps(app_data, ensure_ascii=False).replace("</", "<\\/")

    zones_html = render_zones()
    svg_flows_html = render_svg_flows()
    pills_html = render_flow_pills()
    cards_html = render_node_cards(catalog)

    fx, fy, fw, fh = FRONTIER["x"], FRONTIER["y"], FRONTIER["w"], FRONTIER["h"]

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Diagrama Definitivo de Bloques Funcionales Integral | NexoVitalis360</title>
  <style>
    /* =====================================================================
       PARADIGMA DE DISEÑO NEXOVITALIS360:
       100% Blanco & Negro Puro • Esquinas 100% Rectas (0px) • Alto Contraste
       ===================================================================== */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      border-radius: 0 !important;
    }}

    html, body {{
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background-color: #ffffff;
      color: #000000;
      font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
    }}

    /* LIENZO NAVEGABLE */
    .viewport {{
      position: absolute;
      inset: 0;
      overflow: hidden;
      cursor: grab;
      background-color: #ffffff;
      user-select: none;
      -webkit-user-select: none;
    }}
    .viewport:active {{
      cursor: grabbing;
    }}
    .canvas-world {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      will-change: transform;
      background-color: #ffffff;
    }}

    /* BARRA HUD SUPERIOR IZQUIERDA (BUSCADOR, FILTRO DE CAPAS, MERMAID, MATRIZ) */
    .hud-left {{
      position: fixed;
      top: 10px;
      left: 14px;
      z-index: 2100;
      display: flex;
      align-items: center;
      gap: 6px;
      background: #ffffff;
      border: 1.8px solid #000000;
      padding: 5px 10px;
      box-shadow: 2.5px 2.5px 0px #000000;
      font-size: 11px;
    }}

    .search-wrap {{
      position: relative;
      display: flex;
      align-items: center;
    }}
    .hud-input {{
      width: 205px;
      padding: 4px 8px;
      border: 1.5px solid #000000;
      font-family: "Courier New", monospace;
      font-size: 11px;
      font-weight: bold;
      color: #000000;
      background: #ffffff;
      outline: none;
    }}
    .hud-input:focus {{
      background: #fafafa;
      box-shadow: 2px 2px 0px #000000;
    }}
    .hud-select {{
      padding: 4px 6px;
      border: 1.5px solid #000000;
      background: #ffffff;
      color: #000000;
      font-family: Arial, sans-serif;
      font-size: 11px;
      font-weight: bold;
      cursor: pointer;
      outline: none;
      max-width: 170px;
    }}
    .search-dropdown {{
      display: none;
      position: absolute;
      top: 100%;
      left: 0;
      width: 460px;
      max-height: 410px;
      overflow-y: auto;
      background: #ffffff;
      border: 2px solid #000000;
      box-shadow: 4px 4px 0px #000000;
      z-index: 3500;
      margin-top: 4px;
    }}
    .search-dropdown.open {{
      display: block;
    }}
    .search-item {{
      padding: 7px 10px;
      border-bottom: 1px solid #d4d4d4;
      cursor: pointer;
      display: flex;
      flex-direction: column;
      gap: 2px;
      font-size: 11px;
    }}
    .search-item:hover {{
      background: #000000;
      color: #ffffff;
    }}
    .search-item .si-top {{
      display: flex;
      justify-content: space-between;
      font-weight: 800;
    }}
    .search-item .si-type {{
      font-family: "Courier New", monospace;
      font-size: 10px;
      padding: 1px 4px;
      border: 1px solid currentColor;
    }}
    .search-item .si-sub {{
      font-size: 10px;
      opacity: 0.82;
    }}

    /* BARRA HUD SUPERIOR DERECHA (ZOOM Y MODO SEMÁNTICO - ESTILO OFICIAL) */
    .hud-bar {{
      position: fixed;
      top: 10px;
      right: 14px;
      z-index: 2100;
      display: flex;
      align-items: center;
      gap: 6px;
      background: #ffffff;
      border: 1.8px solid #000000;
      padding: 5px 10px;
      font-size: 11px;
      box-shadow: 2.5px 2.5px 0px #000000;
    }}
    .hud-status-badge {{
      background: #000000;
      color: #ffffff;
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 0.4px;
      padding: 4px 7px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .btn-hud {{
      background: #ffffff;
      color: #000000;
      border: 1.5px solid #000000;
      padding: 4px 8px;
      font-family: inherit;
      font-size: 11px;
      font-weight: 800;
      cursor: pointer;
      white-space: nowrap;
      transition: background 0.1s ease, color 0.1s ease;
    }}
    .btn-hud:hover, .btn-hud.active {{
      background: #000000;
      color: #ffffff;
    }}
    .zoom-text {{
      font-weight: 800;
      min-width: 40px;
      text-align: center;
      font-family: "Courier New", monospace;
      font-size: 11.5px;
    }}

    @media (max-width: 1380px) {{
      .hud-left, .hud-bar {{ padding: 4px 7px; gap: 4px; font-size: 10px; }}
      .hud-left {{ left: 10px; }}
      .hud-bar {{ right: 10px; }}
      .hud-input {{ width: 162px; font-size: 10px; padding: 3px 6px; }}
      .hud-select {{ max-width: 142px; font-size: 10px; padding: 3px 4px; }}
      .btn-hud {{ padding: 3px 6px; font-size: 10px; }}
      .hud-status-badge {{ font-size: 9.5px; padding: 3px 5px; }}
      .zoom-text {{ min-width: 34px; font-size: 10.5px; }}
    }}
    @media (max-width: 1080px) {{
      .hud-bar {{ top: 46px; }}
    }}

    /* PIE INFORMATIVO AUDITORÍA CATÁLOGO */
    .bottom-hud {{
      position: fixed;
      bottom: 10px;
      left: 14px;
      z-index: 2050;
      background: #ffffff;
      border: 1.5px solid #000000;
      box-shadow: 2px 2px 0px #000000;
      padding: 4px 10px;
      font-size: 10.5px;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .bottom-hud:hover {{
      background: #000000;
      color: #ffffff;
    }}

    /* TÍTULO DENTRO DEL LIENZO */
    .canvas-header {{
      position: absolute;
      left: 35px;
      top: 8px;
      width: 4005px;
      height: 54px;
      border: 2px solid #000000;
      background: #fafafa;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 22px;
      z-index: 2;
      pointer-events: none;
    }}
    .canvas-header h1 {{
      font-size: 20px;
      font-weight: 900;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }}
    .canvas-header p {{
      font-size: 11.5px;
      font-weight: bold;
      color: #222222;
      font-family: "Courier New", monospace;
    }}

    /* ZONAS DE DESPLIEGUE Y FRONTERA DEL SISTEMA */
    .zone-box {{
      position: absolute;
      border: 1.6px dotted #444444;
      background: rgba(250, 250, 250, 0.45);
      pointer-events: none;
      z-index: 0;
    }}
    .zone-badge {{
      position: absolute;
      left: 10px;
      bottom: 6px;
      background: #ffffff;
      color: #000000;
      border: 1px solid #000000;
      padding: 1px 6px;
      font-size: 9px;
      font-weight: 900;
      letter-spacing: 0.3px;
    }}
    .system-frontier {{
      position: absolute;
      left: {fx}px;
      top: {fy}px;
      width: {fw}px;
      height: {fh}px;
      border: 2.5px dashed #000000;
      pointer-events: none;
      z-index: 1;
    }}
    .frontier-badge {{
      position: absolute;
      left: 16px;
      top: 6px;
      background: #000000;
      color: #ffffff;
      padding: 3px 10px;
      font-size: 10px;
      font-weight: 900;
      letter-spacing: 0.5px;
    }}

    /* CAPA SVG DE FLECHAS */
    .svg-layer {{
      position: absolute;
      top: 0;
      left: 0;
      width: {CANVAS_W}px;
      height: {CANVAS_H}px;
      pointer-events: none;
      z-index: 4;
    }}
    .flow-edge-group {{
      pointer-events: auto;
      cursor: pointer;
    }}
    .flow-edge-group:hover .flow-line,
    .flow-edge-group.highlighted .flow-line {{
      stroke-width: 4.8px !important;
      filter: drop-shadow(1px 1px 0px #000000);
    }}
    .flow-edge-group.dimmed {{
      opacity: 0.14;
    }}

    /* TARJETAS DE MÓDULO (CON MULTI-LEVEL SEMANTIC ZOOM) */
    .box-card {{
      position: absolute;
      border: 1.8px solid #000000;
      background: #ffffff;
      padding: 8px 11px;
      display: flex;
      flex-direction: column;
      cursor: pointer;
      z-index: 6;
      overflow: hidden;
      transition: box-shadow 0.12s ease, opacity 0.15s ease, background 0.12s ease;
    }}
    .box-card:hover {{
      background: #fafafa;
      box-shadow: 3px 3px 0px #000000;
    }}
    .box-card.card-hub {{
      border: 2.8px solid #000000;
      background: #f5f5f5;
      box-shadow: 3px 3px 0px #000000;
    }}
    .box-card.card-entry {{
      border: 2.2px dashed #000000;
      border-left: 7px solid #000000;
      background: #ffffff;
      box-shadow: 3px 3px 0px #000000;
    }}
    .box-card.card-ext {{
      border: 2px solid #000000;
      background: #ffffff;
    }}
    .box-card.card-dashed {{
      border: 2px dashed #000000;
      background: #fafafa;
    }}
    .box-card.focused {{
      background: #ffffff !important;
      border: 3.5px solid #000000 !important;
      box-shadow: 6px 6px 0px #000000 !important;
      z-index: 50 !important;
    }}
    .box-card.search-hit {{
      outline: 3px solid #000000;
      outline-offset: 4px;
    }}
    .box-card.dimmed {{
      opacity: 0.18 !important;
    }}

    .macro-badge {{
      display: inline-block;
      align-self: flex-start;
      background: #000000;
      color: #ffffff;
      font-family: "Courier New", monospace;
      font-size: 9.5px;
      font-weight: 900;
      padding: 1px 6px;
      margin-bottom: 3px;
      letter-spacing: 0.4px;
    }}
    .box-title {{
      font-weight: 900;
      color: #000000;
      line-height: 1.18;
      font-size: 13px;
    }}
    .box-subtitle {{
      font-size: 9.2px;
      font-weight: 800;
      color: #333333;
      text-transform: uppercase;
      letter-spacing: 0.2px;
      margin-top: 2px;
      margin-bottom: 4px;
    }}
    .box-tag {{
      display: inline-block;
      align-self: flex-start;
      font-family: "Courier New", monospace;
      font-size: 8.8px;
      font-weight: 800;
      background: #000000;
      color: #ffffff;
      padding: 2px 6px;
      margin-bottom: 3px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 100%;
    }}
    .box-gui-strip {{
      font-family: "Courier New", monospace;
      font-size: 8.5px;
      font-weight: 900;
      background: #efefef;
      color: #000000;
      border: 1.2px solid #000000;
      padding: 2px 5px;
      margin-bottom: 3px;
      line-height: 1.18;
    }}
    .box-content {{
      font-size: 9.0px;
      line-height: 1.20;
      color: #111111;
      border-top: 1px solid #000000;
      padding-top: 3px;
      display: flex;
      flex-direction: column;
      gap: 2px;
    }}
    .box-content p {{ margin: 0; }}

    /* MODO 1: TÍTULOS (MACRO VIEW - SIN RUIDO VISUAL) */
    body.mode-titles-only .box-card {{
      justify-content: center !important;
      align-items: center !important;
      text-align: center !important;
      padding: 12px 16px !important;
    }}
    body.mode-titles-only .box-card .macro-badge {{
      align-self: center;
      font-size: 11px;
      padding: 2px 8px;
      margin-bottom: 6px;
    }}
    body.mode-titles-only .box-card .box-title {{
      font-size: 19px !important;
      font-weight: 900 !important;
      text-transform: uppercase !important;
      letter-spacing: 0.4px !important;
      line-height: 1.2 !important;
    }}
    body.mode-titles-only .box-card.card-hub .box-title {{
      font-size: 23px !important;
    }}
    body.mode-titles-only .box-card .box-subtitle,
    body.mode-titles-only .box-card .box-tag,
    body.mode-titles-only .box-card .box-gui-strip,
    body.mode-titles-only .box-card .box-content {{
      display: none !important;
    }}

    /* MODO 2: RESUMEN INTERMEDIO */
    body.mode-summary .box-card .box-title {{
      font-size: 14px;
    }}
    body.mode-summary .box-card.card-hub .box-title {{
      font-size: 16px;
    }}
    body.mode-summary .box-card .box-content {{
      display: none;
    }}

    /* MODO 3: DETALLE COMPLETO (O CARD ENFOCADA) */
    body.mode-details-visible .box-card .box-content,
    .box-card.focused .box-content {{
      display: flex !important;
    }}
    body.mode-titles-only .box-card.focused {{
      justify-content: flex-start !important;
      align-items: stretch !important;
      text-align: left !important;
      padding: 10px 12px !important;
    }}
    body.mode-titles-only .box-card.focused .macro-badge {{
      align-self: flex-start;
      margin-bottom: 4px;
    }}
    body.mode-titles-only .box-card.focused .box-title {{
      font-size: 13.5px !important;
      text-transform: none !important;
    }}
    body.mode-titles-only .box-card.focused .box-subtitle,
    body.mode-titles-only .box-card.focused .box-gui-strip {{
      display: block !important;
    }}
    body.mode-titles-only .box-card.focused .box-tag {{
      display: inline-block !important;
    }}

    /* PÍLDORAS DE FLUJOS (PROGRESIVAS Y ACOTADAS AL ANCHO DE CORREDOR) */
    .flow-pill {{
      position: absolute;
      background: #ffffff;
      border: 1.6px solid #000000;
      padding: 2px 6px;
      font-size: 10.5px;
      font-weight: 800;
      color: #000000;
      white-space: nowrap;
      transform: translate(-50%, -50%);
      z-index: 15;
      cursor: pointer;
      box-shadow: 2px 2px 0px #000000;
      line-height: 1.2;
      text-align: center;
      transition: background 0.12s ease, color 0.12s ease, opacity 0.15s ease;
    }}
    .flow-pill:hover, .flow-pill.highlighted {{
      background: #000000;
      color: #ffffff;
      z-index: 120;
      box-shadow: 3px 3px 0px rgba(0,0,0,0.45);
    }}
    .flow-pill.dimmed {{
      opacity: 0.15;
    }}
    .flow-pill .pill-detail {{
      font-weight: normal;
      font-size: 9px;
      display: none;
    }}
    body.mode-details-visible .flow-pill,
    .flow-pill:hover,
    .flow-pill.highlighted {{
      max-width: 185px;
      white-space: normal;
      padding: 3px 6px;
    }}
    body.mode-details-visible .flow-pill .pill-detail,
    .flow-pill:hover .pill-detail,
    .flow-pill.highlighted .pill-detail {{
      display: block;
    }}

    /* PANEL INSPECTOR DERECHO (CATALOGO 100% DETALLADO) */
    .inspector-drawer {{
      position: fixed;
      top: 56px;
      right: 14px;
      bottom: 14px;
      width: 470px;
      max-width: calc(100vw - 28px);
      background: #ffffff;
      border: 2.2px solid #000000;
      box-shadow: 5px 5px 0px #000000;
      z-index: 2200;
      display: none;
      flex-direction: column;
      overflow: hidden;
    }}
    .inspector-drawer.open {{
      display: flex;
    }}
    .insp-header {{
      background: #000000;
      color: #ffffff;
      padding: 10px 12px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .insp-header-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
    }}
    .insp-code-badge {{
      background: #ffffff;
      color: #000000;
      font-family: "Courier New", monospace;
      font-weight: 900;
      font-size: 11px;
      padding: 2px 7px;
    }}
    .insp-nav-btns {{
      display: flex;
      gap: 4px;
    }}
    .btn-insp {{
      background: #000000;
      color: #ffffff;
      border: 1.2px solid #ffffff;
      padding: 2px 7px;
      font-size: 10.5px;
      font-weight: bold;
      cursor: pointer;
    }}
    .btn-insp:hover {{
      background: #ffffff;
      color: #000000;
    }}
    .insp-title {{
      font-size: 13.5px;
      font-weight: 900;
      line-height: 1.25;
    }}
    .insp-sub {{
      font-size: 10.5px;
      color: #cccccc;
      text-transform: uppercase;
    }}
    .insp-tabs {{
      display: flex;
      border-bottom: 2px solid #000000;
      background: #f4f4f4;
    }}
    .insp-tab {{
      flex: 1;
      padding: 7px 4px;
      font-size: 10.5px;
      font-weight: 800;
      text-align: center;
      cursor: pointer;
      border: none;
      border-right: 1px solid #000000;
      background: #f4f4f4;
      color: #000000;
      font-family: inherit;
    }}
    .insp-tab:last-child {{ border-right: none; }}
    .insp-tab.active {{
      background: #000000;
      color: #ffffff;
    }}
    .insp-body {{
      flex: 1;
      overflow-y: auto;
      padding: 12px;
      font-size: 11.5px;
      line-height: 1.4;
      background: #ffffff;
      user-select: text;
    }}
    .insp-section-title {{
      font-size: 11px;
      font-weight: 900;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      background: #f4f4f4;
      border-left: 4px solid #000000;
      padding: 4px 8px;
      margin: 10px 0 6px 0;
    }}
    .insp-section-title:first-child {{ margin-top: 0; }}

    .insp-card {{
      border: 1.5px solid #000000;
      padding: 8px 10px;
      margin-bottom: 8px;
      background: #ffffff;
    }}
    .insp-card.highlight-item {{
      border: 2.5px solid #000000;
      box-shadow: 3px 3px 0px #000000;
      background: #fafafa;
    }}
    .insp-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 6px;
      font-weight: 800;
      margin-bottom: 4px;
    }}
    .chip {{
      display: inline-block;
      font-family: "Courier New", monospace;
      font-size: 10px;
      font-weight: 800;
      padding: 1px 5px;
      border: 1px solid #000000;
      background: #ffffff;
      color: #000000;
    }}
    .chip-inv {{
      background: #000000;
      color: #ffffff;
    }}
    .ila-details {{
      border-top: 1px dashed #999999;
      margin-top: 6px;
      padding-top: 5px;
    }}
    .ila-details summary {{
      cursor: pointer;
      font-weight: 800;
      font-size: 11px;
      padding: 2px 0;
    }}
    .ila-details summary:hover {{
      text-decoration: underline;
    }}
    .ila-body {{
      padding: 6px 8px;
      margin-top: 4px;
      background: #fafafa;
      border-left: 2.5px solid #000000;
      font-size: 10.5px;
      white-space: pre-line;
    }}
    .flow-jump-btn {{
      display: inline-block;
      margin: 2px 4px 2px 0;
      padding: 2px 6px;
      border: 1.2px solid #000000;
      background: #ffffff;
      font-size: 10.5px;
      font-weight: 800;
      cursor: pointer;
    }}
    .flow-jump-btn:hover {{
      background: #000000;
      color: #ffffff;
    }}

    /* MODALES FULLSCREEN (MATRIZ GLOBAL & VISOR MERMAID) */
    .full-modal {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(0,0,0,0.75);
      z-index: 3000;
      align-items: center;
      justify-content: center;
      padding: 18px;
    }}
    .full-modal.open {{
      display: flex;
    }}
    .full-modal-box {{
      width: 96vw;
      height: 92vh;
      background: #ffffff;
      border: 2.5px solid #000000;
      box-shadow: 7px 7px 0px #000000;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}
    .full-modal-header {{
      background: #000000;
      color: #ffffff;
      padding: 9px 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      font-weight: 900;
      font-size: 12.5px;
      text-transform: uppercase;
    }}
    .modal-subtabs {{
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      border-bottom: 2px solid #000000;
      background: #f4f4f4;
      flex-wrap: wrap;
    }}
    .full-modal-body {{
      flex: 1;
      overflow: auto;
      padding: 14px;
      background: #ffffff;
      user-select: text;
    }}

    /* TABLA DE TRAZABILIDAD 100% */
    table.audit-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
    }}
    table.audit-table th, table.audit-table td {{
      border: 1.2px solid #000000;
      padding: 6px 8px;
      text-align: left;
      vertical-align: top;
    }}
    table.audit-table th {{
      background: #000000;
      color: #ffffff;
      font-weight: 800;
      position: sticky;
      top: 0;
      z-index: 2;
    }}
    table.audit-table tr:nth-child(even) {{
      background: #fafafa;
    }}

    /* CONTENEDOR MERMAID INTERACTIVO */
    .mermaid-stage {{
      width: 100%;
      height: calc(100% - 10px);
      overflow: auto;
      border: 1.5px solid #000000;
      background: #ffffff;
      padding: 16px;
      text-align: center;
    }}
    .mermaid-code-box {{
      width: 100%;
      height: calc(100% - 10px);
      font-family: "Courier New", monospace;
      font-size: 11.5px;
      padding: 12px;
      border: 1.5px solid #000000;
      background: #fafafa;
      color: #000000;
      resize: none;
    }}
  </style>
</head>
<body class="mode-titles-only">

  <!-- HUD SUPERIOR IZQUIERDO: BÚSQUEDA, FILTRO POR CAPAS Y MODALES -->
  <div class="hud-left">
    <div class="search-wrap">
      <input type="text" class="hud-input" id="searchInput" placeholder="Buscar RNF, EDU, ILA, API, TB_..." autocomplete="off" />
      <div class="search-dropdown" id="searchDropdown"></div>
    </div>
    <select class="hud-select" id="capaFilter" title="Filtrar vista por capa arquitectónica">
      <option value="ALL">Todas las Capas (30 Nodos)</option>
      <option value="Capa 1: Presentación y Actores">Capa 1: Actores (EXT-A1..A4)</option>
      <option value="Entry Points y Canales">Ingreso: Entry Points (EP-01..06)</option>
      <option value="Capa 2: Seguridad y API Gateway">Capa 2: DMZ Gateway &amp; JWT (B0)</option>
      <option value="Capa 3: Lógica Clínica y Subsistemas">Capa 3: Subsistemas (B1–B10)</option>
      <option value="Capa 4: Persistencia, Storage y Pizarra">Capa 4: BD, MinIO &amp; Pizarra (B11–B12)</option>
      <option value="Capa 5: APIs Externas">Capa 5: APIs Externas</option>
      <option value="Transversal">Transversal: HW, Stack &amp; Catálogo</option>
    </select>
    <button class="btn-hud" id="btnOpenMatrix" title="Explorar EP, 27 EDU, 108 ILA, 104 ESP, 113 Pruebas, 28 RNF y 28 GUI [C]">Matriz Total [C]</button>
    <button class="btn-hud" id="btnOpenMermaid" title="Ver y copiar 5 diagramas Mermaid oficiales [M]">Mermaid [M]</button>
  </div>

  <!-- HUD SUPERIOR DERECHO: CONTROLES DE ZOOM Y MODO SEMÁNTICO -->
  <header class="hud-bar">
    <span class="hud-status-badge" id="statusBadge">MODO TÍTULOS</span>
    <button class="btn-hud" id="btnZoomOut">− Zoom</button>
    <span class="zoom-text" id="zoomText">100%</span>
    <button class="btn-hud" id="btnZoomIn">+ Zoom</button>
    <button class="btn-hud" id="btnFit" title="Tecla 0">Ajustar</button>
    <button class="btn-hud" id="btnReset">100%</button>
    <button class="btn-hud" id="btnToggleMode">Modo: AUTO</button>
    <button class="btn-hud" id="btnToggleInspector" title="Tecla I">Inspector [I]</button>
  </header>

  <!-- AUDITORÍA INFERIOR -->
  <div class="bottom-hud" id="bottomAuditBadge" title="Clic para abrir auditoría completa del catálogo">
    ✔ COBERTURA 100%: 6 ENTRY POINTS &bull; 27/27 EDU &bull; 108 ILA &bull; 104 ESP &bull; 113 PRUEBAS &bull; 28 RNF &bull; 28 GUI/140 MDL &bull; 39 FLUJOS
  </div>

  <!-- PANEL INSPECTOR DERECHO -->
  <aside class="inspector-drawer" id="inspectorDrawer">
    <div class="insp-header">
      <div class="insp-header-top">
        <span class="insp-code-badge" id="inspCode">B4</span>
        <div class="insp-nav-btns">
          <button class="btn-insp" id="btnPrevNode" title="Módulo anterior">◀ Ant</button>
          <button class="btn-insp" id="btnNextNode" title="Siguiente módulo">Sig ▶</button>
          <button class="btn-insp" id="btnCenterNode" title="Centrar en el lienzo">Centrar</button>
          <button class="btn-insp" id="btnCloseInsp" title="Cerrar (Esc)">✕</button>
        </div>
      </div>
      <div class="insp-title" id="inspTitle">Seleccione un módulo o flujo</div>
      <div class="insp-sub" id="inspSub">Arquitectura Integral NexoVitalis360</div>
    </div>
    <div class="insp-tabs" id="inspTabs">
      <button class="insp-tab active" data-tab="resumen">Resumen &amp; APIs</button>
      <button class="insp-tab" data-tab="edus">EDUs &amp; ILAs</button>
      <button class="insp-tab" data-tab="rnfs">RNFs</button>
      <button class="insp-tab" data-tab="datos">GUIs &amp; Datos</button>
    </div>
    <div class="insp-body" id="inspBody"></div>
  </aside>

  <!-- MODAL MATRIZ TOTAL DEL CATÁLOGO -->
  <div class="full-modal" id="matrixModal">
    <div class="full-modal-box">
      <div class="full-modal-header">
        <span>Matriz de Trazabilidad Total del Catálogo — NexoVitalis360 (Auditoría 100%)</span>
        <button class="btn-hud" id="btnCloseMatrix">✕ Cerrar</button>
      </div>
      <div class="modal-subtabs">
        <button class="btn-hud active" data-mtab="edus">27 Educciones (EDU)</button>
        <button class="btn-hud" data-mtab="ilaciones">108 Ilaciones (ILA) + Riesgos</button>
        <button class="btn-hud" data-mtab="esps">104 ESP + 113 Pruebas</button>
        <button class="btn-hud" data-mtab="rnfs">28 Entradas RNF (01..27)</button>
        <button class="btn-hud" data-mtab="apis">APIs REST / WSS / Externas</button>
        <button class="btn-hud" data-mtab="guis">6 Entry Points &amp; 28 GUIs (140 MDL)</button>
        <button class="btn-hud" data-mtab="tables">27 Tablas TB_* / Storage</button>
        <input type="text" class="hud-input" id="matrixFilterInput" placeholder="Filtrar tabla actual..." style="margin-left:auto; width:200px;" />
      </div>
      <div class="full-modal-body" id="matrixBody"></div>
    </div>
  </div>

  <!-- MODAL VISOR MERMAID -->
  <div class="full-modal" id="mermaidModal">
    <div class="full-modal-box">
      <div class="full-modal-header">
        <span>Suite Mermaid Oficial — Diagrama Definitivo de Bloques Funcionales (5 Vistas)</span>
        <button class="btn-hud" id="btnCloseMermaid">✕ Cerrar</button>
      </div>
      <div class="modal-subtabs">
        <button class="btn-hud active" data-mmd="m1">1. Integral (Zonas + EP)</button>
        <button class="btn-hud" data-mmd="m5">5. Entry Points &amp; GUIs</button>
        <button class="btn-hud" data-mmd="m2">2. APIs REST / WSS / Hooks</button>
        <button class="btn-hud" data-mmd="m3">3. Matriz RNF 01..27</button>
        <button class="btn-hud" data-mmd="m4">4. Pizarra + Tuberías/Lotes</button>
        <button class="btn-hud" id="btnMmdZoomOut" style="margin-left:auto;">− Zoom SVG</button>
        <button class="btn-hud" id="btnMmdFit">Ajustar</button>
        <button class="btn-hud" id="btnMmdZoomIn">+ Zoom SVG</button>
        <button class="btn-hud" id="btnMmdToggleCode">Ver Código .mmd</button>
        <button class="btn-hud" id="btnMmdCopy">Copiar Código</button>
      </div>
      <div class="full-modal-body" id="mermaidModalBody">
        <div class="mermaid-stage" id="mermaidStage">Cargando motor Mermaid...</div>
        <textarea class="mermaid-code-box" id="mermaidCodeBox" style="display:none;" readonly></textarea>
      </div>
    </div>
  </div>

  <!-- LIENZO INTERACTIVO -->
  <div class="viewport" id="viewport">
    <div class="canvas-world" id="canvasWorld" style="width: {CANVAS_W}px; height: {CANVAS_H}px;">

      <div class="canvas-header">
        <div>
          <h1>Diagrama Definitivo de Bloques Funcionales Integral — NexoVitalis360 (v02.10)</h1>
          <p>Proyección Biunívoca Total: Entry Points (EP-01..06) &bull; 27 EDU &bull; 108 ILA &bull; 104 ESP &bull; 113 Pruebas &bull; 28 RNF &bull; 28 GUI/140 MDL &bull; Tuberías/Lotes</p>
        </div>
        <div style="font-size:11px; font-weight:800; border:1.5px solid #000; padding:4px 10px; background:#fff;">
          ORG-0001..0003 &bull; RuwayLabs Perú / UNSA EPIS
        </div>
      </div>

      {zones_html}

      <div class="system-frontier">
        <div class="frontier-badge">FRONTERA DEL SISTEMA: NEXOVITALIS360 (ZONA 2 DMZ B0 + ZONA 3 APP VPC B1–B10 + ZONA 4 DATOS B11–B12)</div>
      </div>

      <svg class="svg-layer" width="{CANVAS_W}" height="{CANVAS_H}">
        <defs>
          <marker id="arrow" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="8.5" markerHeight="8.5" orient="auto-start-reverse">
            <path d="M 0 1.2 L 9 5 L 0 8.8 z" fill="#000000" />
          </marker>
        </defs>
        {svg_flows_html}
      </svg>

      {pills_html}

      {cards_html}

    </div>
  </div>

  <!-- CARGA LOCAL DE MERMAID CON FALLBACK DESDE SUBDIRECTORIOS -->
  <script>
    (function loadMermaidScript() {{
      const s1 = document.createElement('script');
      s1.src = 'vendor/mermaid.min.js';
      s1.onerror = function() {{
        const s2 = document.createElement('script');
        s2.src = '../VISOR_HTML_ARQUITECTURA_v01.00/vendor/mermaid.min.js';
        document.head.appendChild(s2);
      }};
      document.head.appendChild(s1);
    }})();
  </script>

  <script>
    const APP_DATA = {json_payload};
    const CANVAS_W = {CANVAS_W};
    const CANVAS_H = {CANVAS_H};

    // Índices rápidos
    const NODE_MAP = Object.fromEntries(APP_DATA.nodes.map(n => [n.id, n]));
    const FLOW_MAP = Object.fromEntries(APP_DATA.flows.map(f => [f.id, f]));

    function getNodeData(nid) {{
      const n = NODE_MAP[nid];
      const edus = APP_DATA.catalog.educciones.filter(e => e.bloque === nid);
      const ilas = APP_DATA.catalog.ilaciones.filter(i => i.bloque === nid);
      const rnfs = APP_DATA.catalog.rnfs.filter(r => r.nodos.includes(nid));
      const guis = APP_DATA.catalog.guis.filter(g => g.bloque === nid);
      const inFlows = APP_DATA.flows.filter(f => f.dst === nid);
      const outFlows = APP_DATA.flows.filter(f => f.src === nid);
      return {{ node: n, edus, ilas, rnfs, guis, inFlows, outFlows }};
    }}

    // =========================================================================
    // MOTOR DE PAN, ZOOM Y SEMANTIC ZOOM DE 3 NIVELES
    // =========================================================================
    const viewport = document.getElementById('viewport');
    const canvasWorld = document.getElementById('canvasWorld');
    const zoomText = document.getElementById('zoomText');
    const statusBadge = document.getElementById('statusBadge');
    const btnToggleMode = document.getElementById('btnToggleMode');

    let scale = 1.0;
    let initialFitScale = 0.4;
    let panX = 0;
    let panY = 0;
    let isDragging = false;
    let startX = 0;
    let startY = 0;
    // 'auto' -> 'details' -> 'titles'
    let userMode = 'auto';

    function escHtml(str) {{
      if (str === null || str === undefined) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
    }}

    function applyTransform() {{
      canvasWorld.style.transform = `matrix(${{scale}}, 0, 0, ${{scale}}, ${{panX}}, ${{panY}})`;
      zoomText.textContent = `${{Math.round(scale * 100)}}%`;
    }}

    function updateSemanticZoom() {{
      document.body.classList.remove('mode-titles-only', 'mode-summary', 'mode-details-visible');
      if (userMode === 'details') {{
        document.body.classList.add('mode-details-visible');
        statusBadge.textContent = 'DETALLES (FIJO)';
        return;
      }}
      if (userMode === 'titles') {{
        document.body.classList.add('mode-titles-only');
        statusBadge.textContent = 'SOLO TÍTULOS';
        return;
      }}
      const ratio = scale / Math.max(0.1, initialFitScale);
      if (ratio >= 1.72) {{
        document.body.classList.add('mode-details-visible');
        statusBadge.textContent = 'MODO DETALLE';
      }} else if (ratio >= 1.18) {{
        document.body.classList.add('mode-summary');
        statusBadge.textContent = 'MODO RESUMEN';
      }} else {{
        document.body.classList.add('mode-titles-only');
        statusBadge.textContent = 'MODO TÍTULOS';
      }}
    }}

    function fitToScreen() {{
      const inspOpen = document.getElementById('inspectorDrawer').classList.contains('open');
      const availW = window.innerWidth - (inspOpen ? 500 : 40);
      const availH = window.innerHeight - 104;
      const s = Math.min(availW / CANVAS_W, availH / CANVAS_H);
      scale = Math.max(0.22, Math.min(s, 1.0));
      initialFitScale = scale;
      panX = (availW - CANVAS_W * scale) / 2 + 18;
      panY = 58 + Math.max(4, (availH - CANVAS_H * scale) / 2);
      applyTransform();
      updateSemanticZoom();
    }}

    function zoomAtPoint(factor, clientX, clientY) {{
      const prev = scale;
      const next = Math.min(Math.max(0.20, scale * factor), 2.8);
      if (next === prev) return;
      const dx = clientX - panX;
      const dy = clientY - panY;
      panX -= dx * (next / prev - 1);
      panY -= dy * (next / prev - 1);
      scale = next;
      applyTransform();
      updateSemanticZoom();
    }}

    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('.hud-bar, .hud-left, .inspector-drawer, .bottom-hud')) return;
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }});
    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      applyTransform();
    }});
    window.addEventListener('mouseup', () => {{ isDragging = false; }});

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const factor = e.deltaY < 0 ? 1.12 : 0.89;
      zoomAtPoint(factor, e.clientX, e.clientY);
    }}, {{ passive: false }});

    document.getElementById('btnZoomIn').onclick = () => zoomAtPoint(1.22, window.innerWidth / 2, window.innerHeight / 2);
    document.getElementById('btnZoomOut').onclick = () => zoomAtPoint(0.82, window.innerWidth / 2, window.innerHeight / 2);
    document.getElementById('btnFit').onclick = fitToScreen;
    document.getElementById('btnReset').onclick = () => {{
      scale = 0.85;
      panX = 40;
      panY = 64;
      applyTransform();
      updateSemanticZoom();
    }};
    btnToggleMode.onclick = () => {{
      if (userMode === 'auto') {{
        userMode = 'details';
        btnToggleMode.textContent = 'Modo: SIEMPRE DETALLES';
        btnToggleMode.classList.add('active');
      }} else if (userMode === 'details') {{
        userMode = 'titles';
        btnToggleMode.textContent = 'Modo: SOLO TÍTULOS';
      }} else {{
        userMode = 'auto';
        btnToggleMode.textContent = 'Modo: AUTO';
        btnToggleMode.classList.remove('active');
      }}
      updateSemanticZoom();
    }};

    // =========================================================================
    // INSPECTOR LATERAL INTERACTIVO
    // =========================================================================
    const drawer = document.getElementById('inspectorDrawer');
    const inspBody = document.getElementById('inspBody');
    let currentInspKind = 'node'; // 'node' | 'flow'
    let currentInspId = 'B4';
    let currentTab = 'resumen';
    let highlightCode = '';

    function focusNodeOnCanvas(nid, openDrawer = true, tab = null, searchTerm = '') {{
      const n = NODE_MAP[nid];
      if (!n) return;
      currentInspKind = 'node';
      currentInspId = nid;
      if (tab) currentTab = tab;
      highlightCode = searchTerm;

      document.querySelectorAll('.box-card').forEach(c => c.classList.remove('focused'));
      document.querySelectorAll('.flow-edge-group, .flow-pill').forEach(el => el.classList.remove('highlighted'));
      const card = document.getElementById('node-' + nid);
      if (card) card.classList.add('focused');

      // Resaltar flujos conectados
      APP_DATA.flows.forEach(f => {{
        if (f.src === nid || f.dst === nid) {{
          document.querySelectorAll(`[data-flow="${{f.id}}"]`).forEach(el => el.classList.add('highlighted'));
        }}
      }});

      if (openDrawer) {{
        drawer.classList.add('open');
        document.getElementById('btnToggleInspector').classList.add('active');
        renderInspector();
      }}

      const [x, y, w, h] = n.rect;
      const drawerW = drawer.classList.contains('open') ? 490 : 0;
      const availW = window.innerWidth - drawerW;
      const availH = window.innerHeight - 80;
      scale = Math.max(scale, 0.72);
      scale = Math.min(scale, 1.15);
      panX = (availW / 2) - (x + w / 2) * scale;
      panY = 56 + (availH / 2) - (y + h / 2) * scale;
      applyTransform();
      updateSemanticZoom();
    }}

    function focusFlowOnCanvas(fid) {{
      const f = FLOW_MAP[fid];
      if (!f) return;
      currentInspKind = 'flow';
      currentInspId = fid;
      highlightCode = '';

      document.querySelectorAll('.box-card').forEach(c => c.classList.remove('focused'));
      document.querySelectorAll('.flow-edge-group, .flow-pill').forEach(el => el.classList.remove('highlighted'));
      document.querySelectorAll(`[data-flow="${{fid}}"]`).forEach(el => el.classList.add('highlighted'));

      drawer.classList.add('open');
      document.getElementById('btnToggleInspector').classList.add('active');
      renderInspector();

      const [px, py] = f.pill;
      const availW = window.innerWidth - 490;
      const availH = window.innerHeight - 80;
      scale = Math.max(scale, 0.78);
      panX = (availW / 2) - px * scale;
      panY = 56 + (availH / 2) - py * scale;
      applyTransform();
      updateSemanticZoom();
    }}

    function renderInspector() {{
      const tabsEl = document.getElementById('inspTabs');
      if (currentInspKind === 'flow') {{
        tabsEl.style.display = 'none';
        const f = FLOW_MAP[currentInspId];
        document.getElementById('inspCode').textContent = f.id;
        document.getElementById('inspTitle').textContent = f.core;
        document.getElementById('inspSub').textContent = `${{f.src}} → ${{f.dst}} • Flujo ${{f.kind === 'async' ? 'Asíncrono' : 'Síncrono'}}`;

        const srcNode = NODE_MAP[f.src];
        const dstNode = NODE_MAP[f.dst];
        const rnfs = APP_DATA.catalog.rnfs.filter(r => f.rnfs.includes(r.codigo));
        const edus = APP_DATA.catalog.educciones.filter(e => f.edus.includes(e.codigo));

        inspBody.innerHTML = `
          <div class="insp-section-title">Descripción del Flujo y Contrato</div>
          <div class="insp-card">
            <p><strong>Detalle:</strong> ${{escHtml(f.detail)}}</p>
            <p style="margin-top:4px;"><strong>Contrato / API:</strong> <code>${{escHtml(f.api)}}</code></p>
            <div style="margin-top:8px;">
              <button class="flow-jump-btn" onclick="focusNodeOnCanvas('${{f.src}}')">Origen: ${{escHtml(srcNode ? srcNode.code : f.src)}}</button>
              <button class="flow-jump-btn" onclick="focusNodeOnCanvas('${{f.dst}}')">Destino: ${{escHtml(dstNode ? dstNode.code : f.dst)}}</button>
            </div>
          </div>
          <div class="insp-section-title">Educciones Asociadas (${{edus.length}})</div>
          ${{edus.map(e => `
            <div class="insp-card">
              <div class="insp-card-head"><span>${{escHtml(e.codigo)}} — ${{escHtml(e.nombre)}}</span><span class="chip">${{escHtml(e.importancia)}}</span></div>
              <p>${{escHtml(e.descripcion)}}</p>
            </div>
          `).join('') || '<div class="insp-card">Flujo transversal de infraestructura / seguridad aplicable a todo el sistema.</div>'}}
          <div class="insp-section-title">Requisitos No Funcionales (${{rnfs.length}})</div>
          ${{rnfs.map(r => `
            <div class="insp-card">
              <div class="insp-card-head"><span>${{escHtml(r.display_code)}} — ${{escHtml(r.nombre)}}</span><span class="chip">${{escHtml(r.atributo)}}</span></div>
              <p>${{escHtml(r.descripcion)}}</p>
            </div>
          `).join('')}}
        `;
        return;
      }}

      tabsEl.style.display = 'flex';
      document.querySelectorAll('.insp-tab').forEach(t => {{
        t.classList.toggle('active', t.dataset.tab === currentTab);
      }});

      const info = getNodeData(currentInspId);
      const n = info.node;
      document.getElementById('inspCode').textContent = n.code;
      document.getElementById('inspTitle').textContent = n.title;
      document.getElementById('inspSub').textContent = `${{n.capa}} • ${{n.subtitle}}`;

      const hl = (code) => (highlightCode && code.toLowerCase().includes(highlightCode.toLowerCase())) ? 'highlight-item' : '';

      if (currentTab === 'resumen') {{
        inspBody.innerHTML = `
          <div class="insp-section-title">Responsabilidades del Módulo</div>
          <div class="insp-card">
            ${{n.summary_lines.map(l => `<p style="margin-bottom:4px;">${{l}}</p>`).join('')}}
          </div>
          <div class="insp-section-title">Contratos API / Endpoints / Transporte (${{n.apis.length}})</div>
          ${{n.apis.map(a => `
            <div class="insp-card ${{hl(a.endpoint)}}">
              <div class="insp-card-head">
                <span class="chip chip-inv">${{escHtml(a.method)}}</span>
                <span class="chip">${{escHtml(a.sla)}}</span>
              </div>
              <p style="font-family:'Courier New',monospace;font-weight:bold;word-break:break-all;margin-bottom:4px;">${{escHtml(a.endpoint)}}</p>
              <p><strong>Seguridad:</strong> ${{escHtml(a.auth)}}</p>
              <p>${{escHtml(a.purpose)}}</p>
            </div>
          `).join('') || '<div class="insp-card">Componente normativo / transversal de referencia. Ver pestaña de RNFs.</div>'}}
          <div class="insp-section-title">Flujos Entrantes (${{info.inFlows.length}}) &amp; Salientes (${{info.outFlows.length}})</div>
          <div class="insp-card">
            <p style="margin-bottom:4px;"><strong>Entradas:</strong></p>
            ${{info.inFlows.map(f => `<button class="flow-jump-btn" onclick="focusFlowOnCanvas('${{f.id}}')">${{escHtml(f.core)}} ← ${{escHtml(f.src)}}</button>`).join('') || '<span>Ninguna directa</span>'}}
            <p style="margin:8px 0 4px 0;"><strong>Salidas:</strong></p>
            ${{info.outFlows.map(f => `<button class="flow-jump-btn" onclick="focusFlowOnCanvas('${{f.id}}')">${{escHtml(f.core)}} → ${{escHtml(f.dst)}}</button>`).join('') || '<span>Ninguna directa</span>'}}
          </div>
        `;
      }} else if (currentTab === 'edus') {{
        const ctxNote = (nid => {{
          if (nid === 'CTX-CAT') {{
            return `<div class="insp-section-title">Organizaciones (${{APP_DATA.catalog.organizaciones.length}}) y Actores (${{APP_DATA.catalog.actores_catalogo.length}})</div>
            <div class="insp-card">
              ${{APP_DATA.catalog.organizaciones.map(o => `<p><b>${{escHtml(o.codigo)}}:</b> ${{escHtml(o.nombre)}}</p>`).join('')}}
              <hr style="margin:6px 0;border:none;border-top:1px solid #000;" />
              ${{APP_DATA.catalog.actores_catalogo.map(a => `<p><b>${{escHtml(a.codigo)}}:</b> ${{escHtml(a.rol)}} (${{escHtml(a.tipo)}})</p>`).join('')}}
            </div>`;
          }}
          return '';
        }})(n.id);

        inspBody.innerHTML = ctxNote + `
          <div class="insp-section-title">Educciones (${{info.edus.length}}) &bull; Ilaciones / ESP (${{info.ilas.length}}) &bull; Pruebas T-*</div>
          ${{info.edus.map(e => {{
            const eIlas = info.ilas.filter(i => i.edu === e.codigo);
            return `
              <div class="insp-card ${{hl(e.codigo)}}">
                <div class="insp-card-head">
                  <span>${{escHtml(e.codigo)}} — ${{escHtml(e.nombre)}}</span>
                  <span class="chip chip-inv">${{escHtml(e.importancia)}}</span>
                </div>
                <p style="margin-bottom:6px;">${{escHtml(e.descripcion)}}</p>
                ${{eIlas.map(il => `
                  <details class="ila-details" ${{hl(il.codigo) || (highlightCode && il.esp_code && hl(il.esp_code)) ? 'open' : ''}}>
                    <summary>${{escHtml(il.codigo)}} → ${{escHtml(il.esp_code)}}${{il.prueba_tipo ? ' [' + escHtml(il.prueba_tipo) + ']' : ''}}: ${{escHtml(il.nombre)}}</summary>
                    <div class="ila-body">
                      <b>Actor:</b> ${{escHtml(il.actor)}} | <b>Tablas:</b> ${{escHtml(il.tbs.join(', '))}}
                      <b>GUIs/Modales (ILA):</b> ${{escHtml(il.guis.concat(il.mdls).join(', ') || il.esp_artefactos || 'GUI asociada')}}
                      ${{il.esp_trigger ? `\n<b>Disparador Entry GUI (ESP):</b> <code>${{escHtml(il.esp_trigger)}}</code>` : ''}}
                      ${{il.esp_artefactos ? `\n<b>Artefactos ESP:</b> ${{escHtml(il.esp_artefactos)}}` : ''}}
                      \n<b>Precondición (ILA):</b> ${{escHtml(il.precondicion)}}
                      \n<b>Procedimiento (ILA):</b> ${{escHtml(il.procedimiento)}}
                      ${{il.esp_proc ? `\n<b>Procedimiento Detallado (${{escHtml(il.esp_code)}}):</b> ${{escHtml(il.esp_proc)}}` : ''}}
                      \n<b>Postcondición:</b> ${{escHtml(il.postcondicion || il.esp_post)}}
                      ${{il.prueba_desc ? `\n<b>Prueba (${{escHtml(il.prueba_tipo)}} — ${{escHtml(il.prueba_tipo_desc)}}):</b> ${{escHtml(il.prueba_desc)}}` : ''}}
                      ${{il.riesgo_ila ? `\n<b>Riesgo ${{escHtml(il.riesgo_ila.clave)}}:</b> ${{escHtml(il.riesgo_ila.riesgo)}} → <i>Mitigación:</i> ${{escHtml(il.riesgo_ila.mitigacion)}}` : ''}}
                    </div>
                  </details>
                `).join('')}}
              </div>
            `;
          }}).join('') || '<div class="insp-card">Este componente actúa como puerta de entrada o infraestructura transversal para las 27 Educciones. Revise la pestaña "Resumen &amp; APIs" o abra "Matriz Total [C]".</div>'}}
        `;
      }} else if (currentTab === 'rnfs') {{
        inspBody.innerHTML = `
          <div class="insp-section-title">Requisitos No Funcionales Vinculados (${{info.rnfs.length}})</div>
          ${{info.rnfs.map(r => `
            <div class="insp-card ${{hl(r.codigo)}}">
              <div class="insp-card-head">
                <span>${{escHtml(r.display_code)}} — ${{escHtml(r.nombre)}}</span>
                <span class="chip">${{escHtml(r.atributo)}}</span>
              </div>
              <p><b>Importancia:</b> ${{escHtml(r.importancia)}}</p>
              <p style="margin-top:4px;">${{escHtml(r.descripcion)}}</p>
              ${{r.comentario ? `<p style="margin-top:4px;font-style:italic;">Nota: ${{escHtml(r.comentario)}}</p>` : ''}}
            </div>
          `).join('') || '<div class="insp-card">Sin RNF directo en este nodo.</div>'}}
        `;
      }} else if (currentTab === 'datos') {{
        const epGuis = (n.kind === 'entry')
          ? APP_DATA.catalog.guis.filter(g => g.ep && g.ep.includes(n.id))
          : info.guis;
        inspBody.innerHTML = `
          <div class="insp-section-title">Ubicación de Interfaces GUI (${{epGuis.length}} secciones — "Esta GUI va acá")</div>
          ${{epGuis.map(g => `
            <div class="insp-card ${{hl(g.titulo)}} ${{hl(g.gui_code)}}">
              <div class="insp-card-head">
                <span>${{escHtml(g.titulo)}} ${{g.nombre_corto ? '— ' + escHtml(g.nombre_corto) : ''}}</span>
                <span class="chip">${{escHtml(g.edu)}}</span>
              </div>
              <p><b>Bloque Destino:</b> <b>${{escHtml(g.bloque)}}</b> &bull; <b>Entry Point (Ruta):</b> <code>${{escHtml(g.ep || 'Transversal')}}</code></p>
              <p style="margin-top:3px;"><b>Modales (${{g.modales.length}}):</b> ${{escHtml(g.modales.join(' • '))}}</p>
            </div>
          `).join('') || '<div class="insp-card">Sin pantallas GUI asignadas directamente a este componente.</div>'}}
          <div class="insp-section-title">Tablas de Datos / Storage / Redis (${{n.tbs.length}})</div>
          <div class="insp-card">
            ${{n.tbs.length ? n.tbs.map(tb => `<span class="chip ${{hl(tb) ? 'chip-inv' : ''}}" style="margin:2px;">${{escHtml(tb)}}</span>`).join('') : '<span>No gestiona almacenamiento directo (actor, entry point HTTP o gateway stateless).</span>'}}
          </div>
        `;
      }}
    }}

    document.querySelectorAll('.insp-tab').forEach(btn => {{
      btn.addEventListener('click', () => {{
        currentTab = btn.dataset.tab;
        renderInspector();
      }});
    }});
    document.getElementById('btnCloseInsp').onclick = () => {{
      drawer.classList.remove('open');
      document.getElementById('btnToggleInspector').classList.remove('active');
    }};
    document.getElementById('btnToggleInspector').onclick = () => {{
      drawer.classList.toggle('open');
      document.getElementById('btnToggleInspector').classList.toggle('active');
      if (drawer.classList.contains('open')) renderInspector();
    }};
    document.getElementById('btnCenterNode').onclick = () => {{
      if (currentInspKind === 'node') focusNodeOnCanvas(currentInspId, false);
      else focusFlowOnCanvas(currentInspId);
    }};
    const nodeIds = APP_DATA.nodes.map(n => n.id);
    document.getElementById('btnPrevNode').onclick = () => {{
      const curIdx = nodeIds.indexOf(currentInspId);
      const prevIdx = curIdx > 0 ? curIdx - 1 : nodeIds.length - 1;
      focusNodeOnCanvas(nodeIds[prevIdx], true);
    }};
    document.getElementById('btnNextNode').onclick = () => {{
      const curIdx = nodeIds.indexOf(currentInspId);
      const nextIdx = (curIdx + 1) % nodeIds.length;
      focusNodeOnCanvas(nodeIds[nextIdx], true);
    }};

    // Click en tarjetas y flujos
    document.querySelectorAll('.box-card').forEach(card => {{
      card.addEventListener('click', (e) => {{
        e.stopPropagation();
        focusNodeOnCanvas(card.dataset.node, true);
      }});
    }});
    document.querySelectorAll('.flow-pill, .flow-edge-group').forEach(el => {{
      el.addEventListener('click', (e) => {{
        e.stopPropagation();
        focusFlowOnCanvas(el.dataset.flow);
      }});
    }});

    // =========================================================================
    // FILTRO POR CAPA Y BUSCADOR GLOBAL DE CATÁLOGO
    // =========================================================================
    document.getElementById('capaFilter').addEventListener('change', (e) => {{
      const val = e.target.value;
      document.querySelectorAll('.box-card').forEach(c => {{
        c.classList.toggle('dimmed', val !== 'ALL' && c.dataset.capa !== val);
      }});
      document.querySelectorAll('.flow-edge-group, .flow-pill').forEach(f => {{
        if (val === 'ALL') {{ f.classList.remove('dimmed'); return; }}
        const srcOk = NODE_MAP[f.dataset.src]?.capa === val;
        const dstOk = NODE_MAP[f.dataset.dst]?.capa === val;
        f.classList.toggle('dimmed', !(srcOk || dstOk));
      }});
    }});

    const searchInput = document.getElementById('searchInput');
    const searchDropdown = document.getElementById('searchDropdown');

    function buildSearchIndex() {{
      const items = [];
      APP_DATA.nodes.forEach(n => {{
        const typ = n.kind === 'entry' ? 'ENTRY POINT' : 'MÓDULO';
        items.push({{ type: typ, code: n.code, title: n.title, sub: n.capa + (n.gui_strip ? ' • ' + n.gui_strip : ''), node: n.id, tab: 'resumen', kw: (n.id + ' ' + n.code + ' ' + n.title + ' ' + n.subtitle + ' ' + (n.gui_strip || '') + ' ' + n.summary_lines.join(' ')).toLowerCase() }});
        n.apis.forEach(a => items.push({{ type: 'API', code: a.method, title: a.endpoint, sub: n.code + ' — ' + a.purpose, node: n.id, tab: 'resumen', kw: (a.endpoint + ' ' + a.purpose + ' ' + n.code).toLowerCase() }}));
        n.tbs.forEach(tb => items.push({{ type: 'TABLA/S3', code: tb, title: 'Almacenamiento en ' + n.code, sub: n.title, node: n.id, tab: 'datos', kw: (tb + ' ' + n.code).toLowerCase() }}));
      }});
      APP_DATA.catalog.educciones.forEach(e => {{
        items.push({{ type: 'EDUCCIÓN', code: e.codigo, title: e.nombre, sub: 'Bloque ' + e.bloque + ' • ' + e.importancia, node: e.bloque, tab: 'edus', kw: (e.codigo + ' ' + e.nombre + ' ' + e.descripcion).toLowerCase() }});
      }});
      APP_DATA.catalog.ilaciones.forEach(il => {{
        items.push({{ type: 'ILACIÓN', code: il.codigo, title: il.nombre, sub: il.edu + ' • ' + il.esp_code + ' • Bloque ' + il.bloque + (il.prueba_tipo ? ' • ' + il.prueba_tipo : ''), node: il.bloque, tab: 'edus', kw: (il.codigo + ' ' + il.esp_code + ' ' + il.nombre + ' ' + il.edu + ' ' + il.esp_trigger + ' ' + il.esp_artefactos + ' ' + il.prueba_tipo + ' ' + il.guis.join(' ') + ' ' + il.mdls.join(' ')).toLowerCase() }});
      }});
      APP_DATA.catalog.rnfs.forEach(r => {{
        items.push({{ type: 'RNF', code: r.display_code, title: r.nombre, sub: r.atributo + ' • Nodos: ' + r.nodos.join(', '), node: r.nodos[0], tab: 'rnfs', kw: (r.codigo + ' ' + r.nombre + ' ' + r.atributo + ' ' + r.descripcion).toLowerCase() }});
      }});
      APP_DATA.catalog.guis.forEach(g => {{
        items.push({{ type: 'GUI/MDL', code: g.gui_code || g.edu || 'GUI', title: g.titulo + (g.nombre_corto ? ' — ' + g.nombre_corto : ''), sub: 'Bloque ' + g.bloque + ' • Entry: ' + (g.ep || 'Transversal') + ' • ' + g.modales.join(', '), node: g.bloque, tab: 'datos', kw: (g.gui_code + ' ' + g.titulo + ' ' + g.nombre_corto + ' ' + g.ep + ' ' + g.modales.join(' ')).toLowerCase() }});
      }});
      APP_DATA.flows.forEach(f => {{
        items.push({{ type: 'FLUJO', code: f.id, title: f.core + ' (' + f.detail + ')', sub: f.src + ' → ' + f.dst + ' • ' + f.api, flow: f.id, kw: (f.id + ' ' + f.core + ' ' + f.detail + ' ' + f.api).toLowerCase() }});
      }});
      return items;
    }}
    const SEARCH_INDEX = buildSearchIndex();

    searchInput.addEventListener('input', () => {{
      const q = searchInput.value.trim().toLowerCase();
      document.querySelectorAll('.box-card').forEach(c => c.classList.remove('search-hit'));
      if (!q) {{
        searchDropdown.classList.remove('open');
        return;
      }}
      const rankType = {{ 'RNF': 1, 'ENTRY POINT': 2, 'EDUCCIÓN': 3, 'GUI/MDL': 4, 'ILACIÓN': 5, 'API': 6, 'TABLA/S3': 7, 'FLUJO': 8, 'MÓDULO': 9 }};
      const hits = SEARCH_INDEX
        .filter(it => it.kw.includes(q))
        .sort((a, b) => {{
          const ac = a.code.toLowerCase().includes(q) ? 0 : 1;
          const bc = b.code.toLowerCase().includes(q) ? 0 : 1;
          if (ac !== bc) return ac - bc;
          return (rankType[a.type] || 9) - (rankType[b.type] || 9);
        }})
        .slice(0, 24);
      const hitNodes = new Set(hits.map(h => h.node).filter(Boolean));
      hitNodes.forEach(nid => {{
        const c = document.getElementById('node-' + nid);
        if (c) c.classList.add('search-hit');
      }});

      if (!hits.length) {{
        searchDropdown.innerHTML = '<div class="search-item">Sin coincidencias en el catálogo.</div>';
      }} else {{
        searchDropdown.innerHTML = hits.map((h, i) => `
          <div class="search-item" data-hit-idx="${{i}}">
            <div class="si-top"><span>${{escHtml(h.code)}} — ${{escHtml(h.title)}}</span><span class="si-type">${{h.type}}</span></div>
            <div class="si-sub">${{escHtml(h.sub)}}</div>
          </div>
        `).join('');
        searchDropdown.querySelectorAll('.search-item').forEach((el, idx) => {{
          el.onclick = () => {{
            const h = hits[idx];
            searchDropdown.classList.remove('open');
            if (h.flow) focusFlowOnCanvas(h.flow);
            else focusNodeOnCanvas(h.node, true, h.tab, h.code);
          }};
        }});
      }}
      searchDropdown.classList.add('open');
    }});

    document.addEventListener('click', (e) => {{
      if (!e.target.closest('.search-wrap')) searchDropdown.classList.remove('open');
    }});

    // =========================================================================
    // MODAL MATRIZ GLOBAL DE TRAZABILIDAD (27 EDU, 108 ILA, 28 RNF, APIS, GUIS, TB)
    // =========================================================================
    const matrixModal = document.getElementById('matrixModal');
    const matrixBody = document.getElementById('matrixBody');
    const matrixFilterInput = document.getElementById('matrixFilterInput');
    let currentMtab = 'edus';

    function renderMatrix() {{
      const q = matrixFilterInput.value.trim().toLowerCase();
      document.querySelectorAll('[data-mtab]').forEach(b => b.classList.toggle('active', b.dataset.mtab === currentMtab));

      if (currentMtab === 'edus') {{
        const rows = APP_DATA.catalog.educciones.filter(e => !q || (e.codigo + e.nombre + e.bloque + e.descripcion).toLowerCase().includes(q));
        matrixBody.innerHTML = `<table class="audit-table"><thead><tr><th>Código</th><th>Nombre Educción</th><th>Bloque</th><th>Importancia</th><th>Descripción Oficial del Catálogo</th><th>Acción</th></tr></thead><tbody>
          ${{rows.map(e => `<tr><td><b>${{escHtml(e.codigo)}}</b></td><td>${{escHtml(e.nombre)}}</td><td><b>${{escHtml(e.bloque)}}</b></td><td>${{escHtml(e.importancia)}}</td><td>${{escHtml(e.descripcion)}}</td><td><button class="flow-jump-btn" onclick="jumpFromMatrix('${{e.bloque}}','edus','${{e.codigo}}')">Ir a ${{e.bloque}}</button></td></tr>`).join('')}}
        </tbody></table>`;
      }} else if (currentMtab === 'ilaciones') {{
        const rows = APP_DATA.catalog.ilaciones.filter(i => !q || (i.codigo + i.nombre + i.edu + i.bloque + i.tbs.join(' ') + i.guis.join(' ')).toLowerCase().includes(q));
        matrixBody.innerHTML = `<table class="audit-table"><thead><tr><th>ILA</th><th>EDU</th><th>Bloque</th><th>Nombre Ilación</th><th>GUIs / Modales</th><th>Tablas TB_*</th><th>Riesgo &amp; Mitigación</th><th>Acción</th></tr></thead><tbody>
          ${{rows.map(i => `<tr><td><b>${{escHtml(i.codigo)}}</b></td><td>${{escHtml(i.edu)}}</td><td><b>${{escHtml(i.bloque)}}</b></td><td>${{escHtml(i.nombre)}}</td><td>${{escHtml(i.guis.concat(i.mdls).join(', '))}}</td><td><code>${{escHtml(i.tbs.join(', '))}}</code></td><td>${{i.riesgo_ila ? escHtml(i.riesgo_ila.riesgo + ' → ' + i.riesgo_ila.mitigacion) : ''}}</td><td><button class="flow-jump-btn" onclick="jumpFromMatrix('${{i.bloque}}','edus','${{i.codigo}}')">Ver</button></td></tr>`).join('')}}
        </tbody></table>`;
      }} else if (currentMtab === 'esps') {{
        const rows = APP_DATA.catalog.ilaciones.filter(i => !q || (i.esp_code + i.codigo + i.nombre + i.bloque + i.esp_trigger + i.esp_artefactos + i.prueba_tipo + i.prueba_desc).toLowerCase().includes(q));
        matrixBody.innerHTML = `<p style="font-size:11px;margin-bottom:8px;"><b>Especificaciones Formales (&lt;w:sdt&gt;):</b> ${{APP_DATA.catalog.esps_resumen.filled}} fichas completas de ${{APP_DATA.catalog.esps_resumen.total_headings}} encabezados (vacías en base: ${{APP_DATA.catalog.esps_resumen.empty_headings.join(', ')}}) &bull; <b>Matriz Pruebas:</b> ${{APP_DATA.catalog.pruebas_map.length}} filas / 20 tipos (T-001..T-020).</p>
        <table class="audit-table"><thead><tr><th>ESP</th><th>ILA Origen</th><th>Bloque</th><th>Disparador UI / Artefactos</th><th>Prueba Asignada</th><th>Descripción de Prueba</th><th>Acción</th></tr></thead><tbody>
          ${{rows.map(i => `<tr><td><b>${{escHtml(i.esp_code)}}</b>${{i.esp_empty ? ' <i>(vacía base)</i>' : ''}}</td><td>${{escHtml(i.codigo)}}</td><td><b>${{escHtml(i.bloque)}}</b></td><td><code>${{escHtml(i.esp_trigger || i.esp_artefactos || '—')}}</code></td><td><b>${{escHtml(i.prueba_tipo || '—')}}</b><br/><small>${{escHtml(i.prueba_tipo_desc || '')}}</small></td><td>${{escHtml(i.prueba_desc || '—')}}</td><td><button class="flow-jump-btn" onclick="jumpFromMatrix('${{i.bloque}}','edus','${{i.esp_code}}')">Ver</button></td></tr>`).join('')}}
        </tbody></table>`;
      }} else if (currentMtab === 'rnfs') {{
        const rows = APP_DATA.catalog.rnfs.filter(r => !q || (r.display_code + r.nombre + r.atributo + r.descripcion + r.nodos.join(' ')).toLowerCase().includes(q));
        matrixBody.innerHTML = `<table class="audit-table"><thead><tr><th>Código RNF</th><th>Nombre</th><th>Atributo ISO 25010</th><th>Imp.</th><th>Nodos Implementadores</th><th>Descripción Oficial</th></tr></thead><tbody>
          ${{rows.map(r => `<tr><td><b>${{escHtml(r.display_code)}}</b></td><td>${{escHtml(r.nombre)}}</td><td>${{escHtml(r.atributo)}}</td><td>${{escHtml(r.importancia)}}</td><td>${{r.nodos.map(nid => `<button class="flow-jump-btn" onclick="jumpFromMatrix('${{nid}}','rnfs','${{r.codigo}}')">${{escHtml(nid)}}</button>`).join('')}}</td><td>${{escHtml(r.descripcion)}}</td></tr>`).join('')}}
        </tbody></table>`;
      }} else if (currentMtab === 'apis') {{
        const rows = [];
        APP_DATA.nodes.forEach(n => n.apis.forEach(a => rows.push({{ node: n.id, code: n.code, ...a }})));
        const filtered = rows.filter(a => !q || (a.code + a.method + a.endpoint + a.purpose + a.auth).toLowerCase().includes(q));
        matrixBody.innerHTML = `<table class="audit-table"><thead><tr><th>Módulo</th><th>Método</th><th>Endpoint / Contrato</th><th>Autenticación</th><th>SLA</th><th>Propósito Funcional</th><th>Acción</th></tr></thead><tbody>
          ${{filtered.map(a => `<tr><td><b>${{escHtml(a.code)}}</b></td><td><b>${{escHtml(a.method)}}</b></td><td><code>${{escHtml(a.endpoint)}}</code></td><td>${{escHtml(a.auth)}}</td><td>${{escHtml(a.sla)}}</td><td>${{escHtml(a.purpose)}}</td><td><button class="flow-jump-btn" onclick="jumpFromMatrix('${{a.node}}','resumen','${{escHtml(a.endpoint)}}')">Ir</button></td></tr>`).join('')}}
        </tbody></table>`;
      }} else if (currentMtab === 'guis') {{
        const eps = APP_DATA.nodes.filter(n => n.kind === 'entry').filter(ep => !q || (ep.id + ep.title + ep.gui_strip + ep.summary_lines.join(' ')).toLowerCase().includes(q));
        const rows = APP_DATA.catalog.guis.filter(g => !q || (g.titulo + g.nombre_corto + g.ep + g.edu + g.bloque + g.modales.join(' ')).toLowerCase().includes(q));
        matrixBody.innerHTML = `
          <div style="margin-bottom:12px;">
            <p style="font-size:11px;font-weight:900;margin-bottom:6px;text-transform:uppercase;">1. Entry Points (EP-01..EP-06): Quién actúa y por dónde entra</p>
            <table class="audit-table"><thead><tr><th>Entry Point</th><th>Portal / Endpoint</th><th>Actores / Disparador</th><th>GUIs Alojadas / Uso</th><th>Acción</th></tr></thead><tbody>
              ${{eps.map(ep => `<tr><td><b>${{escHtml(ep.id)}}</b></td><td>${{escHtml(ep.title)}}</td><td>${{escHtml((ep.summary_lines[0] || '').replace(/<[^>]+>/g,''))}}</td><td>${{escHtml(ep.gui_strip)}}</td><td><button class="flow-jump-btn" onclick="jumpFromMatrix('${{ep.id}}','datos','')">Ir a ${{ep.id}}</button></td></tr>`).join('')}}
            </tbody></table>
          </div>
          <p style="font-size:11px;font-weight:900;margin-bottom:6px;text-transform:uppercase;">2. Ubicación Exacta de las 28 Secciones GUI y 140 Modales ("Esta GUI va acá")</p>
          <table class="audit-table"><thead><tr><th>GUI Catálogo</th><th>Función</th><th>EDU</th><th>Bloque</th><th>Entry Point (EP)</th><th>5 Modales (MDL)</th><th>Acción</th></tr></thead><tbody>
          ${{rows.map(g => `<tr><td><b>${{escHtml(g.titulo)}}</b></td><td>${{escHtml(g.nombre_corto)}}</td><td>${{escHtml(g.edu)}}</td><td><b>${{escHtml(g.bloque)}}</b></td><td><code>${{escHtml(g.ep || 'N/A')}}</code></td><td>${{escHtml(g.modales.join(' | '))}}</td><td><button class="flow-jump-btn" onclick="jumpFromMatrix('${{g.bloque}}','datos','${{escHtml(g.gui_code)}}')">Ir a ${{g.bloque}}</button></td></tr>`).join('')}}
        </tbody></table>`;
      }} else if (currentMtab === 'tables') {{
        const tbMap = new Map();
        APP_DATA.nodes.forEach(n => n.tbs.forEach(tb => {{
          if (!tbMap.has(tb)) tbMap.set(tb, []);
          tbMap.get(tb).push(n.id);
        }}));
        const rows = Array.from(tbMap.entries()).filter(([tb, nids]) => !q || (tb + nids.join(' ')).toLowerCase().includes(q));
        matrixBody.innerHTML = `<table class="audit-table"><thead><tr><th>Tabla / Bucket / Key</th><th>Bloques Consumidores / Repositorio</th></tr></thead><tbody>
          ${{rows.map(([tb, nids]) => `<tr><td><code><b>${{escHtml(tb)}}</b></code></td><td>${{nids.map(nid => `<button class="flow-jump-btn" onclick="jumpFromMatrix('${{nid}}','datos','${{escHtml(tb)}}')">${{escHtml(nid)}}</button>`).join('')}}</td></tr>`).join('')}}
        </tbody></table>`;
      }}
    }}

    function jumpFromMatrix(nid, tab, code) {{
      matrixModal.classList.remove('open');
      focusNodeOnCanvas(nid, true, tab, code);
    }}

    document.getElementById('btnOpenMatrix').onclick = () => {{ matrixModal.classList.add('open'); renderMatrix(); }};
    document.getElementById('bottomAuditBadge').onclick = () => {{ matrixModal.classList.add('open'); renderMatrix(); }};
    document.getElementById('btnCloseMatrix').onclick = () => matrixModal.classList.remove('open');
    document.querySelectorAll('[data-mtab]').forEach(b => b.onclick = () => {{ currentMtab = b.dataset.mtab; renderMatrix(); }});
    matrixFilterInput.oninput = renderMatrix;

    // =========================================================================
    // MODAL VISOR OFICIAL MERMAID (CON RENDER OFFLINE + COPIADO .MMD)
    // =========================================================================
    const mermaidModal = document.getElementById('mermaidModal');
    const mermaidStage = document.getElementById('mermaidStage');
    const mermaidCodeBox = document.getElementById('mermaidCodeBox');
    let currentMmdKey = 'm1';
    let mmdZoom = 1.0;
    let showingCode = false;

    function applyMermaidScale() {{
      const svgEl = mermaidStage.querySelector('svg');
      if (!svgEl) return;
      const vbAttr = svgEl.getAttribute('viewBox');
      let vbW = parseFloat(svgEl.dataset.vbW || '0');
      let vbH = parseFloat(svgEl.dataset.vbH || '0');
      if ((!vbW || !vbH) && vbAttr) {{
        const p = vbAttr.trim().split(/[\\s,]+/).map(Number);
        if (p.length === 4 && p[2] > 0 && p[3] > 0) {{
          vbW = p[2]; vbH = p[3];
          svgEl.dataset.vbW = vbW;
          svgEl.dataset.vbH = vbH;
        }}
      }}
      if (vbW && vbH) {{
        svgEl.removeAttribute('width');
        svgEl.removeAttribute('height');
        svgEl.style.maxWidth = 'none';
        svgEl.style.width = Math.round(vbW * mmdZoom) + 'px';
        svgEl.style.height = Math.round(vbH * mmdZoom) + 'px';
        svgEl.style.display = 'block';
        svgEl.style.margin = '0 auto';
      }}
    }}

    async function renderMermaidView() {{
      document.querySelectorAll('[data-mmd]').forEach(b => b.classList.toggle('active', b.dataset.mmd === currentMmdKey));
      const spec = APP_DATA.mermaid[currentMmdKey];
      mermaidCodeBox.value = spec.code;
      if (showingCode) {{
        mermaidStage.style.display = 'none';
        mermaidCodeBox.style.display = 'block';
        return;
      }}
      mermaidStage.style.display = 'block';
      mermaidCodeBox.style.display = 'none';

      if (typeof window.mermaid === 'undefined') {{
        mermaidStage.innerHTML = '<p style="font-weight:bold;padding:20px;">Cargando librería local Mermaid...</p>';
        return;
      }}
      try {{
        window.mermaid.initialize({{ startOnLoad: false, securityLevel: 'loose', flowchart: {{ useMaxWidth: false, htmlLabels: true }} }});
        const uid = 'mmd_svg_' + currentMmdKey + '_' + Date.now();
        const {{ svg }} = await window.mermaid.render(uid, spec.code);
        mermaidStage.innerHTML = svg;
        const svgEl = mermaidStage.querySelector('svg');
        if (svgEl) {{
          const vb = (svgEl.getAttribute('viewBox') || '').trim().split(/[\\s,]+/).map(Number);
          if (vb.length === 4 && vb[2] > 0) {{
            svgEl.dataset.vbW = vb[2];
            svgEl.dataset.vbH = vb[3];
            // Ajuste inicial legible equilibrado en ancho y alto
            const targetW = Math.max(960, mermaidStage.clientWidth - 48);
            const targetH = Math.max(520, mermaidStage.clientHeight - 48);
            const fitScale = Math.min(targetW / vb[2], targetH / vb[3]);
            if (mmdZoom === 1.0) mmdZoom = Math.min(1.65, Math.max(0.25, fitScale));
          }}
        }}
        applyMermaidScale();
      }} catch (err) {{
        mermaidStage.innerHTML = `<div style="border:2px solid #000;padding:12px;text-align:left;"><b>Error al renderizar Mermaid:</b> ${{escHtml(err.message)}}</div>`;
      }}
    }}

    document.getElementById('btnOpenMermaid').onclick = () => {{ mmdZoom = 1.0; mermaidModal.classList.add('open'); renderMermaidView(); }};
    document.getElementById('btnCloseMermaid').onclick = () => mermaidModal.classList.remove('open');
    document.querySelectorAll('[data-mmd]').forEach(b => b.onclick = () => {{ currentMmdKey = b.dataset.mmd; mmdZoom = 1.0; renderMermaidView(); }});
    document.getElementById('btnMmdZoomIn').onclick = () => {{ mmdZoom = Math.min(3.5, mmdZoom * 1.25); applyMermaidScale(); }};
    document.getElementById('btnMmdZoomOut').onclick = () => {{ mmdZoom = Math.max(0.30, mmdZoom * 0.8); applyMermaidScale(); }};
    document.getElementById('btnMmdFit').onclick = () => {{ mmdZoom = 1.0; renderMermaidView(); }};
    document.getElementById('btnMmdToggleCode').onclick = () => {{
      showingCode = !showingCode;
      document.getElementById('btnMmdToggleCode').textContent = showingCode ? 'Ver Diagrama SVG' : 'Ver Código .mmd';
      renderMermaidView();
    }};
    document.getElementById('btnMmdCopy').onclick = () => {{
      navigator.clipboard?.writeText(APP_DATA.mermaid[currentMmdKey].code);
      const btn = document.getElementById('btnMmdCopy');
      btn.textContent = '✓ Copiado';
      setTimeout(() => btn.textContent = 'Copiar Código', 1400);
    }};

    // Teclado rápido
    window.addEventListener('keydown', (e) => {{
      if (document.activeElement && ['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) {{
        if (e.key === 'Escape') document.activeElement.blur();
        return;
      }}
      if (e.key === '+' || e.key === '=') zoomAtPoint(1.2, window.innerWidth / 2, window.innerHeight / 2);
      else if (e.key === '-') zoomAtPoint(0.83, window.innerWidth / 2, window.innerHeight / 2);
      else if (e.key === '0') fitToScreen();
      else if (e.key === 'i' || e.key === 'I') document.getElementById('btnToggleInspector').click();
      else if (e.key === 'm' || e.key === 'M') document.getElementById('btnOpenMermaid').click();
      else if (e.key === 'c' || e.key === 'C') document.getElementById('btnOpenMatrix').click();
      else if (e.key === 'Escape') {{
        matrixModal.classList.remove('open');
        mermaidModal.classList.remove('open');
        drawer.classList.remove('open');
        document.getElementById('btnToggleInspector').classList.remove('active');
        document.querySelectorAll('.box-card').forEach(c => c.classList.remove('focused', 'search-hit'));
        document.querySelectorAll('.flow-edge-group, .flow-pill').forEach(el => el.classList.remove('highlighted'));
      }}
    }});

    window.addEventListener('resize', fitToScreen);
    window.addEventListener('DOMContentLoaded', () => {{
      fitToScreen();
    }});
  </script>
</body>
</html>"""
    return html


def main():
    print("1. Ejecutando auditoría geométrica...")
    geo_issues = audit_geometry()
    if geo_issues:
        for gi in geo_issues:
            print("ERROR:", gi)
        raise SystemExit(1)
    print(f"   -> OK: {len(NODES)} tarjetas, {len(FLOWS)} flujos, 0 colisiones.")

    print("2. Cargando y validando Catálogo completo v01.00...")
    catalog = load_enriched_catalog()
    print(f"   -> OK: 27/27 EDU, 108/108 ILA, 28/28 RNF, 28/28 GUI cargados.")

    print("3. Generando suite Mermaid (.mmd y .md)...")
    build_all_mermaid()

    print("4. Generando HTML Definitivo Integral...")
    html = build_html_document(catalog)
    for dest in [OUT_HTML_VISOR, OUT_HTML_VL, OUT_HTML_COMP]:
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"   -> Escrito: {dest} ({len(html)/1024:.1f} KB)")

    print("Construcción culminada con éxito.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
package_delivery.py
Empaqueta todos los artefactos generados en la Fase 1 del Hito 3 en un ZIP listo para presentar.
"""

import os
import shutil
import zipfile

BASE_DIR = "/home/marco/Projects/NexoVitalis360"
PKG_DIR = os.path.join(BASE_DIR, "ENTREGA_FASE1_HITO3_NEXOVITALIS360")
ZIP_OUTPUT = os.path.join(BASE_DIR, "NexoVitalis360_Entrega_Fase1_Hito3.zip")

def make_dirs():
    dirs = [
        "01_DOCUMENTOS_FORMALES_PLANTILLAS",
        "02_GOBERNANZA_Y_ACTAS_DE_TRABAJO",
        "03_LINEA_BASE_REQUERIMIENTOS_ACTUALIZADA",
        "04_DIAGRAMAS_ALTA_RESOLUCION_300DPI/06_Arquitectura_Centrada_Datos",
        "04_DIAGRAMAS_ALTA_RESOLUCION_300DPI/07_GUIs_Interfaces",
        "05_VISOR_INTERACTIVO_SUITE_HTML",
        "06_PLAN_MAESTRO_Y_TRAZABILIDAD"
    ]
    for d in dirs:
        os.makedirs(os.path.join(PKG_DIR, d), exist_ok=True)

def copy_files():
    # 01 Plantillas
    p6_dir = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/06_Arquitectura_Centrada_Datos")
    p7_dir = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/07_GUIs_Interfaces")
    dst_docs = os.path.join(PKG_DIR, "01_DOCUMENTOS_FORMALES_PLANTILLAS")
    
    for f in ["Plantilla_6_Arquitectura_Centrada_Datos_v01.00.docx", "Plantilla_6_Arquitectura_Centrada_Datos_v01.00.pdf"]:
        src = os.path.join(p6_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst_docs)
            
    for f in ["Plantilla_7_GUIs_Interfaces_v01.00.docx", "Plantilla_7_GUIs_Interfaces_v01.00.pdf"]:
        src = os.path.join(p7_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst_docs)

    # 02 Actas
    dst_actas = os.path.join(PKG_DIR, "02_GOBERNANZA_Y_ACTAS_DE_TRABAJO")
    actas_src = os.path.join(BASE_DIR, "00_ADMINISTRACION_Y_GESTION_EQUIPO/Actas_de_Trabajo")
    for f in ["ACTA DE TRABAJO N°06.docx", "ACTA DE TRABAJO N°06.pdf"]:
        src = os.path.join(actas_src, f)
        if os.path.exists(src):
            shutil.copy2(src, dst_actas)
    json_src = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/Actas_de_Trabajo/acta_06.json")
    if os.path.exists(json_src):
        shutil.copy2(json_src, dst_actas)

    # 03 Catalogo
    dst_cat = os.path.join(PKG_DIR, "03_LINEA_BASE_REQUERIMIENTOS_ACTUALIZADA")
    cat_docx = os.path.join(BASE_DIR, "01_LINEA_BASE_REQUERIMIENTOS/Artefacto_Catalogo_Requisitos_v01.00.docx")
    cat_md = os.path.join(BASE_DIR, "01_LINEA_BASE_REQUERIMIENTOS/EXPLICACION_REFINAMIENTO_ILACIONES_Y_RNF.md")
    if os.path.exists(cat_docx):
        shutil.copy2(cat_docx, dst_cat)
    if os.path.exists(cat_md):
        shutil.copy2(cat_md, dst_cat)

    # 04 Diagramas
    dst_diag6 = os.path.join(PKG_DIR, "04_DIAGRAMAS_ALTA_RESOLUCION_300DPI/06_Arquitectura_Centrada_Datos")
    for f in os.listdir(p6_dir):
        if not f.startswith("Plantilla_6"):
            shutil.copy2(os.path.join(p6_dir, f), dst_diag6)

    dst_diag7 = os.path.join(PKG_DIR, "04_DIAGRAMAS_ALTA_RESOLUCION_300DPI/07_GUIs_Interfaces")
    for f in os.listdir(p7_dir):
        if not f.startswith("Plantilla_7"):
            shutil.copy2(os.path.join(p7_dir, f), dst_diag7)

    # 05 Visor
    dst_visor = os.path.join(PKG_DIR, "05_VISOR_INTERACTIVO_SUITE_HTML")
    src_visor = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/VISOR_HTML_ARQUITECTURA_v01.00")
    for root, dirs, files in os.walk(src_visor):
        rel = os.path.relpath(root, src_visor)
        target_dir = os.path.join(dst_visor, rel) if rel != "." else dst_visor
        os.makedirs(target_dir, exist_ok=True)
        for file in files:
            shutil.copy2(os.path.join(root, file), target_dir)

    # 06 Plan y trazabilidad
    dst_plan = os.path.join(PKG_DIR, "06_PLAN_MAESTRO_Y_TRAZABILIDAD")
    shutil.copy2(os.path.join(BASE_DIR, "fase3.md"), dst_plan)
    shutil.copy2(os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/CONTROL_DE_VERSIONES_DIAGRAMAS.md"), dst_plan)

def make_zip():
    print(f"Comprimiendo {PKG_DIR} -> {ZIP_OUTPUT}...")
    with zipfile.ZipFile(ZIP_OUTPUT, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PKG_DIR):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, BASE_DIR)
                zipf.write(abs_path, rel_path)
    sz = os.path.getsize(ZIP_OUTPUT)
    print(f"¡ZIP creado con éxito! Tamaño: {sz / (1024*1024):.2f} MB")

if __name__ == "__main__":
    make_dirs()
    copy_files()
    make_zip()

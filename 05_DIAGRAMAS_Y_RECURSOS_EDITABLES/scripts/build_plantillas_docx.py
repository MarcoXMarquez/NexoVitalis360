#!/usr/bin/env python3
"""
build_plantillas_docx.py
Genera los documentos formales Word (.docx) y PDF para:
- Plantilla 6: Arquitectura Centrada en Datos (v01.00)
- Plantilla 7: GUIs e Interfaces (v01.00)
Basándose en las plantillas oficiales del curso en Material del curso/Plantillas/
e incrustando los diagramas vectoriales renderizados a 300 DPI.
"""

import os
import subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

MEMBERS = [
    ("Marquez Herrera Marco Antonio (Líder)", "Venero Guevara Christian Henry"),
    ("Alfonso Huacasi Alejandro Sebastián", "Payehuanca Riquelme Jhastyn Jefferson"),
    ("Turpo Huanca Wilson Josue", "Arce Mayhua Leonardo Rubén"),
    ("Gallegos Condori Anette Isabel", "Huamani Condori Jeanpiero Sixto")
]

def format_cell(cell, text, bold=False, font_size=9, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = text
    p = cell.paragraphs[0]
    p.alignment = align
    for run in p.runs:
        run.font.name = 'Arial'
        run.font.size = Pt(font_size)
        run.font.bold = bold
        run.font.color.rgb = RGBColor(0, 0, 0)

def set_cover_data(table, doc_title, rubric="2.3"):
    # Row 4: Rubric
    for c in table.rows[4].cells:
        format_cell(c, f"RESULTADO DEL ESTUDIANTE A MEDIR: {rubric}", bold=True, font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    # Row 5: System
    for c in table.rows[5].cells:
        format_cell(c, "SISTEMA DE GESTIÓN INTEGRAL DE SALUD — NEXOVITALIS360 (RUWAYLABS PERÚ)", bold=True, font_size=11, align=WD_ALIGN_PARAGRAPH.CENTER)
    # Row 6: Title
    for c in table.rows[6].cells:
        format_cell(c, doc_title, bold=True, font_size=13, align=WD_ALIGN_PARAGRAPH.CENTER)
    # Row 7: Version
    for c in table.rows[7].cells:
        format_cell(c, "VERSIÓN V01.00", bold=True, font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    # Row 11: Header Integrantes
    for c in table.rows[11].cells:
        format_cell(c, "INTEGRANTES", bold=True, font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    # Rows 13-16: Members
    for idx, (m1, m2) in enumerate(MEMBERS):
        row = table.rows[13 + idx]
        format_cell(row.cells[0], m1, bold=False, font_size=9)
        format_cell(row.cells[1], m2, bold=False, font_size=9)
    # Row 22: Date
    for c in table.rows[22].cells:
        format_cell(c, "NOVIEMBRE 2026", bold=True, font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER)
    # Row 23: City
    for c in table.rows[23].cells:
        format_cell(c, "AREQUIPA — PERÚ", bold=True, font_size=10, align=WD_ALIGN_PARAGRAPH.CENTER)

def set_revision_tables(table_rev, table_ver, doc_type_name):
    # Table 1: Historial de Revisiones
    # Row 2 is headers: FECHA, OBSERVACIONES, VERSIÓN, NOTA, V°B°
    r1 = table_rev.add_row()
    format_cell(r1.cells[0], "01/11/2026", font_size=8.5)
    format_cell(r1.cells[1], f"Formulación inicial del modelo de {doc_type_name} y sincronización con el Catálogo de Requisitos.", font_size=8.5)
    format_cell(r1.cells[2], "v00.10", font_size=8.5)
    format_cell(r1.cells[3], "", font_size=8.5)
    format_cell(r1.cells[4], "En revisión", font_size=8.5)

    r2 = table_rev.add_row()
    format_cell(r2.cells[0], "08/11/2026", font_size=8.5)
    format_cell(r2.cells[1], f"Consolidación definitiva de {doc_type_name} para el Hito 3 / Fase 1, sincronizada con RNF-0026 y RNF-0027, e inclusión de diagramas vectoriales oficiales a 300 DPI.", font_size=8.5)
    format_cell(r2.cells[2], "v01.00", font_size=8.5)
    format_cell(r2.cells[3], "20", font_size=8.5)
    format_cell(r2.cells[4], "Aprobado", font_size=8.5)

    # Table 2: Historial de Versiones
    # Row 2 is headers: FECHA, VERSIÓN, DESCRIPCIÓN, AUTORES
    rv1 = table_ver.add_row()
    format_cell(rv1.cells[0], "01/11/2026", font_size=8.5)
    format_cell(rv1.cells[1], "v00.10", font_size=8.5)
    format_cell(rv1.cells[2], f"Borrador conceptual del artefacto de {doc_type_name}.", font_size=8.5)
    format_cell(rv1.cells[3], "Subgrupo Responsable RuwayLabs", font_size=8.5)

    rv2 = table_ver.add_row()
    format_cell(rv2.cells[0], "08/11/2026", font_size=8.5)
    format_cell(rv2.cells[1], "v01.00", font_size=8.5)
    format_cell(rv2.cells[2], f"Especificación arquitectónica formal de {doc_type_name} aprobada en Acta de Trabajo N° 06.", font_size=8.5)
    format_cell(rv2.cells[3], "Marquez H. Marco (Líder) y Equipo RuwayLabs", font_size=8.5)

def add_heading_1(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(12)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_heading_2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(10.5)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_body_p(doc, text, bold_prefix=None, italic=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Arial'
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(9.5)
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_bullet_p(doc, text, bold_prefix=None):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    r_bullet = p.add_run("• ")
    r_bullet.font.name = 'Arial'
    r_bullet.font.size = Pt(9.5)
    r_bullet.font.bold = True
    r_bullet.font.color.rgb = RGBColor(0, 0, 0)
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = 'Arial'
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 0, 0)
    run = p.add_run(text)
    run.font.name = 'Arial'
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p

def add_figure_image(doc, img_path, caption_text):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(10)
        p_img.paragraph_format.space_after = Pt(4)
        run = p_img.add_run()
        run.add_picture(img_path, width=Inches(6.2))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        r_cap = p_cap.add_run(caption_text)
        r_cap.font.name = 'Arial'
        r_cap.font.size = Pt(8.5)
        r_cap.font.bold = True
        r_cap.font.italic = True
        r_cap.font.color.rgb = RGBColor(50, 50, 50)
    else:
        print(f"Advertencia: No existe imagen {img_path}")

print("Módulo generador de plantillas inicializado.")

def clean_paragraphs_after_table(doc, start_idx=23):
    # Remueve párrafos plantilla de guía para reemplazarlos con la redacción formal
    for p in list(doc.paragraphs[start_idx:]):
        p_elem = p._element
        p_elem.getparent().remove(p_elem)

def build_plantilla_6():
    template_path = "Material del curso/Plantillas/6. Plantilla Arquitectura centrada en datos.docx"
    output_docx = "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/06_Arquitectura_Centrada_Datos/Plantilla_6_Arquitectura_Centrada_Datos_v01.00.docx"
    doc = docx.Document(template_path)
    
    # Portada y revisiones
    set_cover_data(doc.tables[0], "ARQUITECTURA CENTRADA EN DATOS", rubric="2.3")
    set_revision_tables(doc.tables[1], doc.tables[2], "Arquitectura Centrada en Datos")
    
    # Limpiar contenido guía
    clean_paragraphs_after_table(doc, start_idx=22)
    
    # 1. DESCRIPCIÓN DEL TEMA A TRATAR
    add_heading_1(doc, "1. DESCRIPCIÓN DEL TEMA A TRATAR")
    add_heading_2(doc, "1.1. Fundamentación Conceptual de la Arquitectura Centrada en Datos")
    add_body_p(doc, "Dentro de los estilos de arquitectura de software para sistemas complejos (Lixin Tao, Software Architecture Illuminated, Diapositivas 67–70), los estilos centrados en datos sitúan un almacén central de información estructurada en el núcleo de la solución, en torno al cual orbitan múltiples componentes de procesamiento activos o clientes independientes. En concordancia con los principios impartidos por el docente M.Sc. Percy Oscar Huertas Niquén, la arquitectura de datos no debe concebirse como un mero modelo relacional estático, sino como la columna vertebral que gobierna el sostenimiento, la integridad transaccional y la capacidad de respuesta oportuna ante eventos críticos del negocio.")
    add_body_p(doc, "En la ingeniería de sistemas asistenciales modernos se distinguen dos variantes fundamentales del estilo centrado en datos, ambas adoptadas formalmente en el diseño de NexoVitalis360:")
    add_bullet_p(doc, " Estilo en el cual los clientes o subsistemas del backend actúan de manera activa e independiente, ejecutando transacciones atómicas sobre un almacén pasivo (PostgreSQL 16) que asegura propiedades ACID y preserva la inmutabilidad de los expedientes médicos.", bold_prefix="a) Estilo de Repositorio Centralizado (Pasivo):")
    add_bullet_p(doc, " Estilo en el cual el almacén de datos (Pizarra) actúa como una memoria de trabajo compartida y activa. Múltiples Fuentes de Conocimiento (Knowledge Sources - KS) autónomas y especializadas cooperan de forma oportunista y heurística para resolver problemas de diagnóstico clínico complejo (pre-triaje pediátrico, cribado neuroconductual y alertamiento vital) coordinadas por un módulo de control central.", bold_prefix="b) Estilo de Pizarra (Blackboard Architecture):")

    add_heading_2(doc, "1.2. Contexto Funcional del Sistema NexoVitalis360")
    add_body_p(doc, "El sistema NexoVitalis360, desarrollado por la consultora de ingeniería RuwayLabs Perú, tiene por misión la gestión integral de salud pediátrica y teleconsulta especializada. El universo de persistencia abarca veintisiete (27) educciones activas (EDU-0008 a EDU-0038) y ciento ocho (108) operaciones de ilación. La arquitectura de datos centraliza los expedientes clínicos electrónicos, la facturación electrónica bajo normativa SUNAT UBL 2.1, la agenda médica y el seguimiento continuo de pacientes en una topología robusta denominada Vitalis_BD.")

    add_heading_2(doc, "1.3. Alcance y Delimitación Estricta")
    add_body_p(doc, "El alcance de este artefacto se fundamenta en los requerimientos del Catálogo Oficial v01.00: RNF-0003 (Disponibilidad y Recuperación ante Desastres), RNF-0004 (Bloqueo Pesimista Anticolisión de Horarios), RNF-0006 (Seguridad de Datos Cifrados en Tránsito y Reposo), RNF-0016 (Persistencia y Rendimiento del Motor Relacional), RNF-0021 (Auditoría Inmutable Temporal) y el recientemente incorporado RNF-0027 (Arquitectura de Pizarra para Soporte de Decisiones Clínicas).")

    # 2. METODOLOGÍA DEL PROCESO
    add_heading_1(doc, "2. METODOLOGÍA DEL PROCESO Y SU RELACIÓN CON LA METODOLOGÍA PROPUESTA")
    add_body_p(doc, "La construcción de la Arquitectura Centrada en Datos de NexoVitalis360 se articula mediante una metodología de ingeniería de datos orientada a misión crítica, estructurada en cinco etapas trazables:")
    add_bullet_p(doc, " Se analizaron los flujos transaccionales de las 27 educciones para identificar las entidades de alta concurrencia (turnos médicos y pre-triajes), definiendo niveles de aislamiento transaccional READ COMMITTED y bloqueos SELECT ... FOR UPDATE.", bold_prefix="Etapa 1 — Análisis Transaccional y Concurrencia:")
    add_bullet_p(doc, " Se diseñó el almacén relacional Vitalis_BD en PostgreSQL 16 desacoplado mediante el connection pooler PgBouncer, complementado con MinIO Object Storage para la gestión de actas de consentimiento informado y recetas médicas en formato PDF.", bold_prefix="Etapa 2 — Topología de Repositorio Central Pasivo:")
    add_bullet_p(doc, " Se modeló la estructura de Pizarra clínica inspirada en el modelo canónico de Barbara Hayes-Roth (1985), definiendo tres niveles de abstracción de datos compartidos, cuatro fuentes de conocimiento autónomas y un planificador heurístico de ejecución.", bold_prefix="Etapa 3 — Modelado del Estilo Pizarra (Blackboard):")
    add_bullet_p(doc, " Se estructuró el esquema audit_logs con particionamiento mensual por rango, garantizando almacenamiento inmutable y trazabilidad forense de cada operación asistencial durante un lapso de 5 años.", bold_prefix="Etapa 4 — Estrategia de Auditoría y Sharding:")
    add_bullet_p(doc, " Aplicación del protocolo colegiado de rotación y revisión entre subgrupos de trabajo, formalizado en el Acta de Trabajo N° 06.", bold_prefix="Etapa 5 — Giro de Vistas y Validación Colegiada:")

    # 3. ACTAS DE TRABAJO
    add_heading_1(doc, "3. ACTAS DE TRABAJO")
    add_body_p(doc, "En estricto cumplimiento del esquema de gobernanza del curso, la formulación y validación de la Arquitectura Centrada en Datos se encuentra formalizada en el Acta de Trabajo N° 06 (Semana 1 / Hito 3), suscrita por la totalidad de los 8 integrantes del equipo con firmas manuscritas digitalizadas. Dicha acta aprueba la inclusión del requisito RNF-0027 y la adopción dual de los estilos de Repositorio y Pizarra.")

    # 4. ESTADO DEL ARTE
    add_heading_1(doc, "4. ESTADO DEL ARTE")
    add_body_p(doc, "En el ámbito de la ingeniería de software para telemedicina y salud digital, el tratamiento de los datos ha evolucionado sustancialmente:")
    add_bullet_p(doc, " Hayes-Roth (1985) en 'A Blackboard Architecture for Control' y Lixin Tao (2010) destacan que los sistemas que requieren interpretación sensorial y diagnóstico colaborativo no determinista encuentran en la arquitectura de pizarra la única solución capaz de desacoplar el razonamiento experto de los componentes de adquisición de datos.", bold_prefix="Arquitecturas de Pizarra en Salud:")
    add_bullet_p(doc, " Martin Fowler (2002) en 'Patterns of Enterprise Application Architecture' y el estándar HL7 FHIR (Fast Healthcare Interoperability Resources) establecen que la coexistencia de bases de datos relacionales ACID para la auditoría financiera/clínica junto con almacenamiento de objetos binarios cifrados es el estándar de oro en bioinformática clínica.", bold_prefix="Persistencia Híbrida y Almacenes de Objetos:")

    # 5. DESCRIPCIÓN DEL ARTEFACTO
    add_heading_1(doc, "5. DESCRIPCIÓN DEL ARTEFACTO")
    add_heading_2(doc, "5.1. Estilo de Repositorio Centralizado (Vitalis_BD en PostgreSQL 16)")
    add_body_p(doc, "El primer componente de la arquitectura centrada en datos materializa el estilo de Repositorio Pasivo. El almacén central Vitalis_BD opera bajo PostgreSQL 16 Enterprise, administrando las tablas nucleares del dominio clínico pediátrico. Con el fin de mitigar la saturación de conexiones durante picos de concurrencia en teleconsulta, se incorpora un Connection Pooler PgBouncer configurado en modo transacción (pool_size=50, max_client_conn=1000).")
    add_body_p(doc, "Los archivos de gran volumen (actas de consentimiento informado firmadas digitalmente, recetas médicas y comprobantes electrónicos PDF) se segregan hacia el clúster MinIO Object Storage (compatible con AWS S3), registrando en la base de datos únicamente metadatos y URIs canónicas encriptadas.")
    add_figure_image(doc, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/06_Arquitectura_Centrada_Datos/Figura_6_1_Arquitectura_Repositorio_Datos_v01.00.png", "Figura 6.1: Arquitectura Centrada en Datos — Estilo Repositorio Centralizado (Vitalis_BD en PostgreSQL 16 con PgBouncer y MinIO).")

    add_heading_2(doc, "5.2. Estilo de Pizarra / Blackboard (Pre-Triaje Clínico y Alerta Roja)")
    add_body_p(doc, "En estricta correspondencia con la Diapositiva 70 del curso (Blackboard Architecture) y el requisito RNF-0027, el segundo componente de la arquitectura de datos implementa el patrón Pizarra para el soporte a decisiones clínicas en tiempo real:")
    add_bullet_p(doc, " Estructurada en tres niveles jerárquicos de resolución: Nivel 1 (Datos Crudos de Constantes Vitales y Cuestionario TEA/TDAH), Nivel 2 (Hipótesis Clínicas y Probabilidades de Riesgo) y Nivel 3 (Decisión Asistencial y Clasificación Manchester/ESI I–V).", bold_prefix="1. Pizarra de Estado (Blackboard Data Store):")
    add_bullet_p(doc, " Módulos autónomos e independientes: KS-01 (Analizador de Signos Vitales SpO2 y FC Pediátrica), KS-02 (Evaluador Heurístico de Patrones de Neurodesarrollo TEA/TDAH), KS-03 (Validador de Reglas Bioéticas y Consentimiento de Apoderado) y KS-04 (Gestor de Disponibilidad de Especialistas de Guardia).", bold_prefix="2. Fuentes de Conocimiento (Knowledge Sources - KS):")
    add_bullet_p(doc, " Monitoriza las mutaciones de la pizarra, resuelve prioridades mediante colas heurísticas y, ante la presencia de parámetros de riesgo vital inminente (SpO2 < 92%), interrumpe el ciclo habitual y dispara el despacho prioritario de Alerta Roja en menos de 2.0 segundos hacia el médico y la central de ambulancias.", bold_prefix="3. Módulo de Control Heurístico y Despachador de Alertas:")
    add_figure_image(doc, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/06_Arquitectura_Centrada_Datos/Figura_6_2_Arquitectura_Pizarra_Clinica_v01.00.png", "Figura 6.2: Arquitectura Centrada en Datos — Estilo Pizarra / Blackboard para Pre-Triaje Clínico y Alerta Roja.")

    # 6. CONCLUSIONES
    add_heading_1(doc, "6. CONCLUSIONES")
    add_heading_2(doc, "Del Marco Conceptual")
    add_body_p(doc, "La articulación simultánea del estilo de Repositorio Centralizado y el estilo de Pizarra (Blackboard) demuestra que los patrones de arquitectura de datos no son mutuamente excluyentes, sino sinérgicos. Mientras que el repositorio pasivo garantiza la rigidez transaccional ACID requerida para reservas y facturación SUNAT, la pizarra provee la flexibilidad cognitiva indispensable para resolver triajes médicos mediante agentes autónomos.")
    add_heading_2(doc, "Del Producto")
    add_body_p(doc, "Para NexoVitalis360, esta arquitectura garantiza alta disponibilidad, aislamiento ante colisiones en reservas médicas y capacidad de respuesta sub-segundo ante emergencias críticas pediátricas, salvaguardando la vida del menor y la trazabilidad legal del acto médico.")

    # 7. OBSERVACIONES
    add_heading_1(doc, "7. OBSERVACIONES")
    add_body_p(doc, "1. Se recomienda dimensionar el pool de PgBouncer monitoreando las métricas de latencia de consulta durante los horarios pico de teleconsulta (08:00 a 11:00 hrs).")
    add_body_p(doc, "2. Las heurísticas del evaluador KS-02 para cribado de TEA y TDAH deben ser revalidadas periódicamente con el comité médico especializado de la clínica conforme a las guías clínicas del MINSA.")

    # 8. BIBLIOGRAFÍA
    add_heading_1(doc, "8. BIBLIOGRAFÍA")
    add_body_p(doc, "[1] B. Hayes-Roth, 'A Blackboard Architecture for Control', Artificial Intelligence, vol. 26, no. 3, pp. 251-321, 1985.")
    add_body_p(doc, "[2] L. Tao, Software Architecture Illuminated, Jones & Bartlett Learning, 2010.")
    add_body_p(doc, "[3] P. Kruchten, 'Architectural Blueprints—The '4+1' View Model of Software Architecture', IEEE Software, vol. 12, no. 6, pp. 42-50, 1995.")
    add_body_p(doc, "[4] M. Fowler, Patterns of Enterprise Application Architecture, Addison-Wesley, 2002.")
    add_body_p(doc, "[5] ISO/IEC/IEEE 42010:2011, 'Systems and software engineering — Architecture description', ISO/IEC/IEEE, 2011.")
    add_body_p(doc, "[6] HL7 International, 'HL7 Fast Healthcare Interoperability Resources (FHIR) Release 4B', 2022.")

    # 9. ANEXOS
    add_heading_1(doc, "9. ANEXOS")
    add_body_p(doc, "Anexo 1: Matriz de Trazabilidad entre Requisitos del Catálogo v01.00 y los Componentes de Arquitectura Centrada en Datos (Vitalis_BD, PgBouncer, MinIO y Fuentes de Conocimiento de Pizarra KS-01 a KS-04).")

    doc.save(output_docx)
    print(f"Documento generado: {output_docx}")
    
    # Compilar a PDF
    pdf_cmd = f"libreoffice --headless --convert-to pdf '{output_docx}' --outdir '05_DIAGRAMAS_Y_RECURSOS_EDITABLES/06_Arquitectura_Centrada_Datos/'"
    subprocess.run(pdf_cmd, shell=True, check=True)
    print("PDF compilado exitosamente para Plantilla 6.")

def build_plantilla_7():
    template_path = "Material del curso/Plantillas/7. Plantilla GUIS.docx"
    output_docx = "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/07_GUIs_Interfaces/Plantilla_7_GUIs_Interfaces_v01.00.docx"
    doc = docx.Document(template_path)
    
    # Portada y revisiones
    set_cover_data(doc.tables[0], "ARQUITECTURA CENTRADA EN INTERFACES DE USUARIO (GUIS)", rubric="8.2")
    set_revision_tables(doc.tables[1], doc.tables[2], "Arquitectura Centrada en GUIs")
    
    # Limpiar contenido guía
    clean_paragraphs_after_table(doc, start_idx=22)
    
    # 1. DESCRIPCIÓN DEL TEMA A TRATAR
    add_heading_1(doc, "1. DESCRIPCIÓN DEL TEMA A TRATAR")
    add_heading_2(doc, "1.1. Fundamentación Conceptual de la Arquitectura de Interfaces de Usuario")
    add_body_p(doc, "La Arquitectura Centrada en Interfaces de Usuario (GUIs) modela la topología de navegación, la jerarquía visual de accesos y la semántica de interacción entre los usuarios humanos y los servicios computacionales del sistema. Conforme a la doctrina de cátedra del M.Sc. Percy Oscar Huertas Niquén, la arquitectura de pantallas no es un boceto cosmético para el cliente, sino una especificación técnica rigurosa destinada al equipo de codificadores y maquetadores de frontend (React 18 / TypeScript / Vite / PWA). Su propósito es definir sin ambigüedades qué pantallas existen, cómo se accede a ellas, qué modales bloquean o guían el flujo transaccional y cómo se previene el error operativo en contextos de alta exigencia médica.")
    add_body_p(doc, "El diseño de interfaces de NexoVitalis360 se cimenta en tres pilares teóricos consolidados:")
    add_bullet_p(doc, " Visibilidad del estado del sistema, correspondencia con el mundo clínico, control y libertad del usuario, consistencia terminológica y prevención de errores.", bold_prefix="a) Las 10 Heurísticas de Usabilidad de Jakob Nielsen:")
    add_bullet_p(doc, " Retroalimentación informativa inmediata, diseño de diálogos que cierran operaciones, reversión sencilla de acciones y reducción sustancial de la carga cognitiva en memoria a corto plazo.", bold_prefix="b) Las 8 Reglas de Oro de Ben Shneiderman:")
    add_bullet_p(doc, " Señalética evidente de interacción, mapeo natural de controles clínicos y diseño indulgente.", bold_prefix="c) Principios de Affordance y Manejo del Error de Donald Norman:")

    add_heading_2(doc, "1.2. Contexto Funcional y Segregación de Roles (RBAC)")
    add_body_p(doc, "El sistema NexoVitalis360 implementa un control de acceso basado en roles (RBAC) que segrega de manera estricta la interfaz en tres portales de interacción independientes, además de una sala de teleconsulta transversal:")
    add_bullet_p(doc, " Optimizado para accesibilidad desde smartphones y tablets (PWA), con flujos simplificados para reserva de citas, pago digital y consulta de recetas médicas.", bold_prefix="1. Portal del Tutor Legal / Apoderado (/app/tutor/*):")
    add_bullet_p(doc, " Estación de trabajo médica para escritorio con acceso rápido a agenda, historial clínico pediátrico, editor CIE-10/CIE-11 y prescripción electrónica con firma digital.", bold_prefix="2. Estación Profesional de Salud (/app/medico/*):")
    add_bullet_p(doc, " Consola de gobernanza, alta de especialistas, gestión de tarifas, monitoreo de sesiones y reportes consolidados.", bold_prefix="3. Consola de Administración (/app/admin/*):")
    add_bullet_p(doc, " Entorno WebRTC interactivo de alta definición con telemetría en vivo y botón no descartable de disparo de Alerta Roja.", bold_prefix="4. Sala de Teleconsulta y Alerta Roja (/app/teleconsulta/:id):")

    add_heading_2(doc, "1.3. Alcance y Delimitación")
    add_body_p(doc, "Este documento cubre la totalidad de interfaces derivadas de las 27 educciones del catálogo y responde directamente a RNF-0018 (Usabilidad y Accesibilidad WCAG 2.1 AA) y RNF-0026 (Perfil de Competencias del Equipo de Codificadores Frontend).")

    # 2. METODOLOGÍA DEL PROCESO
    add_heading_1(doc, "2. METODOLOGÍA DEL PROCESO Y SU RELACIÓN CON LA METODOLOGÍA PROPUESTA")
    add_body_p(doc, "El modelado arquitectónico de las GUIs se ejecutó en cuatro fases correlativas:")
    add_bullet_p(doc, " Se asignó a cada una de las 108 ilaciones operativas del catálogo su pantalla receptora o modal interactivo correspondiente.", bold_prefix="Fase 1 — Mapeo de Educciones a Vistas:")
    add_bullet_p(doc, " Se estructuró el árbol jerárquico de rutas protegido por guardas de seguridad de frontend (AuthGuard y RoleGuard).", bold_prefix="Fase 2 — Jerarquización del Árbol de Navegación:")
    add_bullet_p(doc, " Se diseñó el comportamiento de los diálogos modales críticos (horarios, consentimiento informado, pre-triaje, alerta roja y facturación).", bold_prefix="Fase 3 — Modelado de Modales Bloqueantes y Microinteracciones:")
    add_bullet_p(doc, " Verificación de contraste cromático, navegación completa por teclado y confirmación unánime en el Acta de Trabajo N° 06.", bold_prefix="Fase 4 — Auditoría de Accesibilidad y Aprobación Colegiada:")

    # 3. ACTAS DE TRABAJO
    add_heading_1(doc, "3. ACTAS DE TRABAJO")
    add_body_p(doc, "La concepción de la arquitectura de GUIs y su nivel de detalle para el equipo de codificación fue analizada y ratificada en el Acta de Trabajo N° 06, donde se asentó formalmente la política de diseño para programadores junior y de nivel intermedio establecida por el docente.")

    # 4. ESTADO DEL ARTE
    add_heading_1(doc, "4. ESTADO DEL ARTE")
    add_body_p(doc, "En el diseño de sistemas de salud asistenciales, la interfaz de usuario es considerada un componente de seguridad del paciente:")
    add_bullet_p(doc, " La Healthcare Information and Management Systems Society (HIMSS) y la normativa ISO 9241-210 establecen que el 70% de errores de prescripción y agendamiento clínico son atribuibles a interfaces sobrecargadas y ausencia de modales confirmatorios.", bold_prefix="Seguridad Clínica en GUIs:")
    add_bullet_p(doc, " Las guías WCAG 2.1 Nivel AA determinan estándares mandatorios de contraste cromático (mínimo 4.5:1), áreas táctiles mínimas de 48x48 px y legibilidad inequívoca para usuarios apoderados en situaciones de estrés.", bold_prefix="Accesibilidad Universal:")

    # 5. DESCRIPCIÓN DEL ARTEFACTO
    add_heading_1(doc, "5. DESCRIPCIÓN DEL ARTEFACTO")
    add_heading_2(doc, "5.1. Árbol de Navegación Jerárquico por Roles (RBAC)")
    add_body_p(doc, "La Figura 7.1 ilustra la arquitectura de rutas y vistas de la aplicación. Se observa el layout maestro compartido que aloja los elementos perimetrales (barra de estado, notificaciones de telemetría y cabecera de autenticación), ramificándose en los tres dominios protegidos:")
    add_figure_image(doc, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/07_GUIs_Interfaces/Figura_7_1_Arbol_Navegacion_Roles_v01.00.png", "Figura 7.1: GUIs e Interfaces — Árbol de Navegación Jerárquico por Roles (RBAC).")

    add_heading_2(doc, "5.2. Flujo de Interacción y Gestión de Modales Clínicos")
    add_body_p(doc, "La Figura 7.2 modela el comportamiento operacional dinámico de la interfaz, detallando las transiciones de pantalla y la intervención de modales bloqueantes:")
    add_bullet_p(doc, " Valida la disponibilidad de turnos en tiempo real mediante WebSockets, evitando el agendamiento duplicado antes de solicitar confirmación.", bold_prefix="1. Modal de Selección de Horarios:")
    add_bullet_p(doc, " Bloqueo legal estricto que exige firma digital o aceptación explícita del apoderado antes de autorizar cualquier consulta pediátrica.", bold_prefix="2. Modal de Consentimiento Informado:")
    add_bullet_p(doc, " Captura guiada de constantes vitales con validación inmediata en cliente para alertamiento temprano.", bold_prefix="3. Formulario de Pre-Triaje Reactivo:")
    add_bullet_p(doc, " Modal no descartable de máxima prioridad visual y auditiva, activado ante descompensación del menor, que establece enlace WebRTC inmediato y despacho de llamada de urgencia.", bold_prefix="4. Modal Crítico de Alerta Roja:")
    add_bullet_p(doc, " Integración transaccional con pasarela y despacho síncrono del comprobante electrónico UBL 2.1 con código QR.", bold_prefix="5. Modal de Pasarela y Facturación SUNAT:")
    add_figure_image(doc, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/07_GUIs_Interfaces/Figura_7_2_Flujo_Interfaces_Modales_v01.00.png", "Figura 7.2: GUIs e Interfaces — Flujo de Interacción y Gestión de Modales Clínicos (Nielsen & Shneiderman).")

    # 6. CONCLUSIONES
    add_heading_1(doc, "6. CONCLUSIONES")
    add_heading_2(doc, "Del Marco Conceptual")
    add_body_p(doc, "Modelar la interfaz de usuario con rigor arquitectónico permite alinear la experiencia humana con las capacidades de la infraestructura backend, garantizando que cada pantalla cumpla una función transaccional concreta y respete los principios de indulgencia ante errores de Nielsen y Shneiderman.")
    add_heading_2(doc, "Del Producto")
    add_body_p(doc, "La granularidad provista en el árbol y los flujos de modales proporciona a los desarrolladores de frontend una guía exacta para maquetar componentes React 18 / Tailwind CSS sin margen de error, salvaguardando la integridad clínica del paciente pediátrico.")

    # 7. OBSERVACIONES
    add_heading_1(doc, "7. OBSERVACIONES")
    add_body_p(doc, "1. En la PWA para apoderados, se debe verificar que el modal de Alerta Roja cuente con vibración háptica y sonido de alarma pre-cargado en caché local para operar aún ante caídas parciales de señal.")
    add_body_p(doc, "2. Es indispensable realizar pruebas de usabilidad con profesionales de salud reales para optimizar la velocidad de tipeo de diagnósticos CIE-10 mediante atajos de teclado.")

    # 8. BIBLIOGRAFÍA
    add_heading_1(doc, "8. BIBLIOGRAFÍA")
    add_body_p(doc, "[1] B. Shneiderman, C. Plaisant, M. Cohen, S. Jacobs, N. Elmqvist, and N. Diakopoulos, Designing the User Interface: Strategies for Effective Human-Computer Interaction, 6th ed., Pearson, 2016.")
    add_body_p(doc, "[2] J. Nielsen, 'Usability Inspection Methods', in Conference Companion on Human Factors in Computing Systems, 1994, pp. 413-414.")
    add_body_p(doc, "[3] D. A. Norman, The Design of Everyday Things: Revised and Expanded Edition, Basic Books, 2013.")
    add_body_p(doc, "[4] W3C, 'Web Content Accessibility Guidelines (WCAG) 2.1', W3C Recommendation, 2018.")
    add_body_p(doc, "[5] ISO 9241-210:2019, 'Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems', ISO, 2019.")

    # 9. ANEXOS
    add_heading_1(doc, "9. ANEXOS")
    add_body_p(doc, "Anexo 1: Catálogo de Pantallas del Frontend y Matriz de Trazabilidad hacia las 27 Educciones del Catálogo de Requisitos v01.00.")

    doc.save(output_docx)
    print(f"Documento generado: {output_docx}")
    
    # Compilar a PDF
    pdf_cmd = f"libreoffice --headless --convert-to pdf '{output_docx}' --outdir '05_DIAGRAMAS_Y_RECURSOS_EDITABLES/07_GUIs_Interfaces/'"
    subprocess.run(pdf_cmd, shell=True, check=True)
    print("PDF compilado exitosamente para Plantilla 7.")

if __name__ == "__main__":
    print("Iniciando generación de Plantilla 6 y Plantilla 7...")
    build_plantilla_6()
    build_plantilla_7()
    print("¡Generación y compilación culminadas exitosamente!")

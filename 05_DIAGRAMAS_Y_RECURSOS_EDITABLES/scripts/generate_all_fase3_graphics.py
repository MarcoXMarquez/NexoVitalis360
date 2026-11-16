#!/usr/bin/env python3
"""
generate_all_fase3_graphics.py
Construye los 4 diagramas vectoriales oficiales SVG y sus versiones interactivas HTML5 y PNG (300 DPI)
para la Fase 3 del proyecto NexoVitalis360.
"""

import os
import subprocess
from build_fase3_diagrams import create_interactive_html

BASE_DIR = "/home/marco/Projects/NexoVitalis360"
DIR_GUIS = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/07_GUIs_Interfaces")
DIR_DATOS = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/06_Arquitectura_Centrada_Datos")

# ==============================================================================
# 1. FIGURA 7.1: ÁRBOL DE NAVEGACIÓN Y MAPA DE SITIO GLOBAL POR ROLES
# ==============================================================================
def build_svg_fig7_1():
    w, h = 2400, 1400
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Fondo Blanco -->
  <rect width="{w}" height="{h}" fill="#ffffff" />

  <!-- Encabezado Institucional -->
  <rect x="50" y="30" width="2300" height="90" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <text x="70" y="65" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#000000">NEXOVITALIS360 — ARQUITECTURA CENTRADA EN INTERFACES DE USUARIO (PLANTILLA 7)</text>
  <text x="70" y="98" font-family="Arial, sans-serif" font-size="16" fill="#333333">FIGURA 7.1: ÁRBOL DE NAVEGACIÓN Y MAPA DE SITIO GLOBAL POR ROLES DE USUARIO (ESPECIALISTA, RECEPCIÓN, APODERADO)</text>
  <text x="2150" y="80" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000">ESTÁNDAR W3C / ISO 25010</text>

  <!-- Nodo Raíz: Portal Principal -->
  <rect x="950" y="150" width="500" height="70" fill="#000000" stroke="#000000" stroke-width="2" />
  <text x="1200" y="180" font-family="Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">SISTEMA HOSPITALARIO NEXOVITALIS360</text>
  <text x="1200" y="202" font-family="Courier, monospace" font-size="13" fill="#ffffff" text-anchor="middle">https://vitalis360.clinica.pe/ [Autenticación JWT / RBAC]</text>

  <!-- Conectores Troncales hacia los 3 Roles -->
  <path d="M 1200 220 L 1200 250" stroke="#000000" stroke-width="2.5" />
  <path d="M 400 250 L 2000 250" stroke="#000000" stroke-width="2.5" />
  <path d="M 400 250 L 400 290" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow)" />
  <path d="M 1200 250 L 1200 290" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow)" />
  <path d="M 2000 250 L 2000 290" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow)" />

  <!-- =========================================================================
       RAMA 1: PORTAL DEL ESPECIALISTA (X: 80 - 720)
       ========================================================================= -->
  <rect x="80" y="290" width="640" height="70" fill="#f4f4f4" stroke="#000000" stroke-width="2.5" />
  <text x="400" y="320" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">ROL: MÉDICO ESPECIALISTA / NEUROPEDIATRA</text>
  <text x="400" y="342" font-family="Courier, monospace" font-size="13" fill="#000000" text-anchor="middle">Ruta Base: /portal-especialista/* [MFA / Token Bearer]</text>

  <!-- Bus Vertical Rama 1 -->
  <path d="M 140 360 L 140 1200" stroke="#000000" stroke-width="2" />

  <!-- Submódulos Rama 1 -->
  <!-- 1. Dashboard -->
  <path d="M 140 400 L 180 400" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="180" y="375" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="195" y="398" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-ESP-01: Dashboard del Especialista (/dashboard)</text>
  <text x="195" y="416" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Métricas del día, pacientes citados, alertas pendientes y teleconsultas en cola.</text>

  <!-- 2. Agenda y Turnos -->
  <path d="M 140 470 L 180 470" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="180" y="445" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="195" y="468" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-ESP-02: Agenda Semanal y Turnos (/agenda)</text>
  <text x="195" y="486" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Disponibilidad en consultorio, franjas WebRTC y bloqueo de horarios.</text>

  <!-- 3. Consulta Presencial -->
  <path d="M 140 540 L 180 540" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="180" y="515" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="195" y="538" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-ESP-03: Sala de Consulta Presencial (/atencion/presencial)</text>
  <text x="195" y="556" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Recepción física, validación de constantes vitales y pre-triaje.</text>

  <!-- 4. Teleconsulta WebRTC -->
  <path d="M 140 610 L 180 610" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="180" y="585" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="195" y="608" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-ESP-04: Sala de Teleconsulta WebRTC (/atencion/teleconsulta)</text>
  <text x="195" y="626" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Videollamada Google Meet integrada, chat cifrado y pizarra compartida.</text>

  <!-- 5. Historia Clínica -->
  <path d="M 140 680 L 180 680" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="180" y="655" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="195" y="678" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-ESP-05: Historia Clínica Pediátrica (/historia-clinica/:id)</text>
  <text x="195" y="696" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Evolución médica, antecedentes perinatales, hitos y escalas neurodivergentes.</text>

  <!-- Modales Rama 1 -->
  <path d="M 360 705 L 360 735" stroke="#000000" stroke-dasharray="3,3" stroke-width="1.5" />
  <rect x="230" y="735" width="470" height="42" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3" />
  <text x="245" y="754" font-family="Arial, sans-serif" font-size="12" font-weight="bold">MDL-ESP-01: Modal Cierre de Historia y Diagnóstico CIE-10</text>
  <text x="245" y="770" font-family="Arial, sans-serif" font-size="11" fill="#555555">Validación de campos obligatorios, CIE-10/DSM-5 y firma digital médica.</text>

  <path d="M 360 777 L 360 805" stroke="#000000" stroke-dasharray="3,3" stroke-width="1.5" />
  <rect x="230" y="805" width="470" height="42" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3" />
  <text x="245" y="824" font-family="Arial, sans-serif" font-size="12" font-weight="bold">MDL-ESP-02: Modal Emisión de Receta Médica Cifrada</text>
  <text x="245" y="840" font-family="Arial, sans-serif" font-size="11" fill="#555555">Dosificación pediátrica en mg/kg, código QR y despacho a MinIO S3.</text>

  <!-- =========================================================================
       RAMA 2: PORTAL DE ADMISIÓN Y RECEPCIÓN (X: 880 - 1520)
       ========================================================================= -->
  <rect x="880" y="290" width="640" height="70" fill="#f4f4f4" stroke="#000000" stroke-width="2.5" />
  <text x="1200" y="320" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">ROL: RECEPCIONISTA / ASISTENTE DE ADMISIÓN</text>
  <text x="1200" y="342" font-family="Courier, monospace" font-size="13" fill="#000000" text-anchor="middle">Ruta Base: /admision-recepcion/* [Session Auth]</text>

  <!-- Bus Vertical Rama 2 -->
  <path d="M 940 360 L 940 1200" stroke="#000000" stroke-width="2" />

  <!-- Submódulos Rama 2 -->
  <!-- 1. Panel de Recepción -->
  <path d="M 940 400 L 980 400" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="980" y="375" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="995" y="398" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-REC-01: Panel de Control de Admisión (/recepcion)</text>
  <text x="995" y="416" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Monitoreo de salas de espera, llegadas de pacientes y check-in asistencial.</text>

  <!-- 2. Agendamiento Multimodal -->
  <path d="M 940 470 L 980 470" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="980" y="445" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="995" y="468" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-REC-02: Bandeja de Agendamiento Multimodal (/citas/nueva)</text>
  <text x="995" y="486" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Selección de canal: presencial, virtual WebRTC o terapeuta a domicilio.</text>

  <!-- Modales Agendamiento -->
  <path d="M 1160 495 L 1160 520" stroke="#000000" stroke-dasharray="3,3" stroke-width="1.5" />
  <rect x="1030" y="520" width="470" height="42" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3" />
  <text x="1045" y="539" font-family="Arial, sans-serif" font-size="12" font-weight="bold">MDL-REC-01: Modal Reserva y Bloqueo Pesimista (SELECT FOR UPDATE)</text>
  <text x="1045" y="555" font-family="Arial, sans-serif" font-size="11" fill="#555555">Bloqueo atómico anticolisión de 10 min en TB_HORARIOS (RNF-0004).</text>

  <!-- 3. Filiación -->
  <path d="M 940 595 L 980 595" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="980" y="570" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="995" y="593" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-REC-03: Filiación del Menor y Apoderado (/pacientes/registro)</text>
  <text x="995" y="611" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Separación jurídica: paciente infante vs. apoderado tutor (TB_APODERADOS).</text>

  <!-- 4. Pre-Triaje Clínico -->
  <path d="M 940 655 L 980 655" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="980" y="630" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="995" y="653" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-REC-04: Módulo de Pre-Triaje y Consentimiento (/triaje)</text>
  <text x="995" y="671" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Captura de SpO2, FC, PA y verificación de consentimiento bioético.</text>

  <!-- Modales Pre-triaje -->
  <path d="M 1160 680 L 1160 705" stroke="#000000" stroke-dasharray="3,3" stroke-width="1.5" />
  <rect x="1030" y="705" width="470" height="42" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3" />
  <text x="1045" y="724" font-family="Arial, sans-serif" font-size="12" font-weight="bold">MDL-REC-02: Modal Alerta Roja Vital Pediátrica (SpO2 &lt; 92%)</text>
  <text x="1045" y="740" font-family="Arial, sans-serif" font-size="11" fill="#555555">Conmutación alerta_roja=true y notificación WebSockets a guardia médica.</text>

  <!-- 5. Caja y Facturación -->
  <path d="M 940 780 L 980 780" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="980" y="755" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="995" y="778" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-REC-05: Módulo de Caja y Facturación SUNAT (/caja)</text>
  <text x="995" y="796" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Liquidación de servicios, venta de paquetes de terapia y emisión de CPEs.</text>

  <!-- Modales Caja -->
  <path d="M 1160 805 L 1160 830" stroke="#000000" stroke-dasharray="3,3" stroke-width="1.5" />
  <rect x="1030" y="830" width="470" height="42" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3" />
  <text x="1045" y="849" font-family="Arial, sans-serif" font-size="12" font-weight="bold">MDL-REC-03: Modal Emisión Boleta/Factura XML UBL 2.1</text>
  <text x="1045" y="865" font-family="Arial, sans-serif" font-size="11" fill="#555555">Validación RUC/DNI, firma X.509, envío a SUNAT y retorno de CDR en &lt;3s.</text>

  <!-- =========================================================================
       RAMA 3: PORTAL MÓVIL DEL APODERADO (X: 1680 - 2320)
       ========================================================================= -->
  <rect x="1680" y="290" width="640" height="70" fill="#f4f4f4" stroke="#000000" stroke-width="2.5" />
  <text x="2000" y="320" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#000000" text-anchor="middle">ROL: APODERADO / TUTOR LEGAL (PWA MÓVIL)</text>
  <text x="2000" y="342" font-family="Courier, monospace" font-size="13" fill="#000000" text-anchor="middle">Ruta Base: /portal-apoderado/* [PWA Android 11+ / iOS 15+]</text>

  <!-- Bus Vertical Rama 3 -->
  <path d="M 1740 360 L 1740 1200" stroke="#000000" stroke-width="2" />

  <!-- Submódulos Rama 3 -->
  <!-- 1. Inicio Móvil -->
  <path d="M 1740 400 L 1780 400" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="1780" y="375" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1795" y="398" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-APO-01: Portal Móvil del Paciente (/apoderado/inicio)</text>
  <text x="1795" y="416" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Ficha del menor, próximas citas y accesos rápidos de atención.</text>

  <!-- 2. Solicitud de Cita -->
  <path d="M 1740 470 L 1780 470" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="1780" y="445" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1795" y="468" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-APO-02: Agendamiento y Reprogramación (/apoderado/citas)</text>
  <text x="1795" y="486" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Calendario interactivo con aplicación de regla de anticipación >= 24h.</text>

  <!-- 3. Sala de Espera Virtual -->
  <path d="M 1740 540 L 1780 540" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="1780" y="515" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1795" y="538" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-APO-03: Sala de Espera de Teleconsulta (/apoderado/telemedicina)</text>
  <text x="1795" y="556" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Cuenta regresiva de turno, prueba de cámara/micrófono y enlace Meet.</text>

  <!-- 4. Consentimiento y Documentos -->
  <path d="M 1740 610 L 1780 610" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <rect x="1780" y="585" width="520" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1795" y="608" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">GUI-APO-04: Documentos Clínicos y Facturas (/apoderado/documentos)</text>
  <text x="1795" y="626" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">Descarga de recetas, actas firmadas y constancias de pago PDF/XML.</text>

  <!-- Modales Apoderado -->
  <path d="M 1960 635 L 1960 660" stroke="#000000" stroke-dasharray="3,3" stroke-width="1.5" />
  <rect x="1830" y="660" width="470" height="42" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="4,3" />
  <text x="1845" y="679" font-family="Arial, sans-serif" font-size="12" font-weight="bold">MDL-APO-01: Modal Firma de Consentimiento Bioético</text>
  <text x="1845" y="695" font-family="Arial, sans-serif" font-size="11" fill="#555555">Lectura de términos, captura de trazabilidad (IP, DNI, Hash SHA-256).</text>

  <!-- =========================================================================
       PIE: CUADRO DE LEYENDA Y CONTROL DE SEGURIDAD
       ========================================================================= -->
  <rect x="80" y="1230" width="2240" height="120" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <text x="100" y="1258" font-family="Arial, sans-serif" font-size="14" font-weight="bold">LEYENDA Y CRITERIOS DE ARQUITECTURA DE INTERFACES (PLANTILLA 7):</text>

  <!-- Elemento 1 -->
  <rect x="100" y="1275" width="30" height="20" fill="#000000" />
  <text x="140" y="1290" font-family="Arial, sans-serif" font-size="12">Portal Raíz / Autenticación Centralizada (JWT)</text>

  <!-- Elemento 2 -->
  <rect x="470" y="1275" width="30" height="20" fill="#f4f4f4" stroke="#000000" stroke-width="1.5" />
  <text x="510" y="1290" font-family="Arial, sans-serif" font-size="12">Rutas Maestras por Rol (RBAC Clínico)</text>

  <!-- Elemento 3 -->
  <rect x="800" y="1275" width="30" height="20" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="840" y="1290" font-family="Arial, sans-serif" font-size="12">Pantallas de Trabajo (GUI-* con layout unificado)</text>

  <!-- Elemento 4 -->
  <rect x="1210" y="1275" width="30" height="20" fill="#fafafa" stroke="#000000" stroke-width="1.5" stroke-dasharray="3,3" />
  <text x="1250" y="1290" font-family="Arial, sans-serif" font-size="12">Modales Flotantes Contextuales (MDL-* sin pérdida de contexto)</text>

  <!-- Elemento 5 -->
  <line x1="1720" y1="1285" x2="1750" y2="1285" stroke="#000000" stroke-width="2" marker-end="url(#arrow)" />
  <text x="1760" y="1290" font-family="Arial, sans-serif" font-size="12">Navegación Jerárquica y Transición de Estados</text>

  <text x="100" y="1330" font-family="Arial, sans-serif" font-size="12" fill="#555555">Cumplimiento Estricto: Heurísticas de Nielsen (Visibilidad, Consistencia, Prevención de Errores) &#8226; 8 Reglas de Oro de Shneiderman &#8226; RNF-0018 / RNF-0026.</text>
</svg>"""
    return svg

# ==============================================================================
# 2. FIGURA 7.2: DIAGRAMA DE FLUJO DE INTERACCIÓN UI, PANTALLAS Y MODALES
# ==============================================================================
def build_svg_fig7_2():
    w, h = 2400, 1400
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <marker id="arrow2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Fondo Blanco -->
  <rect width="{w}" height="{h}" fill="#ffffff" />

  <!-- Encabezado -->
  <rect x="50" y="30" width="2300" height="90" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <text x="70" y="65" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#000000">NEXOVITALIS360 — ARQUITECTURA CENTRADA EN INTERFACES DE USUARIO (PLANTILLA 7)</text>
  <text x="70" y="98" font-family="Arial, sans-serif" font-size="16" fill="#333333">FIGURA 7.2: FLUJO DE INTERACCIÓN DE INTERFACES, PANTALLAS MAESTRAS (GUI) Y MODALES FLOTANTES (MDL)</text>
  <text x="2100" y="80" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000">HEURÍSTICAS DE USABILIDAD</text>

  <!-- =========================================================================
       PASO 1: AGENDAMIENTO Y RESERVA (COLUMNA 1: X: 80 - 480)
       ========================================================================= -->
  <rect x="80" y="160" width="410" height="340" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="80" y="160" width="410" height="40" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="100" y="186" font-family="Arial, sans-serif" font-size="14" font-weight="bold">ETAPA 1: SELECCIÓN DE CITA</text>

  <rect x="100" y="215" width="370" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="115" y="238" font-family="Arial, sans-serif" font-size="13" font-weight="bold">GUI-001: Calendario Multimodal</text>
  <text x="115" y="258" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Filtro por especialidad neuropediátrica</text>
  <text x="115" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Selector de modalidad: Presencial / WebRTC / Domicilio</text>
  <text x="115" y="292" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Grid interactivo de franjas horarias libres</text>

  <!-- Disparador Evento -->
  <path d="M 285 310 L 285 345" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="295" y="333" font-family="Courier, monospace" font-size="11" font-weight="bold">onClick(BTN_SELECCIONAR_TURNO)</text>

  <rect x="100" y="345" width="370" height="130" fill="#fafafa" stroke="#000000" stroke-width="1.8" stroke-dasharray="4,3" />
  <text x="115" y="368" font-family="Arial, sans-serif" font-size="13" font-weight="bold">MDL-001: Modal Bloqueo Pesimista</text>
  <text x="115" y="388" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Timer de retención: 10:00 minutos activos</text>
  <text x="115" y="405" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Bloqueo atómico en BD: SELECT FOR UPDATE</text>
  <text x="115" y="422" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Botón BTN_CONFIRMAR_RESERVA</text>
  <text x="115" y="439" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Botón BTN_CANCELAR (libera franja en TB_HORARIOS)</text>
  <rect x="115" y="450" width="340" height="18" fill="#e8e8e8" />
  <text x="120" y="463" font-family="Arial, sans-serif" font-size="10" font-weight="bold">Heurística Nielsen #1: Visibilidad del Estado (Cuenta Regresiva)</text>

  <!-- Conexión Etapa 1 a Etapa 2 -->
  <path d="M 490 260 L 540 260" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="515" y="250" font-family="Courier, monospace" font-size="11" font-weight="bold" text-anchor="middle">HTTP 200 OK</text>

  <!-- =========================================================================
       PASO 2: PRE-TRIAJE Y ALERTA VITAL (COLUMNA 2: X: 540 - 940)
       ========================================================================= -->
  <rect x="540" y="160" width="410" height="340" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="540" y="160" width="410" height="40" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="560" y="186" font-family="Arial, sans-serif" font-size="14" font-weight="bold">ETAPA 2: PRE-TRIAJE Y BIOÉTICA</text>

  <rect x="560" y="215" width="370" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="575" y="238" font-family="Arial, sans-serif" font-size="13" font-weight="bold">GUI-002: Formulario de Triaje y Consentimiento</text>
  <text x="575" y="258" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Captura de Signos Vitales: SpO2, FC, PA, Temperatura</text>
  <text x="575" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Verificación de Consentimiento Informado Legal</text>
  <text x="575" y="292" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Botón BTN_EVALUAR_SIGNOS_VITALES</text>

  <!-- Disparador Modal -->
  <path d="M 745 310 L 745 345" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="755" y="333" font-family="Courier, monospace" font-size="11" font-weight="bold">onSubmit(EVALUAR)</text>

  <rect x="560" y="345" width="370" height="130" fill="#fafafa" stroke="#000000" stroke-width="1.8" stroke-dasharray="4,3" />
  <text x="575" y="368" font-family="Arial, sans-serif" font-size="13" font-weight="bold">MDL-002: Modal Evaluación de Alerta Roja</text>
  <text x="575" y="388" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Regla Clínica: Si SpO2 &lt; 92% o FC crítica</text>
  <text x="575" y="405" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Interfaz: Banner Parpadeante de Alto Contraste</text>
  <text x="575" y="422" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Disparo WebSockets automático a central médica</text>
  <text x="575" y="439" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Desvío inmediato a módulo de urgencias</text>
  <rect x="575" y="450" width="340" height="18" fill="#e8e8e8" />
  <text x="580" y="463" font-family="Arial, sans-serif" font-size="10" font-weight="bold">Heurística Nielsen #5: Prevención de Errores y RNF-0027</text>

  <!-- Conexión Etapa 2 a Etapa 3 -->
  <path d="M 950 260 L 1000 260" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="975" y="250" font-family="Courier, monospace" font-size="11" font-weight="bold" text-anchor="middle">Triaje OK</text>

  <!-- =========================================================================
       PASO 3: ATENCIÓN CLÍNICA Y CIE-10 (COLUMNA 3: X: 1000 - 1400)
       ========================================================================= -->
  <rect x="1000" y="160" width="410" height="340" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="1000" y="160" width="410" height="40" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="1020" y="186" font-family="Arial, sans-serif" font-size="14" font-weight="bold">ETAPA 3: CONSULTA MÉDICA</text>

  <rect x="1020" y="215" width="370" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="1035" y="238" font-family="Arial, sans-serif" font-size="13" font-weight="bold">GUI-003: Estación de Consulta Médica</text>
  <text x="1035" y="258" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Visor de Historia Clínica Electrónica</text>
  <text x="1035" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Panel de Notas de Evolución en tiempo real</text>
  <text x="1035" y="292" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Enlace Google Meet integrado para teleconsultas</text>

  <!-- Disparador Modal -->
  <path d="M 1205 310 L 1205 345" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="1215" y="333" font-family="Courier, monospace" font-size="11" font-weight="bold">onClick(BTN_FINALIZAR_SESION)</text>

  <rect x="1020" y="345" width="370" height="130" fill="#fafafa" stroke="#000000" stroke-width="1.8" stroke-dasharray="4,3" />
  <text x="1035" y="368" font-family="Arial, sans-serif" font-size="13" font-weight="bold">MDL-003: Modal Diagnóstico CIE-10 y Cierre</text>
  <text x="1035" y="388" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Buscador predictivo de códigos CIE-10 / DSM-5</text>
  <text x="1035" y="405" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Prescripción médica electrónica con posología</text>
  <text x="1035" y="422" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Cierre inmutable de historia clínica</text>
  <text x="1035" y="439" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Descuento automático de sesión de paquete</text>
  <rect x="1035" y="450" width="340" height="18" fill="#e8e8e8" />
  <text x="1040" y="463" font-family="Arial, sans-serif" font-size="10" font-weight="bold">Shneiderman Regla #3: Retroalimentación Informativa</text>

  <!-- Conexión Etapa 3 a Etapa 4 -->
  <path d="M 1410 260 L 1460 260" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="1435" y="250" font-family="Courier, monospace" font-size="11" font-weight="bold" text-anchor="middle">Sesión Fin</text>

  <!-- =========================================================================
       PASO 4: FACTURACIÓN Y LIQUIDACIÓN SUNAT (COLUMNA 4: X: 1460 - 1860)
       ========================================================================= -->
  <rect x="1460" y="160" width="410" height="340" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="1460" y="160" width="410" height="40" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="1480" y="186" font-family="Arial, sans-serif" font-size="14" font-weight="bold">ETAPA 4: FACTURACIÓN SUNAT</text>

  <rect x="1480" y="215" width="370" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="1495" y="238" font-family="Arial, sans-serif" font-size="13" font-weight="bold">GUI-004: Módulo de Caja y Comprobantes</text>
  <text x="1495" y="258" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Resumen de sesión atendida y tarifas</text>
  <text x="1495" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Bifurcación: Boleta (DNI) vs. Factura (RUC)</text>
  <text x="1495" y="292" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Integración de pago: POS, Yape, Tarjeta o Saldo</text>

  <!-- Disparador Modal -->
  <path d="M 1665 310 L 1665 345" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="1675" y="333" font-family="Courier, monospace" font-size="11" font-weight="bold">onClick(BTN_EMITIR_CPE)</text>

  <rect x="1480" y="345" width="370" height="130" fill="#fafafa" stroke="#000000" stroke-width="1.8" stroke-dasharray="4,3" />
  <text x="1495" y="368" font-family="Arial, sans-serif" font-size="13" font-weight="bold">MDL-004: Modal Emisión XML UBL 2.1</text>
  <text x="1495" y="388" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Firma digital criptográfica X.509 en backend</text>
  <text x="1495" y="405" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Transmisión segura mTLS hacia SUNAT/OSE</text>
  <text x="1495" y="422" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Visualizador de CDR con estado APROBADO</text>
  <text x="1495" y="439" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Botón de descarga PDF con código QR y Hash CPE</text>
  <rect x="1495" y="450" width="340" height="18" fill="#e8e8e8" />
  <text x="1500" y="463" font-family="Arial, sans-serif" font-size="10" font-weight="bold">Heurística Nielsen #9: Ayudar a Reconocer Errores (RNF-0023)</text>

  <!-- =========================================================================
       PASO 5: EXPERIENCIA MÓVIL DEL APODERADO (COLUMNA 5: X: 1920 - 2320)
       ========================================================================= -->
  <rect x="1920" y="160" width="400" height="340" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="1920" y="160" width="400" height="40" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="1940" y="186" font-family="Arial, sans-serif" font-size="14" font-weight="bold">ETAPA 5: PORTAL APODERADO</text>

  <rect x="1940" y="215" width="360" height="95" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="1955" y="238" font-family="Arial, sans-serif" font-size="13" font-weight="bold">GUI-005: PWA Móvil del Tutor</text>
  <text x="1955" y="258" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Historial y calendario familiar de terapias</text>
  <text x="1955" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Botón de acceso directo a teleconsulta</text>
  <text x="1955" y="292" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Descarga local en SessionStorage ante caídas 4G</text>

  <!-- Disparador Modal -->
  <path d="M 2120 310 L 2120 345" stroke="#000000" stroke-width="2" marker-end="url(#arrow2)" />
  <text x="2130" y="333" font-family="Courier, monospace" font-size="11" font-weight="bold">onClick(BTN_FIRMAR_ACTA)</text>

  <rect x="1940" y="345" width="360" height="130" fill="#fafafa" stroke="#000000" stroke-width="1.8" stroke-dasharray="4,3" />
  <text x="1955" y="368" font-family="Arial, sans-serif" font-size="13" font-weight="bold">MDL-005: Modal Firma Biométrica</text>
  <text x="1955" y="388" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Canvas de firma táctil sobre pantalla móvil</text>
  <text x="1955" y="405" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Sellado de tiempo y hash SHA-256 inmutable</text>
  <text x="1955" y="422" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Generación del acta probatoria en MinIO S3</text>
  <text x="1955" y="439" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Notificación push y SMS de confirmación</text>
  <rect x="1955" y="450" width="330" height="18" fill="#e8e8e8" />
  <text x="1960" y="463" font-family="Arial, sans-serif" font-size="10" font-weight="bold">Norman: Affordance Real y Signifiers Táctiles</text>

  <!-- =========================================================================
       SECCIÓN INFERIOR: MATRIZ DE HEURÍSTICAS DE USABILIDAD (SHNEIDERMAN Y NIELSEN)
       ========================================================================= -->
  <rect x="80" y="540" width="2240" height="780" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="80" y="540" width="2240" height="45" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="100" y="570" font-family="Arial, sans-serif" font-size="16" font-weight="bold">MATRIZ DE IMPLEMENTACIÓN ARQUITECTÓNICA: HEURÍSTICAS DE USABILIDAD Y ERGONOMÍA (PLANTILLA 7)</text>

  <!-- Fila 1: Principios 1 a 4 -->
  <rect x="100" y="605" width="530" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="115" y="630" font-family="Arial, sans-serif" font-size="13" font-weight="bold">1. VISIBILIDAD DEL ESTADO DEL SISTEMA (NIELSEN #1)</text>
  <text x="115" y="652" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• En GUI-001 y MDL-001: Indicadores claros de bloqueo pesimista con cronómetro.</text>
  <text x="115" y="670" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• En GUI-004: Barra de progreso en 4 pasos para facturación electrónica.</text>
  <text x="115" y="688" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• En Telemedicina: Semáforo de latencia de red (Verde &lt;100ms, Rojo &gt;300ms).</text>
  <text x="115" y="706" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Trazabilidad: RNF-0004 y RNF-0015.</text>

  <rect x="650" y="605" width="530" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="665" y="630" font-family="Arial, sans-serif" font-size="13" font-weight="bold">2. CONTROL Y LIBERTAD DEL USUARIO (NIELSEN #3)</text>
  <text x="665" y="652" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Botón explícito BTN_CANCELAR en todos los modales para salida segura.</text>
  <text x="665" y="670" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Liberación inmediata de franjas bloqueadas en TB_HORARIOS sin penalidad.</text>
  <text x="665" y="688" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Soporte de tecla ESC y clic fuera del backdrop para descartar ventanas.</text>
  <text x="665" y="706" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Shneiderman Regla #2: Atajos universales y reversibilidad de acciones.</text>

  <rect x="1200" y="605" width="530" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="1215" y="630" font-family="Arial, sans-serif" font-size="13" font-weight="bold">3. CONSISTENCIA Y ESTÁNDARES (NIELSEN #4)</text>
  <text x="1215" y="652" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Nomenclatura nemónica homogénea: BTN_*, FLD_*, SEL_*, MDL_*, TBL_*.</text>
  <text x="1215" y="670" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Paleta B&amp;W de alto contraste con tipografía sans-serif de alta legibilidad.</text>
  <text x="1215" y="688" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Mismo comportamiento de modales flotantes en Web Desktop y PWA Móvil.</text>
  <text x="1215" y="706" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Cumplimiento de WCAG 2.1 AA para contraste y accesibilidad clínica.</text>

  <rect x="1750" y="605" width="550" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="1765" y="630" font-family="Arial, sans-serif" font-size="13" font-weight="bold">4. PREVENCIÓN DE ERRORES E INDULGENCIA (SHNEIDERMAN #5)</text>
  <text x="1765" y="652" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Bloqueo preventivo de campos de texto con validación regex (DNI 8d, RUC 11d).</text>
  <text x="1765" y="670" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Deshabilitación del botón BTN_EMITIR_CPE si faltan datos fiscales obligatorios.</text>
  <text x="1765" y="688" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Alerta modal con doble confirmación antes de anular o reprogramar citas.</text>
  <text x="1765" y="706" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Regla de 24 horas aplicada en frontend y validada por backend (ILA-0029).</text>

  <!-- Fila 2: Principios 5 a 8 -->
  <rect x="100" y="785" width="530" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="115" y="810" font-family="Arial, sans-serif" font-size="13" font-weight="bold">5. RECONOCER ANTES QUE RECORDAR (NIELSEN #6)</text>
  <text x="115" y="832" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Buscador con autocompletado en memoria de códigos CIE-10 neuropediátricos.</text>
  <text x="115" y="850" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Despliegue de antecedentes y alergias del menor en el encabezado de consulta.</text>
  <text x="115" y="868" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Listado desplegable de dosis pediátricas habituales por rango etario.</text>
  <text x="115" y="886" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Reducción de la carga cognitiva en médicos y recepcionistas.</text>

  <rect x="650" y="785" width="530" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="665" y="810" font-family="Arial, sans-serif" font-size="13" font-weight="bold">6. FLEXIBILIDAD Y EFICIENCIA DE USO (NIELSEN #7)</text>
  <text x="665" y="832" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Atajos de teclado para especialistas experimentados (Ctrl+S guardar, Ctrl+P receta).</text>
  <text x="665" y="850" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Plantillas preconfiguradas de texto para notas de evolución frecuentes.</text>
  <text x="665" y="868" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Acceso directo a emisión de comprobantes desde la agenda del día.</text>
  <text x="665" y="886" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Shneiderman Regla #7: Apoyar el locus de control interno.</text>

  <rect x="1200" y="785" width="530" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="1215" y="810" font-family="Arial, sans-serif" font-size="13" font-weight="bold">7. DISEÑO ESTÉTICO Y MINIMALISTA (NIELSEN #8)</text>
  <text x="1215" y="832" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Eliminación total de elementos distractores, bordes curvos o gradientes ruidosos.</text>
  <text x="1215" y="850" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Espaciado uniforme de 8px en grilla CSS para alineación matemática.</text>
  <text x="1215" y="868" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Jerarquía tipográfica rigurosa: 18pt títulos, 13pt campos, 11pt metadatos.</text>
  <text x="1215" y="886" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Interfaz limpia (Clean UI) conforme a las diapositivas de cátedra (Diap. 118).</text>

  <rect x="1750" y="785" width="550" height="160" fill="#fafafa" stroke="#000000" stroke-width="1.5" />
  <text x="1765" y="810" font-family="Arial, sans-serif" font-size="13" font-weight="bold">8. RECUPERACIÓN ANTE ERRORES (NIELSEN #9)</text>
  <text x="1765" y="832" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Mensajes de error constructivos con acción correctiva explícita.</text>
  <text x="1765" y="850" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Si SUNAT rechaza comprobante: código específico (ej. Error 2014 RUC no habido).</text>
  <text x="1765" y="868" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Si se pierde conexión WebRTC: reconexión automática en 3 reintentos con ICE.</text>
  <text x="1765" y="886" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Preservación del borrador de notas en LocalStorage para prevenir pérdida de datos.</text>

  <!-- Fila 3: Conclusiones Ergonómicas -->
  <rect x="100" y="965" width="2200" height="85" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="120" y="995" font-family="Arial, sans-serif" font-size="13" font-weight="bold">CONGRUENCIA CON EL DESARROLLADOR FRONTEND (RNF-0026):</text>
  <text x="120" y="1018" font-family="Arial, sans-serif" font-size="12" fill="#333333">Cada pantalla GUI-* y modal MDL-* se implementa como un componente React 18 modular con TypeScript, utilizando estados desacoplados en React Context / Zustand, peticiones HTTP tipadas hacia Django REST Framework y validación formal de formularios con Zod y React Hook Form, garantizando una codificación sin ambigüedades técnicas.</text>
</svg>"""
    return svg

# ==============================================================================
# 3. FIGURA 6.1: ESTILO DE REPOSITORIO CENTRALIZADO DE DATOS (Vitalis_BD)
# ==============================================================================
def build_svg_fig6_1():
    w, h = 2400, 1450
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <marker id="arrow3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Fondo Blanco -->
  <rect width="{w}" height="{h}" fill="#ffffff" />

  <!-- Encabezado Institucional -->
  <rect x="50" y="30" width="2300" height="90" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <text x="70" y="65" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#000000">NEXOVITALIS360 — ARQUITECTURA CENTRADA EN DATOS (PLANTILLA 6)</text>
  <text x="70" y="98" font-family="Arial, sans-serif" font-size="16" fill="#333333">FIGURA 6.1: ESTILO ARQUITECTÓNICO DE REPOSITORIO CENTRALIZADO (Vitalis_BD EN POSTGRESQL 16 CON PGBOUNCER Y MINIO S3)</text>
  <text x="2100" y="80" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000">DIAPOSITIVAS 67-69</text>

  <!-- =========================================================================
       CAPA 1: CLIENTES Y CONSUMIDORES CONCURRENTES (ARRIBA: Y: 150 - 280)
       ========================================================================= -->
  <rect x="80" y="150" width="2240" height="150" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <rect x="80" y="150" width="2240" height="35" fill="#f0f0f0" stroke="#000000" stroke-width="2" />
  <text x="100" y="174" font-family="Arial, sans-serif" font-size="14" font-weight="bold">CAPA 1: CONSUMIDORES Y SUBSISTEMAS CONCURRENTES (CLIENTES ACTIVOS)</text>

  <!-- Nodo 1: SPA Especialista -->
  <rect x="110" y="200" width="400" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="130" y="225" font-family="Arial, sans-serif" font-size="13" font-weight="bold">SPA React 18: Especialista</text>
  <text x="130" y="245" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Consultas masivas de historias clínicas</text>
  <text x="130" y="262" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Escritura transaccional de notas de evolución</text>

  <!-- Nodo 2: PWA Apoderado -->
  <rect x="550" y="200" width="400" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="570" y="225" font-family="Arial, sans-serif" font-size="13" font-weight="bold">PWA Móvil: Apoderados</text>
  <text x="570" y="245" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Agendamiento de citas concurrentes</text>
  <text x="570" y="262" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Descarga segura de comprobantes y recetas</text>

  <!-- Nodo 3: API REST Django -->
  <rect x="990" y="200" width="400" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1010" y="225" font-family="Arial, sans-serif" font-size="13" font-weight="bold">Backend: Django REST Framework</text>
  <text x="1010" y="245" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Gobernanza de reglas de negocio y validación</text>
  <text x="1010" y="262" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Transacciones atómicas ACID (select_for_update)</text>

  <!-- Nodo 4: Daphne WebSockets -->
  <rect x="1430" y="200" width="400" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1450" y="225" font-family="Arial, sans-serif" font-size="13" font-weight="bold">ASGI Daphne: WebSockets en Tiempo Real</text>
  <text x="1450" y="245" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Notificaciones de Alerta Roja Vital (&lt;92% SpO2)</text>
  <text x="1450" y="262" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Sincronización de cola de atención médica</text>

  <!-- Nodo 5: Celery Workers -->
  <rect x="1870" y="200" width="420" height="80" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1890" y="225" font-family="Arial, sans-serif" font-size="13" font-weight="bold">Workers Asíncronos: Celery 5.4</text>
  <text x="1890" y="245" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Procesamiento Batch de Liquidaciones a médicos</text>
  <text x="1890" y="262" font-family="Arial, sans-serif" font-size="11.5" fill="#444444">• Envío SOAP UBL 2.1 a SUNAT y colas Redis</text>

  <!-- Flechas hacia PgBouncer -->
  <path d="M 1200 300 L 1200 370" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow3)" />
  <text x="1215" y="340" font-family="Courier, monospace" font-size="12" font-weight="bold">TCP 5432 (Pool Connections / TLS 1.3)</text>

  <!-- =========================================================================
       CAPA 2: CONNECTION POOLING (PGBOUNCER) (Y: 370 - 480)
       ========================================================================= -->
  <rect x="300" y="370" width="1800" height="110" fill="#f4f4f4" stroke="#000000" stroke-width="2.5" />
  <text x="1200" y="405" font-family="Arial, sans-serif" font-size="16" font-weight="bold" text-anchor="middle">CAPA DE GESTIÓN Y POOLING DE CONEXIONES: PgBouncer 1.22</text>
  <text x="1200" y="430" font-family="Courier, monospace" font-size="13" text-anchor="middle">Modo: Transaction Pooling | default_pool_size = 50 | max_client_conn = 500 | reserve_pool = 10</text>
  <text x="1200" y="455" font-family="Arial, sans-serif" font-size="12" fill="#444444" text-anchor="middle">Absorbe ráfagas de concurrencia, reutiliza conexiones TCP activas y previene el desbordamiento de memoria RAM en el motor PostgreSQL.</text>

  <!-- Flechas hacia PostgreSQL -->
  <path d="M 1200 480 L 1200 540" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow3)" />
  <text x="1215" y="515" font-family="Courier, monospace" font-size="12" font-weight="bold">Pool Físico (50 Conexiones Dedicadas)</text>

  <!-- =========================================================================
       CAPA 3: MOTOR DE REPOSITORIO CENTRALIZADO: POSTGRESQL 16 (Y: 540 - 1180)
       ========================================================================= -->
  <rect x="80" y="540" width="2240" height="640" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <rect x="80" y="540" width="2240" height="40" fill="#000000" />
  <text x="1200" y="567" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">REPOSITORIO CENTRAL PASIVO DE DATOS: INSTANCIA Vitalis_BD (POSTGRESQL 16 ENGINE)</text>

  <!-- Sub-Bloque A: Tablas Maestras y Entidades del Dominio (X: 110 - 750) -->
  <rect x="110" y="600" width="650" height="550" fill="#fafafa" stroke="#000000" stroke-width="1.8" />
  <text x="130" y="630" font-family="Arial, sans-serif" font-size="14" font-weight="bold">A. ESQUEMA RELACIONAL Y TABLAS MAESTRAS</text>
  <text x="130" y="650" font-family="Arial, sans-serif" font-size="11.5" fill="#555555">Persistencia normalizada bajo reglas de integridad referencial estricta (FKs ON DELETE RESTRICT):</text>

  <!-- Tablas -->
  <rect x="130" y="665" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="688" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_PACIENTES &amp; TB_APODERADOS</text>
  <text x="145" y="704" font-family="Arial, sans-serif" font-size="11" fill="#444444">Filiación clínica del menor, vínculo de patria potestad legal y antecedentes biológicos.</text>

  <rect x="130" y="725" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="748" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_ESPECIALISTAS &amp; TB_HORARIOS</text>
  <text x="145" y="764" font-family="Arial, sans-serif" font-size="11" fill="#444444">Matriz de agendas, turnos disponibles y bloqueo pesimista atómico (SELECT FOR UPDATE).</text>

  <rect x="130" y="785" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="808" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_CITAS_MEDICAS &amp; TB_HISTORIAL_CITAS</text>
  <text x="145" y="824" font-family="Arial, sans-serif" font-size="11" fill="#444444">Máquina de estados de la cita (Solicitada, Confirmada, Atendida) y registro de auditoría.</text>

  <rect x="130" y="845" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="868" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_PRETRIAJE_CLINICO &amp; TB_CONSENTIMIENTOS</text>
  <text x="145" y="884" font-family="Arial, sans-serif" font-size="11" fill="#444444">Signos vitales pediátricos, bandera booleana alerta_roja y hash SHA-256 de firmas.</text>

  <rect x="130" y="905" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="928" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_HISTORIAS_CLINICAS &amp; TB_NOTAS_EVOLUCION</text>
  <text x="145" y="944" font-family="Arial, sans-serif" font-size="11" fill="#444444">Evoluciones inmutables post-cierre, codificación CIE-10 / DSM-5 y recetas médicas.</text>

  <rect x="130" y="965" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="988" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_PAQUETES_SESIONES &amp; TB_COMPROBANTES</text>
  <text x="145" y="1004" font-family="Arial, sans-serif" font-size="11" fill="#444444">Control de saldo de sesiones terapéuticas, Boletas/Facturas y CDR oficial de SUNAT.</text>

  <rect x="130" y="1025" width="610" height="50" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="145" y="1048" font-family="Courier, monospace" font-size="12" font-weight="bold">TB_LIQUIDACIONES_PROFESIONALES</text>
  <text x="145" y="1064" font-family="Arial, sans-serif" font-size="11" fill="#444444">Consolidado mensual batch de honorarios, comisiones y retención de 4ta categoría.</text>

  <!-- Sub-Bloque B: Mecanismos Arquitectónicos de Datos (X: 790 - 1580) -->
  <rect x="790" y="600" width="760" height="550" fill="#fafafa" stroke="#000000" stroke-width="1.8" />
  <text x="810" y="630" font-family="Arial, sans-serif" font-size="14" font-weight="bold">B. MECANISMOS AVANZADOS DE PERSISTENCIA Y RENDIMIENTO</text>

  <!-- B1. Particionamiento -->
  <rect x="810" y="665" width="720" height="85" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="825" y="688" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold">1. Particionamiento Relacional por Rangos Temporales (RANGE PARTITIONING)</text>
  <text x="825" y="708" font-family="Courier, monospace" font-size="11" fill="#000000">PARTITION OF TB_HISTORIAL_CITAS FOR VALUES FROM ('2026-10-01') TO ('2026-11-01');</text>
  <text x="825" y="726" font-family="Arial, sans-serif" font-size="11" fill="#444444">Aislamiento por mes de citas y notas de evolución para mantener índices B-Tree en memoria RAM y acelerar consultas forenses a menos de 50 ms.</text>

  <!-- B2. Transacciones ACID y Bloqueos -->
  <rect x="810" y="765" width="720" height="85" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="825" y="788" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold">2. Aislamiento Transaccional y Control de Concurrencia Pesimista (ACID)</text>
  <text x="825" y="808" font-family="Courier, monospace" font-size="11" fill="#000000">SET TRANSACTION ISOLATION LEVEL READ COMMITTED; SELECT ... FOR UPDATE NOWAIT;</text>
  <text x="825" y="826" font-family="Arial, sans-serif" font-size="11" fill="#444444">Garantiza atomicidad estricta en el débito de sesiones de paquetes y previene venta duplicada de franjas horarias ante reservas concurrentes.</text>

  <!-- B3. Borrado Lógico Soft Delete -->
  <rect x="810" y="865" width="720" height="85" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="825" y="888" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold">3. Política de Eliminación Lógica (SOFT DELETE Y AUDITORÍA FORENSE)</text>
  <text x="825" y="908" font-family="Courier, monospace" font-size="11" fill="#000000">UPDATE TB_CITAS_MEDICAS SET estado = 'Cancelada', activo = false, updated_at = NOW();</text>
  <text x="825" y="926" font-family="Arial, sans-serif" font-size="11" fill="#444444">Prohibición de sentencias DELETE físicas en tablas clínicas; preservación del historial médico para auditorías médico-legales y cumplimiento normativo.</text>

  <!-- B4. Búsqueda Full-Text Search -->
  <rect x="810" y="965" width="720" height="85" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="825" y="988" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold">4. Motor de Búsqueda de Texto Completo (FULL-TEXT SEARCH - GIN INDEX)</text>
  <text x="825" y="1008" font-family="Courier, monospace" font-size="11" fill="#000000">CREATE INDEX idx_cie10_fts ON TB_CIE10 USING GIN (to_tsvector('spanish', descripcion));</text>
  <text x="825" y="1026" font-family="Arial, sans-serif" font-size="11" fill="#444444">Búsqueda predictiva ultrarrápida de diagnósticos y tratamientos sin sobrecargar con LIKEs la base de datos relacional.</text>

  <!-- B5. WAL y Replicación -->
  <rect x="810" y="1065" width="720" height="70" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="825" y="1088" font-family="Arial, sans-serif" font-size="12.5" font-weight="bold">5. Archivador Continuo WAL y Tolerancia a Desastres (DISASTER RECOVERY)</text>
  <text x="825" y="1108" font-family="Arial, sans-serif" font-size="11" fill="#444444">Generación continua de Write-Ahead Logs replicados a disco secundario en SSD NVMe (RPO &lt;= 15 min, RTO &lt;= 30 min conforme a RNF-0020).</text>

  <!-- Sub-Bloque C: Repositorio de Objetos BLOB Cifrados (X: 1580 - 2290) -->
  <rect x="1580" y="600" width="710" height="550" fill="#fafafa" stroke="#000000" stroke-width="1.8" />
  <text x="1600" y="630" font-family="Arial, sans-serif" font-size="14" font-weight="bold">C. ALMACÉN DE OBJETOS CIFRADOS (BLOB STORAGE)</text>
  <text x="1600" y="650" font-family="Arial, sans-serif" font-size="11.5" fill="#555555">Almacenamiento desacoplado para documentos médicos pesados (MinIO / AWS S3):</text>

  <rect x="1600" y="675" width="670" height="130" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="1615" y="700" font-family="Courier, monospace" font-size="12" font-weight="bold">Bucket: vitalis-consentimientos-firmados</text>
  <text x="1615" y="720" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Actas de consentimiento informado firmadas digitalmente por apoderados.</text>
  <text x="1615" y="738" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Cifrado del lado del servidor: SSE-S3 con clave simétrica AES-256.</text>
  <text x="1615" y="756" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Acceso temporal mediante URLs prefirmadas de 300 segundos de validez.</text>
  <text x="1615" y="774" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Metadatos: Hash SHA-256 y dirección IP del firmante (RNF-0024).</text>

  <rect x="1600" y="825" width="670" height="130" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="1615" y="850" font-family="Courier, monospace" font-size="12" font-weight="bold">Bucket: vitalis-comprobantes-sunat-cpe</text>
  <text x="1615" y="870" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Archivos XML UBL 2.1 firmados con certificado digital X.509.</text>
  <text x="1615" y="888" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Constancias de Recepción (CDR) oficiales en formato ZIP/XML.</text>
  <text x="1615" y="906" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Representaciones impresas PDF con Código de Barras Bidimensional QR.</text>
  <text x="1615" y="924" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Retención fiscal legal obligatoria de 5 años inmutable.</text>

  <rect x="1600" y="975" width="670" height="120" fill="#ffffff" stroke="#000000" stroke-width="1.2" />
  <text x="1615" y="1000" font-family="Courier, monospace" font-size="12" font-weight="bold">Bucket: vitalis-recetas-e-informes-medicos</text>
  <text x="1615" y="1020" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Informes de evaluación neuropediátrica, cribados TEA y electroencefalogramas.</text>
  <text x="1615" y="1038" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Recetas médicas firmadas digitalmente con CMP / RNE del profesional.</text>
  <text x="1615" y="1056" font-family="Arial, sans-serif" font-size="11" fill="#333333">• Validación estricta de extensiones y MIME-types (application/pdf).</text>

  <!-- =========================================================================
       PIE DE PÁGINA: JUSTIFICACIÓN DOCTRINAL DE CÁTEDRA
       ========================================================================= -->
  <rect x="80" y="1205" width="2240" height="200" fill="#f4f4f4" stroke="#000000" stroke-width="2" />
  <text x="100" y="1235" font-family="Arial, sans-serif" font-size="14" font-weight="bold">FUNDAMENTACIÓN TÉCNICA DEL ESTILO DE REPOSITORIO SEGÚN LA CÁTEDRA (DR. PERCY HUERTAS):</text>
  <text x="100" y="1260" font-family="Arial, sans-serif" font-size="12.5" fill="#000000">1. Naturaleza Pasiva del Repositorio: El almacén relacional Vitalis_BD opera de manera estrictamente pasiva; no inicia conexiones hacia los clientes, sino que reacciona ante solicitudes de lectura y escritura gobernadas por transacciones ACID.</text>
  <text x="100" y="1285" font-family="Arial, sans-serif" font-size="12.5" fill="#000000">2. Desacoplamiento de Clientes Concurrentes: Los subsistemas (Citas, Triaje, Facturación, Telemedicina) se comunican de forma indirecta compartiendo datos en Vitalis_BD sin generar dependencias de invocación acopladas en memoria de aplicación.</text>
  <text x="100" y="1310" font-family="Arial, sans-serif" font-size="12.5" fill="#000000">3. Absorción de Concurrencia con PgBouncer: La arquitectura soluciona la saturación de conexiones en sistemas clínicos mediante pooling transaccional, garantizando que hasta 500 sesiones de clientes coexistan con solo 50 conexiones físicas en PostgreSQL.</text>
  <text x="100" y="1335" font-family="Arial, sans-serif" font-size="12.5" fill="#000000">4. Alivio del Motor Relacional mediante BLOB Storage: Toda la carga de archivos pesados (PDFs, imágenes de firmas y XMLs fiscales) se externaliza hacia buckets MinIO S3 cifrados con URLs prefirmadas temporales, preservando la ligereza y alta velocidad del motor relacional.</text>
  <text x="100" y="1360" font-family="Arial, sans-serif" font-size="12" font-style="italic" fill="#555555">Trazabilidad Formal: RNF-0011 (PostgreSQL ACID), RNF-0012 (Stack Tecnológico), RNF-0020 (Servidores Producción), RNF-0024 (Blob Storage MinIO) y RNF-0026 (Codificadores).</text>
</svg>"""
    return svg

# ==============================================================================
# 4. FIGURA 6.2: ESTILO DE PIZARRA (BLACKBOARD) PARA SOPORTE DE DECISIONES
# ==============================================================================
def build_svg_fig6_2():
    w, h = 2400, 1450
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <marker id="arrow4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#000000" />
    </marker>
  </defs>

  <!-- Fondo Blanco -->
  <rect width="{w}" height="{h}" fill="#ffffff" />

  <!-- Encabezado -->
  <rect x="50" y="30" width="2300" height="90" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <text x="70" y="65" font-family="Arial, sans-serif" font-size="22" font-weight="bold" fill="#000000">NEXOVITALIS360 — ARQUITECTURA CENTRADA EN DATOS (PLANTILLA 6)</text>
  <text x="70" y="98" font-family="Arial, sans-serif" font-size="16" fill="#333333">FIGURA 6.2: ESTILO ARQUITECTÓNICO DE PIZARRA (BLACKBOARD) PARA SOPORTE DE DECISIONES CLÍNICAS Y ALERTA ROJA</text>
  <text x="2100" y="80" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#000000">DIAPOSITIVA 70 DE CÁTEDRA</text>

  <!-- =========================================================================
       NÚCLEO CENTRAL: LA PIZARRA (MEMORIA COMPARTIDA DE TRABAJO)
       ========================================================================= -->
  <rect x="800" y="160" width="800" height="520" fill="#f8f8f8" stroke="#000000" stroke-width="3" />
  <rect x="800" y="160" width="800" height="45" fill="#000000" />
  <text x="1200" y="190" font-family="Arial, sans-serif" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">1. LA PIZARRA: MEMORIA DE TRABAJO COMPARTIDA (BLACKBOARD)</text>
  <text x="1200" y="225" font-family="Courier, monospace" font-size="13" font-weight="bold" fill="#000000" text-anchor="middle">Objeto de Estado Transaccional: PizarraEvaluacionClinica</text>
  <text x="1200" y="245" font-family="Arial, sans-serif" font-size="11.5" fill="#555555" text-anchor="middle">Almacenamiento Híbrido: Redis 7.2 (En memoria ultra-rápida) + PostgreSQL 16 (TB_PRETRIAJE_CLINICO)</text>

  <!-- Cuadrantes de Estado en la Pizarra -->
  <rect x="830" y="260" width="350" height="180" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="845" y="285" font-family="Arial, sans-serif" font-size="13" font-weight="bold">Parámetros Biométricos Capturados:</text>
  <text x="845" y="310" font-family="Courier, monospace" font-size="11.5" fill="#000000">• saturacion_spo2_pct: float (91.5 %)</text>
  <text x="845" y="330" font-family="Courier, monospace" font-size="11.5" fill="#000000">• frecuencia_cardiaca_bpm: int (135 bpm)</text>
  <text x="845" y="350" font-family="Courier, monospace" font-size="11.5" fill="#000000">• presion_arterial: string ("90/60 mmHg")</text>
  <text x="845" y="370" font-family="Courier, monospace" font-size="11.5" fill="#000000">• temperatura_c: float (37.8 °C)</text>
  <text x="845" y="390" font-family="Courier, monospace" font-size="11.5" fill="#000000">• frecuencia_respiratoria: int (28 rpm)</text>
  <text x="845" y="415" font-family="Arial, sans-serif" font-size="10.5" fill="#666666">Actualizado por: Estación de Triaje</text>

  <rect x="1220" y="260" width="350" height="180" fill="#ffffff" stroke="#000000" stroke-width="1.5" />
  <text x="1235" y="285" font-family="Arial, sans-serif" font-size="13" font-weight="bold">Síntomas y Observaciones del Tutor:</text>
  <text x="1235" y="310" font-family="Courier, monospace" font-size="11.5" fill="#000000">• edad_paciente_meses: int (42 meses)</text>
  <text x="1235" y="330" font-family="Courier, monospace" font-size="11.5" fill="#000000">• hito_lenguaje_retraso: boolean (true)</text>
  <text x="1235" y="350" font-family="Courier, monospace" font-size="11.5" fill="#000000">• contacto_visual_ausente: boolean (true)</text>
  <text x="1235" y="370" font-family="Courier, monospace" font-size="11.5" fill="#000000">• episodios_convulsivos: boolean (false)</text>
  <text x="1235" y="390" font-family="Courier, monospace" font-size="11.5" fill="#000000">• motivo_consulta: string ("Retraso habla")</text>
  <text x="1235" y="415" font-family="Arial, sans-serif" font-size="10.5" fill="#666666">Ingresado por: Portal Apoderado PWA</text>

  <!-- Estado Consolidado en Pizarra -->
  <rect x="830" y="455" width="740" height="205" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <text x="850" y="480" font-family="Arial, sans-serif" font-size="13" font-weight="bold">Estado Dinámico de Diagnóstico y Banderas Heurísticas (Inscritas por KSs):</text>
  <text x="850" y="505" font-family="Courier, monospace" font-size="12" font-weight="bold" fill="#000000">• bandera_alerta_roja: boolean = true [GATILLADA POR KS_01]</text>
  <text x="850" y="525" font-family="Courier, monospace" font-size="12" fill="#000000">• clasificacion_triaje: string = "P1_EMERGENCIA_PEDIATRICA" [ALTO RIESGO VITAL]</text>
  <text x="850" y="545" font-family="Courier, monospace" font-size="12" fill="#000000">• hipotesis_neurodesarrollo: string = "Sospecha Trastorno Espectro Autista (CIE-10 F84.0)"</text>
  <text x="850" y="565" font-family="Courier, monospace" font-size="12" fill="#000000">• consentimiento_bioetico_valido: boolean = true (Hash SHA-256 verificado en TB_CONSENTIMIENTOS)</text>
  <text x="850" y="585" font-family="Courier, monospace" font-size="12" fill="#000000">• agenda_bloqueada_temp: string = "Turno 10:30 Dr. Turpo (SELECT FOR UPDATE)"</text>
  <text x="850" y="605" font-family="Courier, monospace" font-size="12" fill="#000000">• estado_evaluacion: string = "EVALUACION_COMPLETA_REQUIERE_DESPACHO"</text>
  <text x="850" y="640" font-family="Arial, sans-serif" font-size="11" fill="#444444">Semántica de Pizarra: Cualquier fuente de conocimiento puede leer el estado global y aportar deducciones parciales.</text>

  <!-- =========================================================================
       FUENTES DE CONOCIMIENTO (KNOWLEDGE SOURCES - KS)
       ========================================================================= -->
  <!-- KS 1: Izquierda Arriba -->
  <rect x="80" y="160" width="600" height="230" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <rect x="80" y="160" width="600" height="35" fill="#000000" />
  <text x="95" y="184" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">KS_01: ALERTA ROJA VITAL PEDIÁTRICA</text>
  <text x="95" y="215" font-family="Arial, sans-serif" font-size="12" font-weight="bold">Responsabilidad Heurística (Prioridad 1 - Máxima):</text>
  <text x="95" y="235" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Condición de Activación: SpO2 &lt; 92% OR Frecuencia Cardíaca &gt; 140 bpm.</text>
  <text x="95" y="255" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Deducción: Conmuta atómicamente alerta_roja = true en la pizarra.</text>
  <text x="95" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Efecto: Solicita al Control el disparo urgente de sirena visual y WebSockets.</text>
  <text x="95" y="295" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Base Médica: Guía de Reanimación Pediátrica y Triage Manchester.</text>
  <text x="95" y="325" font-family="Courier, monospace" font-size="11" fill="#000000">Trazabilidad: EDU-0023 / ILA-0062 / RNF-0027</text>

  <!-- Flechas KS1 <-> Pizarra -->
  <path d="M 680 275 L 800 275" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" />
  <path d="M 800 285 L 680 285" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" stroke-dasharray="3,3" />

  <!-- KS 2: Derecha Arriba -->
  <rect x="1720" y="160" width="600" height="230" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <rect x="1720" y="160" width="600" height="35" fill="#000000" />
  <text x="1735" y="184" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">KS_02: CRIBADO NEUROPEDIÁTRICO (TEA/TDAH)</text>
  <text x="1735" y="215" font-family="Arial, sans-serif" font-size="12" font-weight="bold">Responsabilidad Heurística (Prioridad 3 - Clínica):</text>
  <text x="1735" y="235" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Condición de Activación: Presencia de cuestionario de desarrollo del apoderado.</text>
  <text x="1735" y="255" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Deducción: Cruza hitos retrasados con criterios diagnósticos DSM-5 / CIE-10.</text>
  <text x="1735" y="275" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Efecto: Sugiere paquete de estimulación temprana y especialista asignado.</text>
  <text x="1735" y="295" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Base Médica: Escala M-CHAT-R/F para detección precoz de autismo.</text>
  <text x="1735" y="325" font-family="Courier, monospace" font-size="11" fill="#000000">Trazabilidad: EDU-0010 / EDU-0025 / ILA-0054</text>

  <!-- Flechas KS2 <-> Pizarra -->
  <path d="M 1720 275 L 1600 275" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" />
  <path d="M 1600 285 L 1720 285" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" stroke-dasharray="3,3" />

  <!-- KS 3: Izquierda Abajo -->
  <rect x="80" y="450" width="600" height="230" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <rect x="80" y="450" width="600" height="35" fill="#000000" />
  <text x="95" y="474" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">KS_03: CONSENTIMIENTO BIOÉTICO Y PATRIA POTESTAD</text>
  <text x="95" y="505" font-family="Arial, sans-serif" font-size="12" font-weight="bold">Responsabilidad Heurística (Prioridad 2 - Legal):</text>
  <text x="95" y="525" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Condición de Activación: Petición de atención presencial o teleconsulta.</text>
  <text x="95" y="545" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Deducción: Inspecciona vigencia del acta de consentimiento en TB_CONSENTIMIENTOS.</text>
  <text x="95" y="565" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Efecto: Si no hay firma válida, inhibe la confirmación y solicita firma inmediata.</text>
  <text x="95" y="585" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Base Legal: Ley General de Salud N° 26842 y protección del menor.</text>
  <text x="95" y="615" font-family="Courier, monospace" font-size="11" fill="#000000">Trazabilidad: EDU-0029 / ILA-0065 / RNF-0010</text>

  <!-- Flechas KS3 <-> Pizarra -->
  <path d="M 680 565 L 800 565" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" />
  <path d="M 800 575 L 680 575" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" stroke-dasharray="3,3" />

  <!-- KS 4: Derecha Abajo -->
  <rect x="1720" y="450" width="600" height="230" fill="#ffffff" stroke="#000000" stroke-width="2.5" />
  <rect x="1720" y="450" width="600" height="35" fill="#000000" />
  <text x="1735" y="474" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#ffffff">KS_04: DISPONIBILIDAD Y DERIVACIÓN DE AGENDAS</text>
  <text x="1735" y="505" font-family="Arial, sans-serif" font-size="12" font-weight="bold">Responsabilidad Heurística (Prioridad 4 - Operativa):</text>
  <text x="1735" y="525" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Condición de Activación: Clasificación de triaje resuelta y consentimiento OK.</text>
  <text x="1735" y="545" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Deducción: Busca médico disponible con subespecialidad neuropediátrica afín.</text>
  <text x="1735" y="565" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Efecto: Adquiere bloqueo pesimista en TB_HORARIOS para evitar colisiones.</text>
  <text x="1735" y="585" font-family="Arial, sans-serif" font-size="11.5" fill="#333333">• Base Técnica: Control transaccional ACID contra colisiones (RNF-0004).</text>
  <text x="1735" y="615" font-family="Courier, monospace" font-size="11" fill="#000000">Trazabilidad: EDU-0012 / ILA-0017 / RNF-0004</text>

  <!-- Flechas KS4 <-> Pizarra -->
  <path d="M 1720 565 L 1600 565" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" />
  <path d="M 1600 575 L 1720 575" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" stroke-dasharray="3,3" />

  <!-- =========================================================================
       COMPONENTE DE CONTROL (ORQUESTADOR HEURÍSTICO) (Y: 720 - 1050)
       ========================================================================= -->
  <rect x="80" y="730" width="2240" height="320" fill="#f4f4f4" stroke="#000000" stroke-width="3" />
  <rect x="80" y="730" width="2240" height="40" fill="#000000" />
  <text x="1200" y="757" font-family="Arial, sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">3. COMPONENTE DE CONTROL: ORQUESTADOR TRANSACCIONAL HEURÍSTICO</text>

  <!-- Bucle de Control -->
  <rect x="110" y="790" width="680" height="235" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="130" y="815" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">Bucle de Inspección y Cola de Prioridades:</text>
  <text x="130" y="840" font-family="Courier, monospace" font-size="11.5" fill="#000000">1. Leer Pizarra cada vez que se produce un cambio de estado.</text>
  <text x="130" y="860" font-family="Courier, monospace" font-size="11.5" fill="#000000">2. Evaluar candidatos ejecutables (KSs habilitadas).</text>
  <text x="130" y="880" font-family="Courier, monospace" font-size="11.5" fill="#000000">3. Ejecutar KS_01 si hay signos vitales (Prioridad 100).</text>
  <text x="130" y="900" font-family="Courier, monospace" font-size="11.5" fill="#000000">4. Ejecutar KS_03 si requiere validación legal (Prioridad 70).</text>
  <text x="130" y="920" font-family="Courier, monospace" font-size="11.5" fill="#000000">5. Ejecutar KS_02 si hay cuestionario de síntomas (Prioridad 50).</text>
  <text x="130" y="940" font-family="Courier, monospace" font-size="11.5" fill="#000000">6. Ejecutar KS_04 si se busca horario de especialista (Prioridad 30).</text>
  <text x="130" y="960" font-family="Courier, monospace" font-size="11.5" fill="#000000">7. Repetir hasta que el estado sea 'EVALUACION_COMPLETA'.</text>
  <text x="130" y="985" font-family="Arial, sans-serif" font-size="11" fill="#555555">Orquestación no lineal: las decisiones emergen de las fuentes de conocimiento.</text>

  <!-- Despachador de Decisiones -->
  <rect x="830" y="790" width="690" height="235" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="850" y="815" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">Despachador de Salidas y Efectos Perimetrales:</text>
  <text x="850" y="845" font-family="Arial, sans-serif" font-size="12" font-weight="bold">• SI alerta_roja == true:</text>
  <text x="870" y="865" font-family="Courier, monospace" font-size="11" fill="#000000">→ Emite evento WebSocket inmediato vía Daphne ASGI a /ws/urgencias/</text>
  <text x="870" y="885" font-family="Courier, monospace" font-size="11" fill="#000000">→ Activa sirena visual y notificación de guardia en pantalla de shock trauma.</text>
  <text x="870" y="905" font-family="Courier, monospace" font-size="11" fill="#000000">→ Interrumpe flujo estándar y genera ficha de ingreso prioritario.</text>
  <text x="850" y="930" font-family="Arial, sans-serif" font-size="12" font-weight="bold">• SI alerta_roja == false &amp;&amp; consentimiento_valido == true:</text>
  <text x="870" y="950" font-family="Courier, monospace" font-size="11" fill="#000000">→ Autoriza consolidación de la Cita Médica en TB_CITAS_MEDICAS.</text>
  <text x="870" y="970" font-family="Courier, monospace" font-size="11" fill="#000000">→ Habilita la emisión del comprobante y pase a sala de espera.</text>
  <text x="870" y="990" font-family="Courier, monospace" font-size="11" fill="#000000">→ Cierra el ciclo de la Pizarra liberando la clave transaccional en Redis.</text>

  <!-- Receptor Perimetral -->
  <rect x="1560" y="790" width="730" height="235" fill="#ffffff" stroke="#000000" stroke-width="1.8" />
  <text x="1580" y="815" font-family="Arial, sans-serif" font-size="13.5" font-weight="bold">Salidas Transaccionales Hacia el Ecosistema:</text>

  <rect x="1580" y="835" width="690" height="48" fill="#f0f0f0" stroke="#000000" stroke-width="1" />
  <text x="1595" y="855" font-family="Arial, sans-serif" font-size="12" font-weight="bold">A. Notificación de Emergencia (WebSockets WSS / Redis Pub-Sub):</text>
  <text x="1595" y="872" font-family="Courier, monospace" font-size="11" fill="#333333">Dispara broadcast en &lt; 200 ms hacia estación de Enfermería y Médico de Guardia.</text>

  <rect x="1580" y="895" width="690" height="48" fill="#f0f0f0" stroke="#000000" stroke-width="1" />
  <text x="1595" y="915" font-family="Arial, sans-serif" font-size="12" font-weight="bold">B. Persistencia Definitiva en Repositorio Relacional (PostgreSQL):</text>
  <text x="1595" y="932" font-family="Courier, monospace" font-size="11" fill="#333333">Inserta registro auditable en TB_PRETRIAJE_CLINICO con parámetros y diagnóstico.</text>

  <rect x="1580" y="955" width="690" height="48" fill="#f0f0f0" stroke="#000000" stroke-width="1" />
  <text x="1595" y="975" font-family="Arial, sans-serif" font-size="12" font-weight="bold">C. Generación de Enlace WebRTC (Google Meet API OAuth2):</text>
  <text x="1595" y="992" font-family="Courier, monospace" font-size="11" fill="#333333">Si la cita es teleconsulta, emite enlace con PIN único para la sala virtual.</text>

  <!-- Flechas de Control hacia la Pizarra -->
  <path d="M 1200 730 L 1200 680" stroke="#000000" stroke-width="2.5" marker-end="url(#arrow4)" />
  <text x="1215" y="710" font-family="Courier, monospace" font-size="11" font-weight="bold">Inspección de Estado y Despacho Heurístico</text>

  <!-- =========================================================================
       PIE: FUNDAMENTACIÓN TEÓRICA (DIAPOSITIVA 70)
       ========================================================================= -->
  <rect x="80" y="1080" width="2240" height="320" fill="#ffffff" stroke="#000000" stroke-width="2" />
  <text x="100" y="1115" font-family="Arial, sans-serif" font-size="15" font-weight="bold">FUNDAMENTACIÓN DEL ESTILO DE PIZARRA EN SALUD DIGITAL SEGÚN CÁTEDRA (DR. PERCY HUERTAS):</text>
  <text x="100" y="1145" font-family="Arial, sans-serif" font-size="13" fill="#000000">1. Justificación de la Pizarra (Blackboard Architecture - Diapositiva 70):</text>
  <text x="120" y="1170" font-family="Arial, sans-serif" font-size="12" fill="#333333">El docente señala que el estilo de pizarra es ideal para sistemas que manejan problemas complejos no deterministas, reconocimiento de patrones, diagnóstico clínico o compiladores (haciendo la analogía con una clase universitaria donde varios profesores expertos escriben y resuelven un problema colaborativamente sobre una misma pizarra).</text>

  <text x="100" y="1205" font-family="Arial, sans-serif" font-size="13" font-weight="bold">2. Aplicación Concreta en Neuropediatría (NexoVitalis360):</text>
  <text x="120" y="1230" font-family="Arial, sans-serif" font-size="12" fill="#333333">En la atención pediátrica no existe un flujo lineal rígido: un niño puede presentar signos de riesgo vital inmediato (hipoxemia SpO2 &lt; 92%), o bien una sospecha de trastorno del neurodesarrollo (TEA/TDAH) que requiere interconsulta, o requerir la firma urgente de su apoderado. La Pizarra permite que las 4 Fuentes de Conocimiento operen de forma totalmente desacoplada, aportando conocimiento incremental a la memoria compartida.</text>

  <text x="100" y="1265" font-family="Arial, sans-serif" font-size="13" font-weight="bold">3. Implementación para el Codificador (RNF-0026 / RNF-0027):</text>
  <text x="120" y="1290" font-family="Arial, sans-serif" font-size="12" fill="#333333">Para los desarrolladores de RuwayLabs, este patrón se implementa con Python 3.12 y Redis 7.2 (hashes HSET para la memoria de la pizarra), tareas Celery para la ejecución de las KSs y Daphne ASGI para el canal WebSocket de notificaciones en tiempo real, garantizando latencias de respuesta inferiores a 150 ms en emergencias médicas.</text>

  <text x="100" y="1335" font-family="Arial, sans-serif" font-size="11.5" font-style="italic" fill="#555555">Referencias: Hayes-Roth, B. (1985). "A Blackboard Architecture for Control" &#8226; Lixin Tao (2010), Software Architecture Illuminated &#8226; Diapositiva 70 del curso.</text>
</svg>"""
    return svg

# ==============================================================================
# EJECUCIÓN PRINCIPAL Y COMPILACIÓN VECTORIAL
# ==============================================================================
def main():
    diagrams = [
        # (Nombre base, función svg, dir_destino, titulo, ancho, alto)
        ("fig7_1_arbol_navegacion_roles", build_svg_fig7_1, DIR_GUIS, "Figura 7.1: Árbol de Navegación y Mapa de Sitio Global por Roles", 2400, 1400, "Figura_7_1_Arbol_Navegacion_Roles_v01.00"),
        ("fig7_2_flujo_interfaces_modales", build_svg_fig7_2, DIR_GUIS, "Figura 7.2: Flujo de Interacción UI, Pantallas y Modales Flotantes", 2400, 1400, "Figura_7_2_Flujo_Interfaces_Modales_v01.00"),
        ("fig6_1_arquitectura_repositorio_datos", build_svg_fig6_1, DIR_DATOS, "Figura 6.1: Estilo Arquitectónico de Repositorio Centralizado de Datos", 2400, 1450, "Figura_6_1_Arquitectura_Repositorio_Datos_v01.00"),
        ("fig6_2_arquitectura_pizarra_clinica", build_svg_fig6_2, DIR_DATOS, "Figura 6.2: Estilo Arquitectónico de Pizarra (Blackboard) para Soporte de Decisiones", 2400, 1450, "Figura_6_2_Arquitectura_Pizarra_Clinica_v01.00")
    ]

    for fname, svg_gen, target_dir, title, w, h, official_png_name in diagrams:
        svg_content = svg_gen()
        svg_path = os.path.join(target_dir, f"{fname}.svg")
        html_path = os.path.join(target_dir, f"{fname}.html")
        png_path = os.path.join(target_dir, f"{official_png_name}.png")

        # 1. Guardar SVG
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"SVG generado: {svg_path}")

        # 2. Guardar HTML interactivo
        html_content = create_interactive_html(svg_content, title, w, h)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"HTML interactivo generado: {html_path}")

        # 3. Compilar a PNG 300 DPI con Inkscape
        cmd = ["inkscape", svg_path, "-o", png_path, "--export-dpi=300"]
        print(f"Compilando a PNG 300 DPI: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        print(f"PNG generado: {png_path} ({os.path.getsize(png_path)} bytes)")

if __name__ == "__main__":
    main()

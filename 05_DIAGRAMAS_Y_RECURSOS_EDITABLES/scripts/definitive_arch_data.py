#!/usr/bin/env python3
"""
definitive_arch_data.py (v02.10)
Definición arquitectónica exhaustiva con Entry Points explícitos (EP-01..EP-06),
Actores reales del Catálogo (ACT-0001..0005 + operativos), ubicación biunívoca de
las 28 secciones GUI / 140 Modales, Zonas de Despliegue VPC, Tuberías/Lotes (Plantilla 8)
y validador geométrico estricto de cero colisiones.
"""

import re

CANVAS_W = 4080
CANVAS_H = 2380
FRONTIER = {"x": 1135, "y": 315, "w": 2005, "h": 1945}

# Bandas visivas de Zonas de Despliegue (05_Vista_Fisica / RNF-0020, RNF-0025)
ZONES = [
    {
        "id": "ZONA-1L",
        "label": "ZONA 1: CLIENTES WEB / PWA & ENTRY POINTS FRONTALES (RNF-0016..0019)",
        "rect": [40, 325, 1000, 1320],
    },
    {
        "id": "ZONA-1R",
        "label": "ZONA 1 (CLÍNICA): ESTACIÓN ESPECIALISTA (RNF-0016..0019)",
        "rect": [3185, 325, 875, 345],
    },
    {
        "id": "ZONA-2-DMZ",
        "label": "ZONA 2: DMZ PERÍMETRO (:443 WAF)",
        "rect": [1165, 340, 580, 245],
    },
    {
        "id": "ZONA-4-DATOS",
        "label": "ZONA 4: SUBRED PRIVADA DATOS VPC (PG16 :6432 • MINIO :9000 • REDIS :6379)",
        "rect": [1835, 1285, 590, 775],
    },
]

# Mapeo explícito 1:1 de las 28 secciones GUI del Catálogo hacia Bloque y Entry Point ("esta GUI va acá")
GUI_PLACEMENT = [
    {"gui": "GUI-0001", "edu": "EDU-0008", "titulo": "Estados de Cita", "bloque": "B4", "ep": "EP-02", "mdls": "MDL-0001..0005 (4 act, 1 bl)"},
    {"gui": "GUI-0002", "edu": "EDU-0009", "titulo": "Historial de Cambios", "bloque": "B10", "ep": "EP-04", "mdls": "MDL-0006..0010 (4 act, 1 bl)"},
    {"gui": "GUI-0003", "edu": "EDU-0010", "titulo": "Validación Derivación", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0011..0015 (5 act)"},
    {"gui": "GUI-0004", "edu": "EDU-0011", "titulo": "Permisos RBAC por Rol", "bloque": "B10", "ep": "EP-04", "mdls": "MDL-0016..0020 (5 act)"},
    {"gui": "GUI-0005", "edu": "EDU-0012", "titulo": "Gestión de Citas", "bloque": "B4", "ep": "EP-02 / EP-01", "mdls": "MDL-0021..0025 (5 act)"},
    {"gui": "GUI-0006", "edu": "EDU-0013", "titulo": "Reprogramación Drag&Drop", "bloque": "B4", "ep": "EP-02 / EP-01", "mdls": "MDL-0026..0030 (5 act)"},
    {"gui": "GUI-0007", "edu": "EDU-0014", "titulo": "Pacientes Pediátricos", "bloque": "B1", "ep": "EP-01 / EP-02", "mdls": "MDL-0031..0035 (5 act)"},
    {"gui": "GUI-0008", "edu": "EDU-0015", "titulo": "Derivación de Pacientes", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0036..0040 (5 act)"},
    {"gui": "GUI-0009", "edu": "EDU-0016", "titulo": "Especialistas y Tarifas", "bloque": "B3", "ep": "EP-02", "mdls": "MDL-0041..0045 (5 act)"},
    {"gui": "GUI-0010", "edu": "EDU-0017", "titulo": "Agenda y Horarios", "bloque": "B3", "ep": "EP-02 / EP-03", "mdls": "MDL-0046..0050 (4 act, 1 bl)"},
    {"gui": "GUI-0011", "edu": "EDU-0018", "titulo": "Modalidades de Cita", "bloque": "B4", "ep": "EP-02 / EP-01", "mdls": "MDL-0051..0055 (4 act, 1 bl)"},
    {"gui": "GUI-0012", "edu": "EDU-0019", "titulo": "Sala Videoconferencia Meet", "bloque": "B5", "ep": "EP-05", "mdls": "MDL-0056..0060 (4 act, 1 bl)"},
    {"gui": "GUI-0013", "edu": "EDU-0020", "titulo": "Mensajería Citas T-24h", "bloque": "B6", "ep": "EP-02", "mdls": "MDL-0061..0065 (4 act, 1 bl)"},
    {"gui": "GUI-0014", "edu": "EDU-0021", "titulo": "Apoderados y Tutores", "bloque": "B1", "ep": "EP-01 / EP-02", "mdls": "MDL-0066..0070 (4 act, 1 bl)"},
    {"gui": "GUI-0015", "edu": "EDU-0022 (OMITIDA)", "titulo": "Sección en blanco base", "bloque": "CTX-CAT", "ep": "N/A", "mdls": "MDL-0071..0075 (5 en blanco)"},
    {"gui": "GUI-0016", "edu": "EDU-0023", "titulo": "Pre-Triaje (TRIAJE_001)", "bloque": "B2", "ep": "EP-01 / EP-02", "mdls": "MDL-0076..0080 (4 act, 1 bl)"},
    {"gui": "GUI-0017", "edu": "EDU-0025", "titulo": "Documentos Adjuntos", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0081..0085 (4 act, 1 bl)"},
    {"gui": "GUI-0018", "edu": "EDU-0027", "titulo": "Interconsulta Clínica", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0086..0090 (4 act, 1 bl)"},
    {"gui": "GUI-0019", "edu": "EDU-0028", "titulo": "Recetas Médicas Cifradas", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0091..0095 (5 act)"},
    {"gui": "GUI-0020", "edu": "EDU-0029", "titulo": "Consentimiento Informado", "bloque": "B2", "ep": "EP-01 / EP-02", "mdls": "MDL-0096..0100 (5 act)"},
    {"gui": "GUI-0021", "edu": "EDU-0030", "titulo": "Diagnóstico CIE-10/DSM-5", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-00101..0105 (5 act)"},
    {"gui": "GUI-0022", "edu": "EDU-0032", "titulo": "Historia Clínica Integral", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0106..0110 (5 act)"},
    {"gui": "GUI-0023", "edu": "EDU-0033", "titulo": "Paquetes de Sesiones (90d)", "bloque": "B8", "ep": "EP-02 / EP-01", "mdls": "MDL-0111..0115 (5 act)"},
    {"gui": "GUI-0024", "edu": "EDU-0034", "titulo": "Descuentos y Convenios", "bloque": "B8", "ep": "EP-02", "mdls": "MDL-0116..0120 (5 act)"},
    {"gui": "GUI-0025", "edu": "EDU-0035", "titulo": "Notas de Evolución (<72h)", "bloque": "B7", "ep": "EP-03", "mdls": "MDL-0121..0125 (5 act)"},
    {"gui": "GUI-0026", "edu": "EDU-0036", "titulo": "Pagos, Vouchers y Devol.", "bloque": "B8", "ep": "EP-02 / EP-01", "mdls": "MDL-0126..0130 (5 act)"},
    {"gui": "GUI-0027", "edu": "EDU-0037", "titulo": "Facturación SUNAT CPE", "bloque": "B8", "ep": "EP-02", "mdls": "MDL-0131..0135 (5 act)"},
    {"gui": "GUI-0028", "edu": "EDU-0038", "titulo": "Liquidación Mensual", "bloque": "B9", "ep": "EP-04", "mdls": "MDL-0136..0140 (5 act)"},
]
GUI_PLACEMENT[20]["mdls"] = "MDL-0101..0105 (5 act)"

# 30 Nodos Arquitectónicos (incluyendo EP-01..EP-06 explícitos y B0..B12 + Actores + APIs)
NODES = [
    {
        "id": "LEGEND",
        "code": "NOTACIÓN & EP",
        "title": "Leyenda, Zonas VPC y Ruta de Entrada",
        "subtitle": "UML 2.5 • Actores → Entry Points → B0 → Bloques",
        "capa": "Transversal",
        "kind": "legend",
        "rect": [35, 115, 455, 170],
        "gui_strip": "28 Secciones GUI (125 MDL activos + 15 en blanco) • 104 ESP + 113 Pruebas",
        "summary_lines": [
            "<b>Ingreso Obligatorio:</b> Actores [EXT-A*] → Entry Points [EP-*] → [B0 WAF/JWT] → [B1..B10]",
            "<b>───►</b> Flujo Síncrono (HTTPS :443 / SQL :6432 / SOAP) | <b>- - ►</b> Asíncrono (WSS / Celery / Webhook)",
            "<i>Clic en cualquier tarjeta, EP-* o flujo F* para inspeccionar APIs, GUIs, ESP y Pruebas.</i>",
        ],
        "apis": [],
        "tbs": [],
        "extra_tags": ["RNF-0022", "RNF-0025"],
    },
    {
        "id": "EP-05",
        "code": "ENTRY POINT EP-05",
        "title": "Sala WebRTC & Alerta WSS (/app/teleconsulta/:id)",
        "subtitle": "Punto de Entrada Compartido • Tutor (A1) + Médico (A3)",
        "capa": "Entry Points y Canales",
        "kind": "entry",
        "rect": [1190, 115, 530, 160],
        "gui_strip": "GUI ACOGIDA: GUI-0012 (Sala Meet MDL-0056..59) + Banner Alerta Roja (RNF-0006)",
        "summary_lines": [
            "<b>Actúan:</b> EXT-A1 (Apoderado) + EXT-A3 (Especialista Clínico) en sesión conjunta",
            "<b>Protocolo:</b> HTTPS + W3C WebRTC MediaDevices + wss://.../ws/alertas-rojas/",
            "<b>Guarda B0:</b> JWT válido + Token Meet API + Pub/Sub Redis (RNF-0008, 0019, 0027)",
        ],
        "apis": [
            {"method": "ROUTE", "endpoint": "/app/teleconsulta/:id & wss://vitalis.pe/ws/alertas-rojas/", "auth": "AuthGuard + JWT Room Token", "purpose": "Sala virtual compartida WebRTC y cabecera de Alerta Roja no descartable (GUI-0012, Fig 7.1)", "sla": "< 150 ms WSS"},
        ],
        "tbs": [],
        "extra_tags": ["GUI-0012", "EDU-0019", "RNF-0006", "RNF-0008", "RNF-0019"],
    },
    {
        "id": "EXT-API1",
        "code": "EXT-API1",
        "title": "Google Meet API",
        "subtitle": "Servicio Externo Capa 5 • Google Cloud",
        "capa": "Capa 5: APIs Externas",
        "kind": "ext",
        "rect": [1880, 115, 480, 155],
        "gui_strip": "Invocado desde B5 → enlace mostrado en GUI-0012 (MDL-0056..0059) y GUI-0013",
        "summary_lines": [
            "<b>Protocolo:</b> OAuth2 + HTTPS REST (TLS 1.3)",
            "<b>Endpoint:</b> POST /v2/spaces → Meet URL + Room Token",
            "<b>Trazabilidad:</b> EDU-0019 • RNF-0008, RNF-0014, RNF-0019",
        ],
        "apis": [
            {"method": "POST", "endpoint": "https://meet.googleapis.com/v2/spaces", "auth": "OAuth 2.0 Bearer", "purpose": "Aprovisionar sala virtual WebRTC al confirmar cita virtual (ILA-0045)", "sla": "< 2.5 s"},
            {"method": "PATCH", "endpoint": "https://meet.googleapis.com/v2/spaces/{space}", "auth": "OAuth 2.0 Bearer", "purpose": "Regenerar o invalidar enlace expirado (ILA-0047/0048)", "sla": "< 2.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["EDU-0019", "RNF-0008", "RNF-0014", "RNF-0019"],
    },
    {
        "id": "EXT-API2",
        "code": "EXT-API2",
        "title": "WhatsApp Cloud API / Twilio",
        "subtitle": "Pasarela Mensajería Externa Capa 5",
        "capa": "Capa 5: APIs Externas",
        "kind": "ext",
        "rect": [2530, 115, 530, 155],
        "gui_strip": "Monitoreado en GUI-0013 (MDL-0061..0064) • Webhook entra vía EP-06 → B0",
        "summary_lines": [
            "<b>Protocolo:</b> HTTPS REST TLS 1.3 + Webhook entrante vía EP-06",
            "<b>Endpoint:</b> POST /messages (T-24h) ↔ Webhook /webhooks/mensajeria/status/",
            "<b>Trazabilidad:</b> EDU-0020, EDU-0013 • RNF-0009, RNF-0014",
        ],
        "apis": [
            {"method": "POST", "endpoint": "https://graph.facebook.com/v20.0/{phone_id}/messages", "auth": "Meta System Token", "purpose": "Despacho automático T-24h por WhatsApp y telefonía con enlace Meet (ILA-0049)", "sla": "Batch Celery T-24h"},
            {"method": "WEBHOOK", "endpoint": "POST /api/v1/webhooks/mensajeria/status/", "auth": "HMAC Signature SHA-256 (EP-06)", "purpose": "Recepción de estado Enviado / Fallido / Pendiente hacia TB_RECORDATORIOS_CITA", "sla": "Asíncrono"},
        ],
        "tbs": [],
        "extra_tags": ["EDU-0020", "RNF-0009", "RNF-0014"],
    },

    # COL 1: ACTORES EXTERNOS (IZQUIERDA)
    {
        "id": "EXT-A1",
        "code": "EXT-A1",
        "title": "Apoderado / Paciente Menor",
        "subtitle": "Actor Operativo • Smartphone PWA (Android/iOS)",
        "capa": "Capa 1: Presentación y Actores",
        "kind": "ext",
        "rect": [55, 375, 355, 220],
        "gui_strip": "ENTRA POR: EP-01 (/app/tutor/*) y EP-05 (/app/teleconsulta/:id)",
        "summary_lines": [
            "<b>Rol Real:</b> Padre/Tutor legal (EDU-0014/21/23/29) • Paciente pediátrico menor",
            "<b>Dispositivo:</b> Smartphone Android 11+/iOS 15+ PWA + SessionStorage (RNF-0018/19)",
            "<b>Actúa en:</b> Filiación, Pre-Triaje, Consentimiento, Reserva/Pago Citas",
        ],
        "apis": [
            {"method": "ACTOR", "endpoint": "Entra vía EP-01 (/app/tutor/*) & EP-05 (/app/teleconsulta/:id)", "auth": "JWT 15m (Rol Tutor)", "purpose": "Portal responsivo de tutela clínica, pago y teleconsulta (RNF-0007, RNF-0018)", "sla": "Heap <= 350MB"},
        ],
        "tbs": [],
        "extra_tags": ["EP-01", "EP-05", "RNF-0007", "RNF-0018", "RNF-0019"],
    },
    {
        "id": "EXT-A2",
        "code": "EXT-A2",
        "title": "Asistente / Secretaria General (ACT-0005)",
        "subtitle": "Actor Catálogo ACT-0005 • Recepción & Caja",
        "capa": "Capa 1: Presentación y Actores",
        "kind": "ext",
        "rect": [55, 685, 355, 235],
        "gui_strip": "ENTRA POR: EP-02 (/app/admin/*, /admision-recepcion/*, /caja)",
        "summary_lines": [
            "<b>Catálogo:</b> ACT-0005 Administrador (Secundario: Secretaria General)",
            "<b>Estación:</b> PC Core i5/Ryzen 5, Win10/11 + pagefile.sys 1.5x-2x (RNF-0016/17)",
            "<b>Actúa en:</b> Agendamiento Multimodal, Horarios, Paquetes, Vouchers y SUNAT",
        ],
        "apis": [
            {"method": "ACTOR", "endpoint": "Entra vía EP-02 (/app/admin/* & /caja)", "auth": "JWT + RBAC ACT-0005", "purpose": "Operación diaria de recepción, agenda <=2.0s y facturación UBL 2.1 (RNF-0015, 0023)", "sla": "<= 2.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["ACT-0005", "EP-02", "RNF-0015", "RNF-0016", "RNF-0017"],
    },
    {
        "id": "EXT-A4",
        "code": "EXT-A4",
        "title": "Gerencia & Jefaturas (ACT-0001..0004)",
        "subtitle": "Actores Principales Catálogo • Dirección Clínica",
        "capa": "Capa 1: Presentación y Actores",
        "kind": "ext",
        "rect": [55, 1015, 355, 225],
        "gui_strip": "ENTRA POR: EP-04 (/app/admin/gobernanza/*, /auditoria, /liquidaciones)",
        "summary_lines": [
            "<b>Catálogo:</b> ACT-0001 Gerente General; ACT-0002..0004 Jefes Med/Nut/Psicología",
            "<b>Organizaciones:</b> ORG-0001 NexoVitalis360 • ORG-0002 RuwayLabs • ORG-0003 UNSA",
            "<b>Actúa en:</b> Políticas RBAC, Auditoría Forense, Aprobación Liquidaciones",
        ],
        "apis": [
            {"method": "ACTOR", "endpoint": "Entra vía EP-04 (/app/admin/gobernanza/*)", "auth": "JWT + RBAC ACT-0001..0004", "purpose": "Control estratégico, permisos por rol y aprobación batch mensual (EDU-0009, 0011, 0038)", "sla": "< 2.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["ACT-0001", "ACT-0002", "ACT-0003", "ACT-0004", "EP-04", "RNF-0003"],
    },

    # COL 2: ENTRY POINTS EXPLÍCITOS (EP-01, EP-02, EP-04, EP-06)
    {
        "id": "EP-01",
        "code": "ENTRY POINT EP-01",
        "title": "Portal PWA Tutor (/app/tutor/*)",
        "subtitle": "Frontend React 18 PWA + Service Worker + AuthGuard",
        "capa": "Entry Points y Canales",
        "kind": "entry",
        "rect": [585, 375, 430, 220],
        "gui_strip": "ALOJAMIENTO GUI: GUI-0007, GUI-0014, GUI-0016, GUI-0020, GUI-0023, GUI-0026 + 0005/06/11",
        "summary_lines": [
            "<b>Quién entra:</b> EXT-A1 (Apoderado / Tutor Legal) vía HTTPS Port 443",
            "<b>Rutas Fig 7.1:</b> /app/tutor/citas, /pretriaje, /expediente, /pagos (/portal-apoderado/*)",
            "<b>Destino vía B0:</b> B1 (Filiación), B2 (Pre-Triaje/Acta), B4 (Citas) y B8 (Pagos)",
        ],
        "apis": [
            {"method": "ENTRY", "endpoint": "https://vitalis.pe/app/tutor/* + /api/v1/auth/jwt/login/", "auth": "AuthGuard + JWT 15m (Rol Tutor)", "purpose": "Punto de entrada único móvil para familias: filiación, triaje, consentimiento y pago (RNF-0018)", "sla": "Heap <= 350MB"},
        ],
        "tbs": [],
        "extra_tags": ["GUI-0007", "GUI-0014", "GUI-0016", "GUI-0020", "GUI-0023", "GUI-0026", "RNF-0018"],
    },
    {
        "id": "EP-02",
        "code": "ENTRY POINT EP-02",
        "title": "Consola Admisión & Caja (/app/admin/*)",
        "subtitle": "Frontend React SPA Recepción + RoleGuard Admin/Asistente",
        "capa": "Entry Points y Canales",
        "kind": "entry",
        "rect": [585, 685, 430, 235],
        "gui_strip": "ALOJAMIENTO GUI: GUI-0001, 0005, 0006, 0009, 0010, 0011, 0013, 0023, 0024, 0026, 0027",
        "summary_lines": [
            "<b>Quién entra:</b> ACT-0005 (Secretaria General / Admisión) en PC Win10/11",
            "<b>Rutas Fig 7.1:</b> /admision-recepcion/* (/recepcion, /citas/nueva, /triaje, /caja)",
            "<b>Destino vía B0:</b> B3 (Horarios), B4 (Orquestador), B6 (Avisos) y B8 (Paquetes/SUNAT)",
        ],
        "apis": [
            {"method": "ENTRY", "endpoint": "https://vitalis.pe/app/admin/* & /caja -> NGINX :443 B0", "auth": "AuthGuard + RoleGuard ACT-0005", "purpose": "Entrada operativa de recepción y caja registradora con validación DNI/RUC SUNAT", "sla": "<= 2.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["ACT-0005", "GUI-0001", "GUI-0005", "GUI-0006", "GUI-0009", "GUI-0010", "GUI-0011", "GUI-0013", "GUI-0024", "GUI-0027"],
    },
    {
        "id": "EP-04",
        "code": "ENTRY POINT EP-04",
        "title": "Consola Gobernanza & BI (/auditoria)",
        "subtitle": "Frontend React SPA Gerencial + RoleGuard Estricto",
        "capa": "Entry Points y Canales",
        "kind": "entry",
        "rect": [585, 1015, 430, 225],
        "gui_strip": "ALOJAMIENTO GUI: GUI-0002 (Historial), GUI-0004 (Permisos RBAC), GUI-0028 (Liquidación)",
        "summary_lines": [
            "<b>Quién entra:</b> ACT-0001 (Gerente) y ACT-0002..0004 (Jefes de Servicio)",
            "<b>Rutas Fig 7.1:</b> /app/admin/gobernanza/*, /usuarios, /auditoria, /liquidaciones",
            "<b>Destino vía B0:</b> B10 (Políticas RBAC & Logs UTC) y B9 (Aprobación Honorarios)",
        ],
        "apis": [
            {"method": "ENTRY", "endpoint": "https://vitalis.pe/app/admin/gobernanza/* -> B0", "auth": "JWT + MFA + RoleGuard ACT-0001", "purpose": "Punto de entrada administrativo de alto privilegio para auditoría, permisos y cierre mensual", "sla": "< 2.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["ACT-0001", "GUI-0002", "GUI-0004", "GUI-0028", "RNF-0001", "RNF-0003"],
    },
    {
        "id": "EP-06",
        "code": "ENTRY POINT EP-06",
        "title": "Ingress M2M: Webhooks TLS & Celery Beat",
        "subtitle": "Entradas Automatizadas sin Login Humano (Sistema a Sistema)",
        "capa": "Entry Points y Canales",
        "kind": "entry",
        "rect": [575, 1345, 440, 265],
        "gui_strip": "SIN GUI HUMANA • Alimenta estados visibles en GUI-0013 (T-24h), GUI-0026 (Pagos) y GUI-0028",
        "summary_lines": [
            "<b>1. Webhook Pagos (EXT-API4):</b> POST /api/v1/pagos/cb (Firma HMAC TLS 1.3 → B0 → B8)",
            "<b>2. Webhook WhatsApp (EXT-API2):</b> POST /api/v1/webhooks/mensajeria/status/ (→ B0 → B6)",
            "<b>3. Cron Celery Beat (B12 Redis):</b> Scheduler diario T-24h (B6) & cierre fin de mes (B9)",
        ],
        "apis": [
            {"method": "WEBHOOK", "endpoint": "POST /api/v1/pagos/cb & /webhooks/mensajeria/status/", "auth": "HMAC-SHA256 + IP Allowlist WAF B0", "purpose": "Callbacks asíncronos autenticados desde Pasarela PCI-DSS y Meta/Twilio sin sesión humana", "sla": "< 500 ms"},
            {"method": "CRON", "endpoint": "celery_beat://schedule (T-24h & monthly_settlement)", "auth": "Subred Privada Redis 6379", "purpose": "Disparo programado de recordatorios T-24h (EDU-0020) y lotes de liquidación (EDU-0038)", "sla": "Cron Determinista"},
        ],
        "tbs": ["TB_RECORDATORIOS_CITA", "TB_PAGOS", "TB_LIQUIDACIONES"],
        "extra_tags": ["EDU-0020", "EDU-0036", "EDU-0038", "RNF-0009", "RNF-0014", "RNF-0026"],
    },

    # COL 3: SISTEMA IZQUIERDA (DMZ B0 + BLOQUES B1, B2, B3, B10, CTX-CAT)
    {
        "id": "B0",
        "code": "B0 • DMZ GATEWAY",
        "title": "B0. API Gateway, WAF, NGINX TLS 1.3 & Auth JWT",
        "subtitle": "Capa 2 (Zona DMZ): Aduana Única, Tokenización y Bus /api/v1/*",
        "capa": "Capa 2: Seguridad y API Gateway",
        "kind": "hub",
        "rect": [1190, 375, 530, 185],
        "gui_strip": "Aplica AuthGuard/RoleGuard sobre todas las 28 GUIs • Endpoints Login & Refresh JWT",
        "summary_lines": [
            "<b>Aduana Única:</b> TODO tráfico de EP-01..06 entra por Port 443 TLS 1.3 + WAF OWASP",
            "<b>Auth Stateless:</b> /api/v1/auth/jwt/login/ + refresh exp 15m HMAC-SHA256 (RNF-0013)",
            "<b>Enrutamiento:</b> NGINX → Django 5 DRF :8000 (REST) + Daphne ASGI (WSS Alertas)",
            "<b>RNF:</b> RNF-0001, RNF-0012, RNF-0013, RNF-0014, RNF-0015, RNF-0025",
        ],
        "apis": [
            {"method": "POST", "endpoint": "/api/v1/auth/jwt/login/ & /refresh/", "auth": "Público TLS 1.3 (RateLimit 100/m)", "purpose": "Emisión de tokens JWT con claims de rol (ACT-0001..0005 / Tutor / Médico) exp 15m (RNF-0013)", "sla": "< 300 ms"},
            {"method": "ALL", "endpoint": "/api/v1/* (Django 5 DRF :8000)", "auth": "Bearer JWT + RBAC RoleGuard", "purpose": "Enrutamiento centralizado hacia B1..B10 dentro de Subred Privada App VPC (RNF-0012, 0015)", "sla": "<= 2.0 s"},
            {"method": "WSS", "endpoint": "wss://vitalis.pe/ws/* (Daphne ASGI)", "auth": "JWT Subprotocol + Pub/Sub", "purpose": "Canal tiempo real hacia EP-03/05 para Alerta Roja SpO2<92% (RNF-0006, 0027)", "sla": "< 150 ms"},
        ],
        "tbs": ["TB_USUARIOS", "TB_PERMISOS"],
        "extra_tags": ["RNF-0001", "RNF-0012", "RNF-0013", "RNF-0014", "RNF-0015", "RNF-0025", "RNF-0026"],
    },
    {
        "id": "B1",
        "code": "B1",
        "title": "B1. Pacientes y Apoderados",
        "subtitle": "Capa 3 • Filiación Pediátrica y Patria Potestad",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [1190, 685, 470, 225],
        "gui_strip": "GUIs ACÁ: GUI-0007 (Pacientes: MDL-0031..35) • GUI-0014 (Apoderados: MDL-0066..69)",
        "summary_lines": [
            "<b>EDUs (2):</b> EDU-0014 (Pacientes), EDU-0021 (Apoderados) • <b>Entrada:</b> EP-01, EP-02",
            "<b>Ilaciones/ESP (8):</b> ILA-0025..0028, 0053..0056 | <b>Pruebas:</b> T-001, T-005, T-006",
            "<b>Reglas:</b> Edad auto, TEA/TDAH, Activo/Inactivo/Reingreso, ≤2° consanguinidad",
            "<b>Tablas & RNF:</b> TB_PACIENTES, TB_APODERADOS | RNF-0002 (AES-256), RNF-0005 (<=1.5s)",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/pacientes/", "auth": "JWT (EP-01 Tutor / EP-02 Admin / EP-03)", "purpose": "Filiación pediátrica, cálculo de edad en tiempo real, estado Reingreso, Soft Delete (ILA-0025..0028)", "sla": "<= 1.5 s"},
            {"method": "CRUD", "endpoint": "/api/v1/apoderados/", "auth": "JWT (EP-01 / EP-02)", "purpose": "Vínculo de DNI, celular y parentesco hasta 2° grado con múltiples apoderados (ILA-0053..0056)", "sla": "<= 1.5 s"},
        ],
        "tbs": ["TB_PACIENTES", "TB_APODERADOS", "TB_USUARIOS"],
        "extra_tags": ["EDU-0014", "EDU-0021", "GUI-0007", "GUI-0014", "RNF-0002", "RNF-0005"],
    },
    {
        "id": "B2",
        "code": "B2",
        "title": "B2. Pre-Triaje, Consentimiento y Motor Pizarra",
        "subtitle": "Capa 3 • Habilitación Clínica & Blackboard (RNF-0027)",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [1190, 995, 470, 275],
        "gui_strip": "GUIs ACÁ: GUI-0016 / TRIAJE_001 (MDL-0076..79) • GUI-0020 (Consent.: MDL-0096..0100)",
        "summary_lines": [
            "<b>EDUs (2):</b> EDU-0023 (Pre-Triaje), EDU-0029 (Consentimiento) • <b>Entrada:</b> EP-01, EP-02",
            "<b>Ilaciones/ESP (8):</b> ILA-0062..0065, 0078..0081 • <b>BPM:</b> Bonita ILA-0062 (4 carriles)",
            "<b>Pizarra RNF-0027:</b> 4 KSs (KS_AlertaRoja SpO2<92%, KS_Neuropediatria, KS_Bioética, KS_Disp)",
            "<b>Reglas & RNF:</b> Constraint BD acta (RNF-0010), Alerta WSS vía B0 (RNF-0006, 0024)",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/pretriage/", "auth": "JWT (EP-01 / EP-02 / Enfermería)", "purpose": "Captura signos vitales/antecedentes, evalúa Pizarra KSs y dispara Alerta Roja (ILA-0062..0065)", "sla": "< 2.0 s"},
            {"method": "CRUD", "endpoint": "/api/v1/consentimientos/", "auth": "JWT + MinIO Presigned URL 300s", "purpose": "Descarga plantilla y subida acta firmada SHA-256 obligatoria antes de cita (ILA-0078..0081)", "sla": "< 2.0 s"},
            {"method": "WSS", "endpoint": "wss://vitalis.pe/ws/alertas-rojas/", "auth": "JWT + Redis Pub/Sub → B0", "purpose": "Push prioritario no descartable hacia EP-03 y EP-05 ante SpO2<92% (RNF-0006, 0027)", "sla": "< 150 ms"},
        ],
        "tbs": ["TB_PRETRIAJE_CLINICO", "TB_CONSENTIMIENTOS", "TB_CITAS", "TB_APODERADOS"],
        "extra_tags": ["EDU-0023", "EDU-0029", "GUI-0016", "GUI-0020", "RNF-0006", "RNF-0010", "RNF-0021", "RNF-0024", "RNF-0027"],
    },
    {
        "id": "B3",
        "code": "B3",
        "title": "B3. Especialistas, Tarifas y Horarios",
        "subtitle": "Capa 3 • Oferta Clínica y Bloques de Agenda",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [1190, 1355, 470, 225],
        "gui_strip": "GUIs ACÁ: GUI-0009 (Especialistas: MDL-0041..45) • GUI-0010 (Horarios: MDL-0046..49)",
        "summary_lines": [
            "<b>EDUs (2):</b> EDU-0016 (Especialistas/Tarifas), EDU-0017 (Horarios) • <b>Entrada:</b> EP-02, EP-03",
            "<b>Ilaciones/ESP (8):</b> ILA-0033..0040 | <b>Pruebas:</b> T-001, T-006, T-017 Rendimiento",
            "<b>Reglas:</b> Vista semanal ocupado/libre/bloqueado, tarifa individual, feriados",
            "<b>API SLA:</b> GET /horarios/disponibilidad <= 2.0s (RNF-0015), Anticolisión (RNF-0004)",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/especialistas/", "auth": "JWT (EP-02 Admin / Consulta Auth)", "purpose": "Registro CMP/RNE, especialidad, tipo terapia y tarifa_individual (ILA-0033..0036)", "sla": "< 1.5 s"},
            {"method": "GET/CRUD", "endpoint": "/api/v1/horarios/disponibilidad/", "auth": "JWT (EP-01..03)", "purpose": "Consulta rápida franjas libres/ocupadas sin superposición (ILA-0037..0040, RNF-0015)", "sla": "<= 2.0 s"},
        ],
        "tbs": ["TB_ESPECIALISTAS", "TB_ESPECIALIDADES", "TB_TIPO_TERAPIA", "TB_HORARIOS", "TB_BLOQUES_HORARIOS"],
        "extra_tags": ["EDU-0016", "EDU-0017", "GUI-0009", "GUI-0010", "RNF-0004", "RNF-0015"],
    },
    {
        "id": "B10",
        "code": "B10",
        "title": "B10. Permisos RBAC y Auditoría Forense",
        "subtitle": "Capa 3 • Seguridad Transversal y Logs Inmutables",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [1190, 1665, 470, 225],
        "gui_strip": "GUIs ACÁ: GUI-0002 (Historial: MDL-0006..09) • GUI-0004 (Permisos RBAC: MDL-0016..20)",
        "summary_lines": [
            "<b>EDUs (2):</b> EDU-0009 (Historial Cambios), EDU-0011 (Permisos) • <b>Entrada:</b> EP-04 + B0",
            "<b>Ilaciones/ESP (8):</b> ILA-0005..0008, 0013..0016 • <b>Pruebas:</b> T-012 Seguridad, T-006",
            "<b>Reglas:</b> Herencia automática por rol, bloqueo no autorizado, logs IP + UTC inmutables",
            "<b>Tablas & RNF:</b> TB_PERMISOS, TB_HISTORIAL_CITAS, audit_logs | RNF-0001, 0003, 0013",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/permisos/roles/", "auth": "JWT (Solo EP-04 ACT-0001)", "purpose": "Matriz permisos heredables por rol sobre módulos y GUIs (ILA-0013..0016, RNF-0001)", "sla": "< 1.0 s"},
            {"method": "GET/POST", "endpoint": "/api/v1/auditoria/historial-citas/", "auth": "JWT (EP-04 Gerencia/Auditor)", "purpose": "Consulta e inserción inmutable IP + UTC de cambios de estado y citas (ILA-0005..0008, RNF-0003)", "sla": "< 1.5 s"},
        ],
        "tbs": ["TB_PERMISOS", "TB_PERMISOS_001", "TB_HISTORIAL_CITAS", "TB_USUARIOS"],
        "extra_tags": ["EDU-0009", "EDU-0011", "GUI-0002", "GUI-0004", "RNF-0001", "RNF-0003", "RNF-0013", "RNF-0025"],
    },
    {
        "id": "CTX-CAT",
        "code": "CATÁLOGO v01",
        "title": "Gobierno Catálogo, ESP & Pruebas Software",
        "subtitle": "Línea Base Integral • RuwayLabs / EPIS-UNSA",
        "capa": "Transversal",
        "kind": "dashed",
        "rect": [1190, 1975, 470, 200],
        "gui_strip": "GUI-0015 / EDU-0022 (en blanco base: MDL-0071..0075) • 27/28 GUIs activas",
        "summary_lines": [
            "<b>Orgs/Actores:</b> ORG-0001..0003 • ACT-0001..0005 • EXP-0001 (Dr. P. Huertas)",
            "<b>Requisitos:</b> 27 EDU • 108 ILA + Riesgos • 104 ESP llenas (+4 vacías ESP-0013..16)",
            "<b>Calidad:</b> 113 filas Pruebas (T-001..T-020) • 28 Entradas RNF (01..27)",
        ],
        "apis": [],
        "tbs": [],
        "extra_tags": ["GUI-0015", "ORG-0001..0003", "ACT-0001..0005", "T-001..T-020"],
    },

    # COL 4: SISTEMA CENTRO (B5, B4 NÚCLEO, B11 PG16, B12 MINIO/REDIS)
    {
        "id": "B5",
        "code": "B5",
        "title": "B5. Videoconferencia y Telemedicina",
        "subtitle": "Capa 3 • Aprovisionamiento Salas WebRTC / Meet",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [1880, 375, 480, 185],
        "gui_strip": "GUI ACÁ: GUI-0012 (Videoconf.: MDL-0056..0059, 0060 blanco) ↔ EP-05",
        "summary_lines": [
            "<b>Requisitos:</b> EDU-0019 (ILA-0045..0048) • GUI-0012 • <b>Entrada:</b> EP-05 + B4",
            "<b>Motor:</b> Integración OAuth2 Google Meet API + W3C MediaDevices WebRTC",
            "<b>Reglas:</b> Generación automática al confirmar cita virtual; regeneración si falla",
            "<b>RNF:</b> RNF-0008 (Sincronización), RNF-0014 (TLS 1.3), RNF-0019 (Blink/Gecko/WebKit)",
        ],
        "apis": [
            {"method": "POST", "endpoint": "/api/v1/teleconsulta/salas/", "auth": "JWT (EP-02 / B4 Confirmación)", "purpose": "Invoca Google Meet API OAuth2 y guarda meet_url + PIN en cita virtual (ILA-0045)", "sla": "< 2.5 s"},
            {"method": "GET/PUT", "endpoint": "/api/v1/teleconsulta/salas/{id}/ & /regenerar/", "auth": "JWT (EP-05 Tutor/Médico)", "purpose": "Consulta o regeneración de enlace expirado (ILA-0046, ILA-0047)", "sla": "< 1.5 s"},
        ],
        "tbs": ["TB_CITAS", "TB_ENLACES_VIDEOCONFERENCIA*"],
        "extra_tags": ["EDU-0019", "GUI-0012", "EP-05", "RNF-0008", "RNF-0019"],
    },
    {
        "id": "B4",
        "code": "B4 • NÚCLEO",
        "title": "B4. GESTIÓN DE CITAS Y AGENDAS",
        "subtitle": "NÚCLEO ORQUESTADOR CENTRAL DE COMPORTAMIENTO (CAPA 3)",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "hub",
        "rect": [1865, 685, 530, 505],
        "gui_strip": "GUIs ACÁ: GUI-0001 (Estados), GUI-0005 (Citas), GUI-0006 (Reprog.), GUI-0011 (Modalidad) • 20 MDL",
        "summary_lines": [
            "<b>EDUs (4):</b> EDU-0008 (Estados), EDU-0012 (Citas), EDU-0013 (Reprog.), EDU-0018 (Modalid.)",
            "<b>Ilaciones/ESP (16):</b> ILA-0001..0004, 0017..0024, 0041..0044 • <b>BPM:</b> Bonita ILA-0017 (5 carriles)",
            "<b>Entradas:</b> EP-01 (Tutor PWA), EP-02 (Admisión ACT-0005), EP-03 (Médico) vía B0",
            "<b>Autómata 8 Estados:</b> Solicitada/Pendiente → Confirmada → Atendida/Cancelada/No asistió",
            "<b>Anticolisión & Ventana:</b> SELECT FOR UPDATE <2s (RNF-0004), Ventana >=24h / 8am,",
            "<b>Saldo & Modalidad:</b> -1 sesión automática al marcar Atendida (EDU-0012/0033) • Presencial/Virtual/Domicilio",
            "<b>RNF Vinculados:</b> RNF-0003, 0004, 0007, 0010, 0011, 0015, 0021 • <b>Pruebas:</b> T-006, T-017",
        ],
        "apis": [
            {"method": "POST", "endpoint": "/api/v1/citas/ (SERIALIZABLE / SELECT FOR UPDATE)", "auth": "JWT (EP-01 Tutor / EP-02 Admin)", "purpose": "Valida Pre-triaje (B2), Consentimiento (RNF-0010), Saldo paquete (B8) y bloquea horario (ILA-0017)", "sla": "< 2.0 s (RNF-0004)"},
            {"method": "PATCH", "endpoint": "/api/v1/citas/{id}/estado/", "auth": "JWT (EP-03 / EP-02)", "purpose": "Ejecuta FSM estados; bloquea cambios si estado==Atendida y descuenta 1 sesión (ILA-0001..0004)", "sla": "< 1.0 s"},
            {"method": "POST", "endpoint": "/api/v1/citas/{id}/reprogramar/", "auth": "JWT (EP-01 / EP-02)", "purpose": "Regla >=24h (o 8:00 am día cita), soporte Drag&Drop (RNF-0007) y aviso WhatsApp (ILA-0021..0024)", "sla": "< 1.5 s"},
            {"method": "CRUD", "endpoint": "/api/v1/citas/{id}/modalidad/", "auth": "JWT", "purpose": "Asigna Presencial, Virtual (dispara B5 Meet) o Domicilio con dirección verificada (ILA-0041..0044)", "sla": "< 1.0 s"},
        ],
        "tbs": ["TB_CITAS", "TB_HISTORIAL_CITAS", "TB_BLOQUES_HORARIOS", "TB_HORARIOS", "TB_REPROGRAMACIONES*"],
        "extra_tags": ["EDU-0008", "EDU-0012", "EDU-0013", "EDU-0018", "GUI-0001", "GUI-0005", "GUI-0006", "GUI-0011", "RNF-0004", "RNF-0007", "RNF-0010", "RNF-0021"],
    },
    {
        "id": "B11",
        "code": "B11 • REPOSITORIO BD",
        "title": "B11. REPOSITORIO CENTRAL VITALIS_BD",
        "subtitle": "Capa 4 (Zona 4 Datos): PostgreSQL 16 ACID + PgBouncer (27 TB_*)",
        "capa": "Capa 4: Persistencia, Storage y Pizarra",
        "kind": "hub",
        "rect": [1865, 1320, 530, 320],
        "gui_strip": "Persistencia compartida para las 27 GUIs activas • Subred Privada (TCP 6432 → 5432)",
        "summary_lines": [
            "<b>Motor & Pool:</b> PostgreSQL 16.2 (5432) + PgBouncer 1.22 (6432, pool 50 → 1000 conn)",
            "<b>Políticas BD:</b> ACID estricto, Soft Delete (eliminacion_logica=false), AES-256 PII menores",
            "<b>Anticolisión & Bioética:</b> SELECT FOR UPDATE (RNF-0004), Constraint Consentimiento (RNF-0010)",
            "<b>Alta Disponibilidad:</b> Ubuntu 24.04 (4 vCPU/16GB/NVMe 3k IOPS), WAL RPO<=15m RTO<=30m",
            "<b>Tablas (27):</b> TB_CITAS, TB_PACIENTES, TB_HISTORIAS_CLINICAS, TB_PRETRIAJE_CLINICO, TB_PAGOS...",
            "<b>RNF:</b> RNF-0002, 0003, 0004, 0005, 0010, 0011, 0020, 0025 • <b>Plantilla 6:</b> Estilo Repositorio",
        ],
        "apis": [
            {"method": "SQL/TLS", "endpoint": "postgresql://pgbouncer.vpc.local:6432/vitalis_bd", "auth": "mTLS + Role App VPC", "purpose": "Pool transaccional único hacia las 27 tablas normalizadas en Subred Privada VPC (RNF-0011, 0025)", "sla": "Query <= 15 ms"},
            {"method": "WAL", "endpoint": "PostgreSQL Streaming Replication -> Standby NVMe", "auth": "Subred Privada", "purpose": "Respaldo continuo WAL con RPO <= 15 min y RTO <= 30 min (RNF-0020)", "sla": "RPO <= 15m"},
        ],
        "tbs": [
            "TB_PACIENTES", "TB_APODERADOS", "TB_USUARIOS", "TB_PERMISOS", "TB_PERMISOS_001",
            "TB_ESPECIALISTAS", "TB_ESPECIALIDADES", "TB_TIPO_TERAPIA", "TB_HORARIOS", "TB_BLOQUES_HORARIOS",
            "TB_CITAS", "TB_HISTORIAL_CITAS", "TB_PRETRIAJE_CLINICO", "TB_CONSENTIMIENTOS",
            "TB_HISTORIAS_CLINICAS", "TB_NOTAS_EVOLUCION", "TB_DIAGNOSTICOS", "TB_RECETAS",
            "TB_DOCUMENTOS_COMPLEMENTARIOS", "TB_DERIVACIONES", "TB_INTERCONSULTAS",
            "TB_PAQUETES_SESIONES", "TB_DESCUENTOS", "TB_PAGOS", "TB_COMPROBANTES",
            "TB_LIQUIDACIONES", "TB_RECORDATORIOS_CITA"
        ],
        "extra_tags": ["RNF-0002", "RNF-0003", "RNF-0004", "RNF-0005", "RNF-0010", "RNF-0011", "RNF-0020", "RNF-0025"],
    },
    {
        "id": "B12",
        "code": "B12 • BLACKBOARD & S3",
        "title": "B12. MinIO S3 Storage + Bus Blackboard Redis / Celery",
        "subtitle": "Capa 4 (Zona 4 Datos): BLOBs AES-256 & Pizarra/Colas",
        "capa": "Capa 4: Persistencia, Storage y Pizarra",
        "kind": "normal",
        "rect": [1865, 1715, 530, 315],
        "gui_strip": "Soporta archivos/alertas en GUI-0016, 0017, 0019, 0020, 0026, 0027, 0028 (URLs 300s)",
        "summary_lines": [
            "<b>MinIO S3 (TCP 9000):</b> Cifrado SSE AES-256 + Presigned URLs TTL 300s (RNF-0024)",
            "<b>5 Buckets:</b> consentimientos • doc-adjuntos • recetas • vouchers • comprobantes-sunat-cpe",
            "<b>Redis 7.2 (TCP 6379):</b> Pizarra Blackboard (HSET signos/KS) + Pub/Sub WSS (RNF-0027)",
            "<b>Celery 5.4 + Beat:</b> Worker avisos T-24h (B6) & Batch liquidaciones mensuales (B9)",
            "<b>RNF:</b> RNF-0006, 0009, 0012, 0024, 0025, 0026, 0027 • <b>Plantilla 6:</b> Estilo Pizarra",
        ],
        "apis": [
            {"method": "S3 API", "endpoint": "https://minio.vpc.local:9000/{bucket} (Presigned 300s)", "auth": "IAM Key + AES-256", "purpose": "Resguardo aislado de PDFs, imágenes médicas, vouchers y XML/CDR SUNAT (RNF-0024)", "sla": "TTL <= 300s"},
            {"method": "REDIS", "endpoint": "redis://redis.vpc.local:6379/0 (Blackboard & Celery)", "auth": "Subred Privada ACL", "purpose": "Memoria compartida Pizarra (RNF-0027), canales WSS Alerta Roja y broker Celery 5.4 (RNF-0026)", "sla": "< 5 ms"},
        ],
        "tbs": ["bucket:vitalis-consentimientos", "bucket:vitalis-doc-adjuntos", "bucket:vitalis-recetas-firmadas", "bucket:vitalis-vouchers", "bucket:vitalis-comprobantes-sunat-cpe", "redis:blackboard:pretriage:*"],
        "extra_tags": ["RNF-0006", "RNF-0009", "RNF-0024", "RNF-0025", "RNF-0026", "RNF-0027"],
    },

    # COL 5: SISTEMA DERECHA (B6, B7, B8 TUBERÍAS, B9 LOTES, INFRA-STD)
    {
        "id": "B6",
        "code": "B6",
        "title": "B6. Mensajería de Citas y Avisos T-24h",
        "subtitle": "Capa 3 • Notificaciones Masivas y Reintentos Celery",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [2560, 375, 530, 185],
        "gui_strip": "GUI ACÁ: GUI-0013 (Mensajería: MDL-0061..0064, 0065 blanco) • Entrada EP-02 & EP-06",
        "summary_lines": [
            "<b>Requisitos:</b> EDU-0020 (ILA-0049..0052) • GUI-0013 • <b>Disparadores:</b> EP-06 Cron + B4",
            "<b>Canales:</b> WhatsApp Cloud API y Telefonía automatizada 24h antes (T-24h)",
            "<b>Estados:</b> Enviado / Fallido / Pendiente + reenvío manual (EP-02)",
            "<b>RNF:</b> RNF-0009 (Automatización T-24h), RNF-0026 (Celery 5.4 + Redis Broker)",
        ],
        "apis": [
            {"method": "POST", "endpoint": "/api/v1/notificaciones/programar/", "auth": "EP-06 Celery Beat / B4", "purpose": "Programa recordatorio T-24h con fecha, especialista, modalidad y enlace Meet (ILA-0049)", "sla": "Async < 1s"},
            {"method": "GET/POST", "endpoint": "/api/v1/notificaciones/ & /{id}/reenviar/", "auth": "JWT (EP-02 Admin/Asistente)", "purpose": "Monitoreo de estados Enviado/Fallido y reenvío manual (ILA-0050..0052)", "sla": "< 1.5 s"},
        ],
        "tbs": ["TB_RECORDATORIOS_CITA", "TB_CITAS", "TB_USUARIOS"],
        "extra_tags": ["EDU-0020", "GUI-0013", "EP-06", "RNF-0009", "RNF-0026"],
    },
    {
        "id": "B7",
        "code": "B7",
        "title": "B7. Historia Clínica Digital, Diagnósticos, Recetas e Interconsultas",
        "subtitle": "Capa 3 • Expediente Pediátrico Integral (8 EDUs • 40 Modales GUI)",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [2560, 685, 550, 390],
        "gui_strip": "GUIs ACÁ (8): GUI-0003, GUI-0008, GUI-0017, GUI-0018, GUI-0019, GUI-0021, GUI-0022, GUI-0025",
        "summary_lines": [
            "<b>EDUs (8):</b> EDU-0010 (Val. Deriv), 0015 (Deriv), 0025 (Docs), 0027 (Interc), 0028 (Recetas), 0030 (CIE-10/DSM-5), 0032 (HCE), 0035 (Evolución)",
            "<b>Ilaciones/ESP (32):</b> ILA-0009..0012, 0029..0032, 0066..0077, 0082..0089, 0098..0101 • <b>Entrada:</b> EP-03",
            "<b>Reglas Clínicas:</b> Plantillas por especialidad, Bloqueo 72h + Log versiones, Exclusión",
            "psicológicos complejos en derivación, Interconsulta expira 7d, Tags TDAH/Lenguaje, Aviso fármaco.",
            "<b>RNF:</b> RNF-0001 (ACL+Vencim), RNF-0002 (AES-256), RNF-0005 (<=1.5s), RNF-0006 (Alerta WSS), RNF-0024",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/historias/ & /evoluciones/", "auth": "JWT (EP-03 Especialista)", "purpose": "HCE por especialidad y notas con bloqueo edición tras 72h + log versiones (ILA-0086..0089, 0098..0101)", "sla": "<= 1.5 s (RNF-0005)"},
            {"method": "CRUD", "endpoint": "/api/v1/diagnosticos-cie10/ & /recetas/", "auth": "JWT (EP-03 Especialista)", "purpose": "Catálogos CIE-10/DSM-5 obligatorios + alerta fármaco activo en Perfil Básico (ILA-0074..0077, 0082..0085)", "sla": "< 1.5 s"},
            {"method": "CRUD", "endpoint": "/api/v1/documentos-adjuntos/", "auth": "JWT + RNF-0001 ACL + MinIO 300s", "purpose": "Subida/descarga PDF/foto informes neurológicos y peritajes protegidos (ILA-0066..0069, RNF-0024)", "sla": "< 2.0 s"},
            {"method": "CRUD", "endpoint": "/api/v1/derivaciones/ & /interconsultas/", "auth": "JWT + RNF-0001 (Expira 7d)", "purpose": "Validación contra casos complejos y junta médica interdisciplinaria (ILA-0009..0012, 0029..0032, 0070..0073)", "sla": "< 1.5 s"},
        ],
        "tbs": ["TB_HISTORIAS_CLINICAS", "TB_NOTAS_EVOLUCION", "TB_DIAGNOSTICOS", "TB_RECETAS", "TB_DOCUMENTOS_COMPLEMENTARIOS", "TB_DERIVACIONES", "TB_INTERCONSULTAS", "TB_TIPO_TERAPIA"],
        "extra_tags": ["EDU-0010", "EDU-0015", "EDU-0025", "EDU-0027", "EDU-0028", "EDU-0030", "EDU-0032", "EDU-0035", "GUI-0003", "GUI-0008", "GUI-0017", "GUI-0018", "GUI-0019", "GUI-0021", "GUI-0022", "GUI-0025", "RNF-0001", "RNF-0005"],
    },
    {
        "id": "B8",
        "code": "B8 • PIPES & FILTERS",
        "title": "B8. Paquetes, Pagos y SUNAT UBL 2.1 (Tuberías y Filtros)",
        "subtitle": "Capa 3 • Motor Financiero Dual & Pipeline UBL 2.1 (Plantilla 8)",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [2560, 1145, 550, 360],
        "gui_strip": "GUIs ACÁ (4): GUI-0023 (Paquetes), GUI-0024 (Dsctos), GUI-0026 (Pagos), GUI-0027 (Facturación) • 20 MDL",
        "summary_lines": [
            "<b>EDUs (4):</b> EDU-0033 (Paq), 0034 (Dsctos), 0036 (Pagos), 0037 (SUNAT) • <b>BPM:</b> Bonita ILA-0106",
            "<b>Entradas:</b> EP-02 (Caja), EP-01 (Pago PWA), EP-06 (Webhook PCI-DSS /pagos/cb → B0)",
            "<b>Pipeline Tuberías y Filtros (EDU-0037):</b> [1 Validador DNI/RUC] → [2 XML UBL 2.1] → [3 Firma X.509] → [4 ZIP] → [5 SOAP OSE] → [6 CDR + QR <3s]",
            "<b>Reglas Paquetes/Control Interno:</b> Unipersonal 90d, devolución por abandono, Control Interno paralelo sin alterar SUNAT.",
            "<b>RNF:</b> RNF-0011 (ACID), RNF-0014 (TLS 1.3), RNF-0021 (Bonita), RNF-0023 (SUNAT), RNF-0024 (MinIO)",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/paquetes/ & /descuentos/", "auth": "JWT (EP-02 Admin / Asistente)", "purpose": "Paquetes inmutables 90d unipersonales, saldo >0 obligatorio y descuentos %/fijo (ILA-0090..0097)", "sla": "< 1.0 s"},
            {"method": "CRUD", "endpoint": "/api/v1/pagos/ & /devoluciones/ (+ Hook EP-06)", "auth": "JWT + MinIO Voucher + HMAC", "purpose": "Registro pago 5 medios con voucher y conciliación vía Webhook /pagos/cb (ILA-0102..0105)", "sla": "< 2.0 s"},
            {"method": "POST", "endpoint": "/api/v1/facturacion/cpe/ & /control-interno/", "auth": "JWT (EP-02) + Certificado X.509", "purpose": "Tubería UBL 2.1 en 6 filtros hacia OSE/SUNAT + módulo paralelo de control interno (ILA-0106..0109, RNF-0023)", "sla": "< 3.0 s"},
        ],
        "tbs": ["TB_PAQUETES_SESIONES", "TB_DESCUENTOS", "TB_PAGOS", "TB_COMPROBANTES", "TB_PACIENTES"],
        "extra_tags": ["EDU-0033", "EDU-0034", "EDU-0036", "EDU-0037", "GUI-0023", "GUI-0024", "GUI-0026", "GUI-0027", "RNF-0011", "RNF-0021", "RNF-0023", "RNF-0024"],
    },
    {
        "id": "B9",
        "code": "B9 • BATCH SECUENCIAL",
        "title": "B9. Liquidación Mensual Profesionales (Lotes Secuenciales)",
        "subtitle": "Capa 3 • Motor Contable Batch en 4 Etapas (Plantilla 8 • EDU-0038)",
        "capa": "Capa 3: Lógica Clínica y Subsistemas",
        "kind": "normal",
        "rect": [2560, 1575, 550, 265],
        "gui_strip": "GUI ACÁ: GUI-0028 (Liquidación Profesional: MDL-0136..0140) • Entradas EP-06 & EP-04",
        "summary_lines": [
            "<b>EDU (1):</b> EDU-0038 • <b>Ilaciones/ESP (4):</b> ILA-0110..0113 • <b>GUI:</b> GUI-0028 (5 MDL)",
            "<b>Lotes Secuenciales (4 Fases):</b> [Lote 1 Citas 'Atendida'] → [Lote 2 Tarifación modalidad] → [Lote 3 Comisión 20% + Retención 8%] → [Lote 4 Cierre TB_LIQUIDACIONES + PDF]",
            "<b>Flujo:</b> Cron EP-06 Celery → 'Pendiente_aprobacion' → Aprobación EP-04 Gerencia",
            "<b>RNF:</b> RNF-0003, RNF-0011, RNF-0024, RNF-0026",
        ],
        "apis": [
            {"method": "CRUD", "endpoint": "/api/v1/liquidaciones/ & /{id}/aprobar/", "auth": "EP-06 Cron + JWT EP-04 Gerencia", "purpose": "Ejecución en 4 lotes secuenciales y flujo gerencial de aprobación mensual (ILA-0110..0113)", "sla": "Batch Celery"},
            {"method": "GET", "endpoint": "/api/v1/liquidaciones/{id}/reporte-pdf/", "auth": "JWT + MinIO Presigned URL", "purpose": "Descarga segura PDF consolidado de honorarios (RNF-0024)", "sla": "< 2.0 s"},
        ],
        "tbs": ["TB_LIQUIDACIONES", "TB_CITAS", "TB_ESPECIALISTAS", "TB_USUARIOS"],
        "extra_tags": ["EDU-0038", "GUI-0028", "EP-04", "EP-06", "RNF-0003", "RNF-0011", "RNF-0024", "RNF-0026"],
    },
    {
        "id": "INFRA-STD",
        "code": "INFRA & RNF",
        "title": "Estándares Técnicos, Infraestructura y Equipo Codificadores",
        "subtitle": "Marco Transversal ISO/IEC 25010 (RNF-0012, 0016..0022, 0025, 0026)",
        "capa": "Transversal",
        "kind": "dashed",
        "rect": [2560, 1910, 550, 275],
        "gui_strip": "Reglas UI transversales: Heurísticas Nielsen, 8 Reglas Oro Shneiderman y W3C/WCAG",
        "summary_lines": [
            "<b>Stack Oficial (RNF-0012/0026):</b> React 18+TS 5.4+Vite+Tailwind PWA | Python 3.12+Django 5+DRF+Daphne+Celery",
            "<b>Hardware Cliente (RNF-0016/0017):</b> i5/Ryzen 5, 8-16GB RAM, SSD 256GB, Win10/11 Pro, pagefile.sys 1.5x-2x, V8 <=350MB",
            "<b>Móvil & Motores (RNF-0018/0019):</b> Android 11+/iOS 15+ PWA + SessionStorage | Blink, Gecko, WebKit",
            "<b>Servidores & Red (RNF-0020/0025):</b> Ubuntu 24.04 + Docker 26 | DMZ :443 + Subred Privada VPC",
            "<b>Modelado & Equipo (RNF-0021/0022/0026):</b> Bonita BPM 2024.1 + UML 2.5 + Arquitectura granular Full-Stack",
        ],
        "apis": [],
        "tbs": [],
        "extra_tags": ["RNF-0012", "RNF-0016", "RNF-0017", "RNF-0018", "RNF-0019", "RNF-0020", "RNF-0021", "RNF-0022", "RNF-0025", "RNF-0026"],
    },

    # DERECHA: ENTRY POINT CLÍNICO EP-03 + ACTOR EXT-A3 + APIS EXTERNAS EXT-API3, EXT-API4
    {
        "id": "EP-03",
        "code": "ENTRY POINT EP-03",
        "title": "Estación Clínica (/app/medico/*)",
        "subtitle": "Frontend React SPA Especialista + RoleGuard + RNF-0001 ACL",
        "capa": "Entry Points y Canales",
        "kind": "entry",
        "rect": [3210, 375, 330, 255],
        "gui_strip": "GUIs ACÁ (8): GUI-0003, 0008, 0017, 0018, 0019, 0021, 0022, 0025 + GUI-0010",
        "summary_lines": [
            "<b>Quién entra:</b> EXT-A3 (Médicos/Nutrición/Psicología/Terapias; Jefes ACT-0002..0004)",
            "<b>Rutas Fig 7.1:</b> /app/medico/* (/portal-especialista/*, /agenda, /historia-clinica/:id)",
            "<b>Autenticación obligatoria:</b> Todo tráfico pasa por B0 (JWT + ACL RNF-0001) hacia B4/B7",
        ],
        "apis": [
            {"method": "ENTRY", "endpoint": "https://vitalis.pe/app/medico/* & wss://.../ws/alertas-rojas/", "auth": "JWT Especialista + RNF-0001 ACL", "purpose": "Portal clínico unificado con recepción en vivo de Alerta Roja WSS y editor CIE-10 (<72h)", "sla": "<= 1.5 s"},
        ],
        "tbs": [],
        "extra_tags": ["GUI-0003", "GUI-0008", "GUI-0017", "GUI-0018", "GUI-0019", "GUI-0021", "GUI-0022", "GUI-0025", "RNF-0001", "RNF-0005", "RNF-0006"],
    },
    {
        "id": "EXT-A3",
        "code": "EXT-A3",
        "title": "Especialista Clínico (ACT-0002..04)",
        "subtitle": "Actor Operativo + Jefaturas • Consultorio & Domicilio",
        "capa": "Capa 1: Presentación y Actores",
        "kind": "ext",
        "rect": [3715, 375, 330, 255],
        "gui_strip": "ENTRA POR: EP-03 (/app/medico/*) y EP-05 (/app/teleconsulta/:id)",
        "summary_lines": [
            "<b>Disciplinas:</b> Medicina, Nutrición, Psicología, Terapias (Jefaturas ACT-0002..0004)",
            "<b>Dispositivos:</b> PC Consultorio i5 (RNF-0016/17) y Tablet Domicilio PWA (RNF-0018)",
            "<b>Registra & Ve:</b> Evolución (<72h), CIE-10, Recetas, Adjuntos, Alerta Roja WSS",
        ],
        "apis": [
            {"method": "ACTOR", "endpoint": "Entra vía EP-03 (/app/medico/*) & EP-05 (/app/teleconsulta/:id)", "auth": "JWT Especialista + ACL RNF-0001", "purpose": "Atención clínica presencial, remota WebRTC y domiciliaria autenticada en B0", "sla": "<= 1.5 s"},
        ],
        "tbs": [],
        "extra_tags": ["ACT-0002", "ACT-0003", "ACT-0004", "EP-03", "EP-05", "RNF-0001", "RNF-0005", "RNF-0006"],
    },
    {
        "id": "EXT-API3",
        "code": "EXT-API3",
        "title": "SUNAT / PSE-OSE API",
        "subtitle": "Ente Tributario Capa 5 • Facturación UBL 2.1",
        "capa": "Capa 5: APIs Externas",
        "kind": "ext",
        "rect": [3260, 1145, 455, 165],
        "gui_strip": "Disparado desde GUI-0027 (Facturación SUNAT: MDL-0131..0135) vía Tubería B8",
        "summary_lines": [
            "<b>Estándar:</b> OASIS XML UBL 2.1 + Firma Digital X.509 v3 (RNF-0023)",
            "<b>Transporte:</b> SOAP / REST sobre HTTPS TLS 1.3 (RNF-0014)",
            "<b>Retorno:</b> Constancia de Recepción (CDR) Aceptado/Anulado < 3.0s",
        ],
        "apis": [
            {"method": "SOAP/REST", "endpoint": "https://ose.sunat.gob.pe/ol-ti-itcpe/billService", "auth": "Certificado Tributario X.509 v3 + Sol", "purpose": "Recepción de ZIP XML UBL 2.1 de Boletas/Facturas y emisión de CDR oficial (ILA-0106, RNF-0023)", "sla": "< 3.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["EDU-0037", "GUI-0027", "RNF-0014", "RNF-0023"],
    },
    {
        "id": "EXT-API4",
        "code": "EXT-API4",
        "title": "Pasarelas de Pago PCI-DSS",
        "subtitle": "Entidad Financiera Capa 5 • Medios de Pago",
        "capa": "Capa 5: APIs Externas",
        "kind": "ext",
        "rect": [3260, 1380, 455, 175],
        "gui_strip": "Usado en GUI-0026 (Pagos: MDL-0126..0130) • Webhook retorna por EP-06 → B0",
        "summary_lines": [
            "<b>Canales:</b> Tarjetas (Niubiz/Izipay PCI-DSS v4.0), Yape, Plin, Transferencia, Efectivo",
            "<b>Seguridad:</b> Salida B8 HTTPS TLS 1.3 ↔ Webhook entra vía EP-06 → B0 WAF HMAC",
            "<b>Trazabilidad:</b> Voucher obligatorio en MinIO y Devoluciones (EDU-0036)",
        ],
        "apis": [
            {"method": "POST/HOOK", "endpoint": "https://api.pasarela-pci.pe/v1/charges & Webhook /api/v1/pagos/cb", "auth": "API Key + HMAC TLS 1.3 (EP-06)", "purpose": "Validación electrónica de pagos de paquetes y conciliación HMAC vía B0 → B8 (ILA-0102)", "sla": "< 3.0 s"},
        ],
        "tbs": [],
        "extra_tags": ["EDU-0036", "GUI-0026", "EP-06", "RNF-0014"],
    },
]

# 40 Flujos Correlativos (Ingress Estricto Actores -> EP-01..06 -> B0 -> Bloques B1..B10)
FLOWS = [
    # Ingreso Humano: Actor -> Entry Point -> Gateway B0
    {"id": "F1", "core": "F1: Actúa Apoderado", "detail": "PWA /app/tutor/* (EXT-A1→EP-01)", "src": "EXT-A1", "dst": "EP-01", "kind": "sync",
     "path": "M 410 485 L 585 485", "pill": [498, 485], "api": "Browser/PWA UI: GUI-0007, 0014, 0016, 0020, 0023, 0026", "edus": ["EDU-0014", "EDU-0021", "EDU-0023", "EDU-0029", "EDU-0033", "EDU-0036"], "rnfs": ["RNF-0007", "RNF-0018", "RNF-0019"]},
    {"id": "F2", "core": "F2: Actúa Admisión", "detail": "/app/admin/* & /caja (EXT-A2→EP-02)", "src": "EXT-A2", "dst": "EP-02", "kind": "sync",
     "path": "M 410 800 L 585 800", "pill": [498, 800], "api": "SPA UI ACT-0005: GUI-0001, 0005, 0006, 0009..11, 0013, 0023..27", "edus": ["EDU-0008", "EDU-0012", "EDU-0013", "EDU-0016", "EDU-0017", "EDU-0018", "EDU-0037"], "rnfs": ["RNF-0015", "RNF-0016", "RNF-0017"]},
    {"id": "F3", "core": "F3: Actúa Gerencia", "detail": "Gobernanza & BI (EXT-A4→EP-04)", "src": "EXT-A4", "dst": "EP-04", "kind": "sync",
     "path": "M 410 1125 L 585 1125", "pill": [498, 1125], "api": "SPA UI ACT-0001..04: GUI-0002, GUI-0004, GUI-0028", "edus": ["EDU-0009", "EDU-0011", "EDU-0038"], "rnfs": ["RNF-0001", "RNF-0003"]},
    {"id": "F4", "core": "F4: Actúa Médico", "detail": "Estación /app/medico/* (EXT-A3→EP-03)", "src": "EXT-A3", "dst": "EP-03", "kind": "sync", "bidir": True,
     "path": "M 3715 505 L 3540 505", "pill": [3627, 505], "api": "SPA Clínico: GUI-0003, 0008, 0017..19, 0021, 0022, 0025 + Alerta WSS", "edus": ["EDU-0010", "EDU-0015", "EDU-0025", "EDU-0027", "EDU-0028", "EDU-0030", "EDU-0032", "EDU-0035"], "rnfs": ["RNF-0005", "RNF-0006", "RNF-0016"]},
    {"id": "F5", "core": "F5: Teleconsulta WebRTC", "detail": "Tutor+Médico → EP-05 ↔ B0", "src": "EP-05", "dst": "B0", "kind": "sync", "bidir": True,
     "path": "M 1455 275 L 1455 375", "pill": [1455, 322], "api": "/app/teleconsulta/:id (GUI-0012) + wss://.../ws/alertas-rojas/", "edus": ["EDU-0019", "EDU-0023"], "rnfs": ["RNF-0006", "RNF-0008", "RNF-0019"]},
    {"id": "F29", "core": "F29: Ingress HTTPS :443", "detail": "EP-01,02,04 → B0 WAF + JWT", "src": "EP-01", "dst": "B0", "kind": "sync", "bidir": True,
     "path": "M 1015 440 L 1190 440 M 1015 745 L 1065 745 L 1065 440 M 1015 1075 L 1095 1075 L 1095 440", "pill": [1095, 440], "api": "HTTPS / WSS Port 443 TLS 1.3 + JWT Bearer 15m (AuthGuard)", "edus": [], "rnfs": ["RNF-0013", "RNF-0014", "RNF-0025"]},
    {"id": "F6", "core": "F6: Webhooks M2M HMAC", "detail": "EP-06 → B0 WAF (TLS 1.3)", "src": "EP-06", "dst": "B0", "kind": "async",
     "path": "M 1015 1410 L 1118 1410 L 1118 525 L 1190 525", "pill": [1118, 1295], "api": "POST /api/v1/pagos/cb & /webhooks/mensajeria/status/ (HMAC TLS 1.3)", "edus": ["EDU-0020", "EDU-0036"], "rnfs": ["RNF-0009", "RNF-0014", "RNF-0025"]},
    {"id": "F37", "core": "F37: Clínica HTTPS+WSS", "detail": "EP-03 ↔ B0 Gateway ACL", "src": "EP-03", "dst": "B0", "kind": "sync", "bidir": True,
     "path": "M 3375 375 L 3375 296 L 1665 296 L 1665 375", "pill": [2445, 296], "api": "HTTPS TLS 1.3 /api/v1/historias/* + wss://.../ws/alertas-rojas/", "edus": ["EDU-0032", "EDU-0035"], "rnfs": ["RNF-0001", "RNF-0006", "RNF-0013", "RNF-0014"]},
    {"id": "F30", "core": "F30: Bus /api/v1/* DRF", "detail": "B0 Gateway → Bloques B1..B10", "src": "B0", "dst": "B4", "kind": "sync", "bidir": True,
     "path": "M 1455 560 L 1455 612 L 2835 612 L 2835 685 M 1425 612 L 1425 685 M 2130 612 L 2130 685 M 2120 612 L 2120 560 M 2825 612 L 2825 560 M 1455 612 L 1165 612 L 1165 1470 L 1190 1470 M 1165 1095 L 1190 1095 M 2480 612 L 2480 1245 L 2560 1245 M 2480 1630 L 2560 1630", "pill": [1780, 612], "api": "Django 5 DRF :8000 + Daphne ASGI Router (RBAC Verificado)", "edus": ["EDU-0008..EDU-0038"], "rnfs": ["RNF-0012", "RNF-0015", "RNF-0026"]},
    {"id": "F31", "core": "F31: Check RBAC+JWT", "detail": "validación claims (B0↔B10)", "src": "B0", "dst": "B10", "kind": "sync", "bidir": True,
     "path": "M 1190 555 L 1148 555 L 1148 1795 L 1190 1795", "pill": [1148, 1625], "api": "RBAC PermissionMiddleware + audit_logs UTC", "edus": ["EDU-0011", "EDU-0009"], "rnfs": ["RNF-0001", "RNF-0003", "RNF-0013"]},

    # Orquestación Interna Capa 3 (Corredor Interno Izquierdo: x 1660..1865, centro=1762)
    {"id": "F7", "core": "F7: Paciente OK", "detail": "filiación validada (B1→B4)", "src": "B1", "dst": "B4", "kind": "sync",
     "path": "M 1660 795 L 1865 795", "pill": [1762, 795], "api": "Service Call: PatientValidationDTO (EDU-0014, 0021)", "edus": ["EDU-0014", "EDU-0021"], "rnfs": ["RNF-0005"]},
    {"id": "F8", "core": "F8: Triaje+Acta OK", "detail": "habilitación cita (RNF-0010)", "src": "B2", "dst": "B4", "kind": "sync",
     "path": "M 1660 1055 L 1865 1055", "pill": [1762, 1055], "api": "Guard: checkPretriageAndConsent(id_paciente)", "edus": ["EDU-0023", "EDU-0029"], "rnfs": ["RNF-0010", "RNF-0027"]},
    {"id": "F9", "core": "F9: Franjas Libres", "detail": "disponibilidad <=2s (RNF-0015)", "src": "B3", "dst": "B4", "kind": "sync",
     "path": "M 1660 1405 L 1762 1405 L 1762 1125 L 1865 1125", "pill": [1762, 1255], "api": "GET /api/v1/horarios/disponibilidad/", "edus": ["EDU-0016", "EDU-0017"], "rnfs": ["RNF-0004", "RNF-0015"]},
    {"id": "F19", "core": "F19: Traza Forense", "detail": "logs UTC cambios (B4→B10)", "src": "B4", "dst": "B10", "kind": "sync",
     "path": "M 1865 1155 L 1810 1155 L 1810 1720 L 1660 1720", "pill": [1762, 1720], "api": "AuditEvent -> TB_HISTORIAL_CITAS + audit_logs", "edus": ["EDU-0009"], "rnfs": ["RNF-0003"]},
    {"id": "F20", "core": "F20: Permisos RBAC", "detail": "roles verificados (B10→B4)", "src": "B10", "dst": "B4", "kind": "sync",
     "path": "M 1660 1795 L 1790 1795 L 1790 1218 L 1935 1218 L 1935 1190", "pill": [1790, 1520], "api": "RoleGuard.checkPermissions(user_role)", "edus": ["EDU-0011"], "rnfs": ["RNF-0001", "RNF-0013"]},
    {"id": "F32", "core": "F32: Pizarra KSs", "detail": "Redis Blackboard HSET (B2↔B12)", "src": "B2", "dst": "B12", "kind": "async", "bidir": True,
     "path": "M 1660 1235 L 1712 1235 L 1712 1900 L 1865 1900", "pill": [1762, 1900], "api": "Redis 6379 HSET blackboard:pretriage + Pub/Sub", "edus": ["EDU-0023", "EDU-0029"], "rnfs": ["RNF-0027", "RNF-0006"]},

    # Eje Central (B4 <-> B5, B4 <-> B11)
    {"id": "F12", "core": "F12: Solicita Sala", "detail": "cita virtual (B4→B5)", "src": "B4", "dst": "B5", "kind": "sync",
     "path": "M 1975 685 L 1975 560", "pill": [1975, 648], "api": "POST /api/v1/teleconsulta/salas/", "edus": ["EDU-0018", "EDU-0019"], "rnfs": ["RNF-0008"]},
    {"id": "F13", "core": "F13: URL Meet", "detail": "token sala virtual (B5→B4)", "src": "B5", "dst": "B4", "kind": "async",
     "path": "M 2280 560 L 2280 685", "pill": [2280, 648], "api": "Callback: meet_url + PIN guardado en TB_CITAS", "edus": ["EDU-0019"], "rnfs": ["RNF-0008"]},
    {"id": "F21", "core": "F21: Transacción ACID", "detail": "SELECT FOR UPDATE (B4↔B11)", "src": "B4", "dst": "B11", "kind": "sync", "bidir": True,
     "path": "M 2130 1190 L 2130 1320", "pill": [2130, 1225], "api": "SQL SERIALIZABLE / PgBouncer TCP 6432", "edus": ["EDU-0008", "EDU-0012", "EDU-0013"], "rnfs": ["RNF-0004", "RNF-0011"]},

    # Corredor Interno Derecho (x 2395..2560, centro=2477)
    {"id": "F14", "core": "F14: Aviso T-24h", "detail": "programar recordatorio (B4→B6)", "src": "B4", "dst": "B6", "kind": "async",
     "path": "M 2395 720 L 2450 720 L 2450 470 L 2560 470", "pill": [2450, 540], "api": "Celery Delay: scheduleReminderT24h(id_cita)", "edus": ["EDU-0020", "EDU-0013"], "rnfs": ["RNF-0009"]},
    {"id": "F15", "core": "F15: Habilitar HCE", "detail": "cita 'En Atención' (B4→B7)", "src": "B4", "dst": "B7", "kind": "sync",
     "path": "M 2395 785 L 2560 785", "pill": [2477, 785], "api": "Unlock Session: openEvolutionWindow72h(id_cita)", "edus": ["EDU-0008", "EDU-0032", "EDU-0035"], "rnfs": ["RNF-0005"]},
    {"id": "F16", "core": "F16: Interconsulta", "detail": "derivación/cita (B7→B4)", "src": "B7", "dst": "B4", "kind": "sync",
     "path": "M 2560 885 L 2395 885", "pill": [2477, 885], "api": "POST /api/v1/derivaciones/, /interconsultas/", "edus": ["EDU-0010", "EDU-0015", "EDU-0027"], "rnfs": ["RNF-0001"]},
    {"id": "F17", "core": "F17: Alerta Roja WSS", "detail": "SpO2<92% Pizarra (B2→B7)", "src": "B2", "dst": "B7", "kind": "async",
     "path": "M 1660 1190 L 1762 1190 L 1762 1265 L 2430 1265 L 2430 960 L 2560 960", "pill": [2130, 1265], "api": "wss://.../ws/alertas-rojas/ vía B0 Daphne (RNF-0006, 0027)", "edus": ["EDU-0023"], "rnfs": ["RNF-0006", "RNF-0027"]},
    {"id": "F10", "core": "F10: Saldo Paquete OK", "detail": "sesiones > 0 (EDU-0033)", "src": "B8", "dst": "B4", "kind": "sync",
     "path": "M 2560 1170 L 2395 1170", "pill": [2477, 1170], "api": "Guard: verifyActivePackageBalance(id_paciente)", "edus": ["EDU-0033"], "rnfs": ["RNF-0011"]},
    {"id": "F11", "core": "F11: -1 Sesión", "detail": "deducción auto 'Atendida'", "src": "B4", "dst": "B8", "kind": "sync",
     "path": "M 2395 1110 L 2450 1110 L 2450 1210 L 2560 1210", "pill": [2477, 1210], "api": "Atomic Update: decrementSessionBalance(id_cita)", "edus": ["EDU-0012", "EDU-0033"], "rnfs": ["RNF-0011"]},
    {"id": "F18", "core": "F18: Turnos Atendida", "detail": "cierre mensual (B4→B9)", "src": "B4", "dst": "B9", "kind": "sync",
     "path": "M 2395 1030 L 2415 1030 L 2415 1605 L 2560 1605", "pill": [2485, 1605], "api": "Query Aggregated Citas Atendida (EDU-0038)", "edus": ["EDU-0038", "EDU-0008"], "rnfs": ["RNF-0011"]},
    {"id": "F34", "core": "F34: Vitalis_BD Pool", "detail": "PgBouncer 6432 CRUD (→B11)", "src": "B11", "dst": "B8", "kind": "sync", "bidir": True,
     "path": "M 1865 1470 L 1660 1470 M 1865 1595 L 1825 1595 L 1825 1690 L 1660 1690 M 2395 1435 L 2475 1435 L 2475 995 L 2560 995 M 2475 1390 L 2560 1390 M 2475 1675 L 2560 1675", "pill": [2485, 1435], "api": "PgBouncer TCP 6432 -> PostgreSQL 5432 ACID", "edus": ["EDU-0008..EDU-0038"], "rnfs": ["RNF-0011", "RNF-0020", "RNF-0002"]},
    {"id": "F33", "core": "F33: MinIO S3 AES-256", "detail": "URLs 300s (B7/8/9↔B12)", "src": "B12", "dst": "B8", "kind": "sync", "bidir": True,
     "path": "M 2395 1865 L 2508 1865 L 2508 1045 L 2560 1045 M 2508 1475 L 2560 1475 M 2508 1755 L 2560 1755", "pill": [2485, 1865], "api": "MinIO S3 TCP 9000 Presigned URLs (300s)", "edus": ["EDU-0025", "EDU-0028", "EDU-0029", "EDU-0036", "EDU-0037", "EDU-0038"], "rnfs": ["RNF-0024"]},

    # Flujos Externos Capa 5, Webhooks, Celery Beat y Salidas
    {"id": "F22", "core": "F22: Google Meet OAuth2", "detail": "POST /v2/spaces ↔ URL", "src": "B5", "dst": "EXT-API1", "kind": "sync", "bidir": True,
     "path": "M 2120 375 L 2120 270", "pill": [2120, 336], "api": "HTTPS TLS 1.3 OAuth2 Meet Spaces API (RNF-0008)", "edus": ["EDU-0019"], "rnfs": ["RNF-0008", "RNF-0014"]},
    {"id": "F23", "core": "F23: WhatsApp / Twilio", "detail": "POST /messages T-24h (B6→API2)", "src": "B6", "dst": "EXT-API2", "kind": "sync",
     "path": "M 2825 375 L 2825 270", "pill": [2825, 336], "api": "HTTPS TLS 1.3 WhatsApp Cloud + Twilio", "edus": ["EDU-0020"], "rnfs": ["RNF-0009", "RNF-0014"]},
    {"id": "F38", "core": "F38: Status Hook WA", "detail": "Callback entrega (API2→EP-06)", "src": "EXT-API2", "dst": "EP-06", "kind": "async",
     "path": "M 2825 115 L 2825 82 L 502 82 L 502 1420 L 575 1420", "pill": [950, 82], "api": "Webhook HTTPS POST /api/v1/webhooks/mensajeria/status/", "edus": ["EDU-0020"], "rnfs": ["RNF-0009", "RNF-0014"]},
    {"id": "F24", "core": "F24: Push T-24h + Meet", "detail": "WhatsApp/SMS a Apoderado", "src": "EXT-API2", "dst": "EXT-A1", "kind": "async",
     "path": "M 2620 115 L 2620 56 L 14 56 L 14 485 L 55 485", "pill": [1320, 56], "api": "Mensaje Externo WhatsApp/Voz hacia Apoderado", "edus": ["EDU-0020", "EDU-0019"], "rnfs": ["RNF-0009"]},
    {"id": "F25", "core": "F25: SUNAT UBL 2.1", "detail": "Tubería X.509 ↔ CDR <3s", "src": "B8", "dst": "EXT-API3", "kind": "sync", "bidir": True,
     "path": "M 3110 1225 L 3260 1225", "pill": [3185, 1225], "api": "SOAP/REST HTTPS TLS 1.3 XML UBL 2.1 (6 Filtros, RNF-0023)", "edus": ["EDU-0037"], "rnfs": ["RNF-0023", "RNF-0014", "RNF-0021"]},
    {"id": "F26", "core": "F26: Cobro Tarjeta/Yape", "detail": "B8 → Pasarela PCI-DSS", "src": "B8", "dst": "EXT-API4", "kind": "sync",
     "path": "M 3110 1445 L 3260 1445", "pill": [3185, 1445], "api": "POST /v1/charges HTTPS TLS 1.3 (Niubiz/Izipay/Yape/Plin)", "edus": ["EDU-0036"], "rnfs": ["RNF-0014", "RNF-0024"]},
    {"id": "F39", "core": "F39: Hook Pago HMAC", "detail": "Callback Abono (API4→EP-06)", "src": "EXT-API4", "dst": "EP-06", "kind": "async",
     "path": "M 3485 1555 L 3485 2292 L 795 2292 L 795 1610", "pill": [2140, 2292], "api": "Webhook PCI-DSS /api/v1/pagos/cb → ingresa por EP-06 → B0", "edus": ["EDU-0036"], "rnfs": ["RNF-0014", "RNF-0025"]},
    {"id": "F27", "core": "F27: Comprobante PDF QR", "detail": "MinIO URL → Tutor (EP-01)", "src": "B8", "dst": "EXT-A1", "kind": "async",
     "path": "M 3110 1335 L 3168 1335 L 3168 2328 L 28 2328 L 28 545 L 55 545", "pill": [1650, 2328], "api": "Comprobante PDF QR SUNAT (MinIO 300s) → Portal Tutor EP-01", "edus": ["EDU-0037", "EDU-0036"], "rnfs": ["RNF-0023", "RNF-0024"]},
    {"id": "F28", "core": "F28: Liquidación PDF", "detail": "4 Lotes → Gerencia (EP-04)", "src": "B9", "dst": "EXT-A4", "kind": "sync",
     "path": "M 2560 1805 L 2535 1805 L 2535 2248 L 365 2248 L 365 1240", "pill": [1450, 2248], "api": "GET /api/v1/liquidaciones/{id}/reporte-pdf/ → EP-04", "edus": ["EDU-0038"], "rnfs": ["RNF-0024", "RNF-0011"]},
    {"id": "F35", "core": "F35: Cola Celery & Cron", "detail": "EP-06 Beat & B12 → B6, B9", "src": "B12", "dst": "B6", "kind": "async",
     "path": "M 2395 1875 L 3152 1875 L 3152 470 L 3090 470 M 2835 1875 L 2835 1840 M 795 1610 L 795 2205 L 2130 2205 L 2130 2030", "pill": [2835, 1875], "api": "Celery 5.4 Worker + Beat Scheduler via Redis Broker TCP 6379", "edus": ["EDU-0020", "EDU-0038"], "rnfs": ["RNF-0009", "RNF-0026"]},
    {"id": "F36", "core": "F36: Ficha & Alerta Clín.", "detail": "WSS <2s + HCE (B7 ↔ EP-03)", "src": "B7", "dst": "EP-03", "kind": "async", "bidir": True,
     "path": "M 3110 880 L 3375 880 L 3375 630", "pill": [3285, 880], "api": "Push wss://.../ws/alertas-rojas/ (vía B0 Daphne) + REST <=1.5s HCE", "edus": ["EDU-0017", "EDU-0023", "EDU-0028", "EDU-0032", "EDU-0019"], "rnfs": ["RNF-0005", "RNF-0006", "RNF-0027"]},
]


def _segments_from_path(path_str):
    """Extrae segmentos ortogonales de una cadena SVG path M/L."""
    segs = []
    tokens = re.findall(r"[ML]|-?\d+(?:\.\d+)?", path_str)
    i = 0
    cur = None
    while i < len(tokens):
        tok = tokens[i]
        if tok == "M":
            cur = (float(tokens[i + 1]), float(tokens[i + 2]))
            i += 3
        elif tok == "L":
            nxt = (float(tokens[i + 1]), float(tokens[i + 2]))
            if cur is not None:
                segs.append((cur, nxt))
            cur = nxt
            i += 3
        else:
            i += 1
    return segs


def _seg_hits_rect(p1, p2, rect):
    """Comprueba si un segmento ortogonal atraviesa el interior estricto de un rectángulo."""
    rx, ry, rw, rh = rect
    x1, y1 = p1
    x2, y2 = p2
    ix1, iy1, ix2, iy2 = rx + 4, ry + 4, rx + rw - 4, ry + rh - 4
    minx, maxx = min(x1, x2), max(x1, x2)
    miny, maxy = min(y1, y2), max(y1, y2)
    return not (maxx <= ix1 or minx >= ix2 or maxy <= iy1 or miny >= iy2)


def audit_geometry():
    """Audita superposición de tarjetas, píldoras y cruce de flechas sobre tarjetas."""
    issues = []
    # 1. Tarjetas entre sí
    for i in range(len(NODES)):
        x1, y1, w1, h1 = NODES[i]["rect"]
        for j in range(i + 1, len(NODES)):
            x2, y2, w2, h2 = NODES[j]["rect"]
            if not (x1 + w1 <= x2 or x2 + w2 <= x1 or y1 + h1 <= y2 or y2 + h2 <= y1):
                issues.append(f"COLISION TARJETAS: {NODES[i]['id']} vs {NODES[j]['id']}")

    # 2. Píldora vs Tarjeta (caja máxima macro 148x24)
    pw, ph = 148, 24
    for f in FLOWS:
        px, py = f["pill"]
        fx1, fy1, fx2, fy2 = px - pw / 2, py - ph / 2, px + pw / 2, py + ph / 2
        for n in NODES:
            x, y, w, h = n["rect"]
            if not (fx2 <= x or x + w <= fx1 or fy2 <= y or y + h <= fy1):
                issues.append(f"PILDORA SOBRE TARJETA: {f['id']} pill={f['pill']} sobre {n['id']} {n['rect']}")

    # 3. Píldora vs Píldora
    for i in range(len(FLOWS)):
        p1x, p1y = FLOWS[i]["pill"]
        for j in range(i + 1, len(FLOWS)):
            p2x, p2y = FLOWS[j]["pill"]
            if abs(p1x - p2x) < 132 and abs(p1y - p2y) < 28:
                issues.append(f"PILDORAS SOLAPADAS: {FLOWS[i]['id']} {FLOWS[i]['pill']} vs {FLOWS[j]['id']} {FLOWS[j]['pill']}")

    # 4. Segmentos de flecha atravesando tarjetas
    for f in FLOWS:
        segs = _segments_from_path(f["path"])
        for p1, p2 in segs:
            for n in NODES:
                if _seg_hits_rect(p1, p2, n["rect"]):
                    issues.append(f"FLECHA ATRAVIESA TARJETA: {f['id']} seg=({p1}->{p2}) cruza {n['id']} {n['rect']}")

        # 5. Cada píldora debe reposar sobre su propia línea
        px, py = f["pill"]
        on_or_near = any(
            (abs(x1 - x2) < 1e-3 and abs(px - x1) <= 42 and min(y1, y2) - 2 <= py <= max(y1, y2) + 2) or
            (abs(y1 - y2) < 1e-3 and abs(py - y1) <= 12 and min(x1, x2) - 2 <= px <= max(x1, x2) + 2)
            for (x1, y1), (x2, y2) in segs
        )
        if not on_or_near:
            issues.append(f"PILDORA DESCONECTADA DE SU FLECHA: {f['id']} pill={f['pill']}")

    return issues


if __name__ == "__main__":
    errs = audit_geometry()
    if errs:
        print("PROBLEMAS GEOMETRICOS:")
        for e in errs:
            print(" -", e)
        raise SystemExit(1)
    print(f"AUDITORIA GEOMETRICA PERFECTA: {len(NODES)} tarjetas, {len(FLOWS)} flechas y píldoras con 0 colisiones.")

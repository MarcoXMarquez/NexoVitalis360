#!/usr/bin/env python3
"""
build_mermaid_suite.py (v02.10)
Genera la suite de 5 diagramas Mermaid oficiales (.mmd + .md consolidado):
  1. Arquitectura Integral Definitiva (Actores -> Entry Points -> DMZ B0 -> B1..B10 -> Datos -> APIs)
  2. Mapa Exhaustivo de APIs REST / WSS / Webhooks / Celery Beat
  3. Matriz RNF-0001..0027 (ISO/IEC 25010)
  4. Patrón Pizarra (RNF-0027) + Tuberías/Filtros & Lotes Secuenciales (Plantilla 8)
  5. Mapa Completo de Entry Points (EP-01..06), Actores y Ubicación de las 28 GUIs (140 MDL)
Estética: Tema base B&W puro con contraste máximo.
"""

import os

BASE_DIR = "/home/marco/Projects/NexoVitalis360"
VL_DIR = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica")
COMP_DIR = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/02_Diagrama_Comportamiento")
VISOR_DIR = os.path.join(BASE_DIR, "05_DIAGRAMAS_Y_RECURSOS_EDITABLES/VISOR_HTML_ARQUITECTURA_v01.00")

MERMAID_INIT = """%%{init: {'theme': 'base', 'flowchart': {'curve': 'orthogonal', 'htmlLabels': true, 'nodeSpacing': 34, 'rankSpacing': 52}, 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000', 'secondaryColor': '#f4f4f4', 'tertiaryColor': '#fafafa', 'clusterBkg': '#fafafa', 'clusterBorder': '#000000', 'fontFamily': 'Arial, sans-serif'}}}%%"""

MERMAID_INIT_COMPACT = """%%{init: {'theme': 'base', 'flowchart': {'curve': 'basis', 'htmlLabels': true, 'nodeSpacing': 20, 'rankSpacing': 44}, 'themeVariables': {'primaryColor': '#ffffff', 'primaryTextColor': '#000000', 'primaryBorderColor': '#000000', 'lineColor': '#000000', 'secondaryColor': '#f4f4f4', 'tertiaryColor': '#fafafa', 'clusterBkg': '#fafafa', 'clusterBorder': '#000000', 'fontFamily': 'Arial, sans-serif', 'fontSize': '12px'}}}%%"""

MERMAID_01 = MERMAID_INIT_COMPACT + """
flowchart TB
    classDef ext fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef ep fill:#fafafa,stroke:#000000,stroke-width:2.5px,stroke-dasharray:6 3,color:#000000
    classDef gw fill:#f0f0f0,stroke:#000000,stroke-width:3.5px,color:#000000
    classDef blk fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef hub fill:#f0f0f0,stroke:#000000,stroke-width:3.5px,color:#000000
    classDef db fill:#fafafa,stroke:#000000,stroke-width:3px,color:#000000
    classDef meta fill:#ffffff,stroke:#000000,stroke-width:1.8px,stroke-dasharray:5 4,color:#000000

    subgraph CAPA1["ZONA 1 — ACTORES & ENTRY POINTS FRONTALES (Quién Actúa y Por Dónde Entra)"]
        direction TB
        EXT_A1["EXT-A1: Apoderado / Menor<br/>PWA Android 11+/iOS 15+"]:::ext
        EXT_A2["EXT-A2: Asistente ACT-0005<br/>PC Win10/11 pagefile.sys"]:::ext
        EXT_A3["EXT-A3: Especialista Clínico<br/>Med/Nut/Psic (ACT-0002..04)"]:::ext
        EXT_A4["EXT-A4: Gerencia ACT-0001..04<br/>ORG-0001..0003"]:::ext

        EP1["EP-01: /app/tutor/* PWA<br/>GUI-0007,14,16,20,23,26"]:::ep
        EP2["EP-02: /app/admin/* & /caja<br/>GUI-0001,05,06,09..11,13,24,27"]:::ep
        EP3["EP-03: /app/medico/* SPA<br/>8 GUIs HCE (03..25) + WSS"]:::ep
        EP4["EP-04: /auditoria & BI<br/>GUI-0002, GUI-0004, GUI-0028"]:::ep
        EP5["EP-05: /app/teleconsulta/:id<br/>WebRTC + GUI-0012 + Alerta"]:::ep
        EP6["EP-06: Ingress M2M<br/>Webhooks HMAC + Celery Beat"]:::ep
    end

    subgraph CAPA2["ZONA 2 DMZ — ADUANA PERIMETRAL ÚNICA (:443 WAF + JWT RBAC)"]
        direction TB
        B0["B0. API Gateway NGINX TLS 1.3 + WAF + JWT 15m<br/>DRF :8000 • Daphne ASGI WSS • RBAC RoleGuard"]:::gw
    end

    subgraph CAPA3["ZONA 3 VPC APP — 10 BLOQUES FUNCIONALES (27 EDU | 108 ILA | 104 ESP | 113 Pruebas | 28 GUIs)"]
        direction TB
        B1["B1. Pacientes y Apoderados<br/>EDU-0014, 21 | GUI-0007, 14"]:::blk
        B2["B2. Pre-Triaje, Acta & Pizarra<br/>EDU-0023, 29 | Bonita ILA-0062<br/>GUI-0016, 20 | 4 KSs RNF-0027"]:::blk
        B3["B3. Especialistas y Horarios<br/>EDU-0016, 17 | GUI-0009, 10<br/>API <=2s RNF-0015"]:::blk
        B10["B10. RBAC y Auditoría Forense<br/>EDU-0009, 11 | GUI-0002, 04<br/>RNF-0001, 0003, 0013"]:::blk
        B4["B4. NÚCLEO ORQUESTADOR CITAS<br/>EDU-0008,12,13,18 | Bonita ILA-0017<br/>GUI-0001,05,06,11 (20 MDL) • >=24h<br/>SELECT FOR UPDATE RNF-0004"]:::hub
        B5["B5. Videoconf. WebRTC<br/>EDU-0019 | GUI-0012<br/>RNF-0008, 0019"]:::blk
        B6["B6. Mensajería T-24h<br/>EDU-0020 | GUI-0013<br/>RNF-0009, 0026"]:::blk
        B7["B7. HCE, CIE-10, Recetas, Intercons.<br/>8 EDU (32 ILA) | 8 GUIs / 40 MDL<br/>Lock 72h • Intercons 7d • RNF-0001,05"]:::blk
        B8["B8. Paquetes, Pagos & SUNAT<br/>Tuberías 6 Filtros UBL 2.1<br/>GUI-0023,24,26,27 | Bonita ILA-0106"]:::blk
        B9["B9. Liquidación Mensual<br/>Lotes Secuenciales 4 Fases<br/>EDU-0038 | GUI-0028"]:::blk
    end

    subgraph CAPA4["ZONA 4 VPC DATOS — POSTGRESQL 16, MINIO S3, REDIS BLACKBOARD & CODIFICACIÓN"]
        B11[("B11. Vitalis_BD PG16 + PgBouncer 6432<br/>27 Tablas TB_* • ACID • AES-256<br/>WAL RPO<=15m RTO<=30m")]:::db
        B12["B12. MinIO S3 (9000) + Redis 7.2 (6379)<br/>5 Buckets URLs 300s (RNF-0024)<br/>Pizarra HSET + Pub/Sub (RNF-0027)"]:::db
        INFRA["Estándares & Codificadores<br/>Django 5 DRF + React 18 (RNF-0012/26)<br/>Ubuntu 24.04 + Docker 26 (RNF-0020)"]:::meta
    end

    subgraph CAPA5["CAPA 5 CLOUD — APIS EXTERNAS REGULADAS (HTTPS TLS 1.3)"]
        EXT_API1["EXT-API1: Google Meet v2<br/>OAuth2 /spaces (RNF-0008)"]:::ext
        EXT_API2["EXT-API2: WhatsApp / Twilio<br/>/messages T-24h + Hook"]:::ext
        EXT_API3["EXT-API3: SUNAT OSE/PSE<br/>UBL 2.1 X.509 -> CDR <3s"]:::ext
        EXT_API4["EXT-API4: Pasarelas Pago<br/>Niubiz/Izipay/Yape/Plin"]:::ext
    end

    EXT_A1 -->|"F1"| EP1
    EXT_A2 -->|"F2"| EP2
    EXT_A3 <-->|"F4"| EP3
    EXT_A4 -->|"F3"| EP4
    EXT_A1 & EXT_A3 -.-> EP5

    EP1 & EP2 & EP4 -->|"F29: HTTPS/WSS :443 + JWT"| B0
    EP3 <-->|"F37: HTTPS + WSS Alerta"| B0
    EP5 <-->|"F5: Meet + WSS"| B0
    EP6 -->|"F6: Webhooks HMAC"| B0

    B0 -->|"F30: Bus /api/v1/* DRF + ASGI"| CAPA3
    B0 <-->|"F31: RBAC"| B10

    B1 -->|"F7"| B4
    B2 -->|"F8"| B4
    B3 -->|"F9"| B4
    B10 -->|"F20"| B4
    B4 -->|"F19"| B10
    B4 <-->|"F12/F13"| B5
    B4 -.->|"F14"| B6
    B4 <-->|"F15/F16"| B7
    B2 -.->|"F17: Alerta <2s"| B7
    B4 <-->|"F10/F11"| B8
    B4 -->|"F18"| B9

    B4 <-->|"F21: ACID"| B11
    B1 & B3 & B7 & B8 & B9 & B10 <-->|"F34: Pool 6432"| B11
    B2 <-.->|"F32: KSs"| B12
    B7 & B8 & B9 <-->|"F33: S3 300s"| B12
    B6 & B9 <-.->|"F35: Celery Beat"| EP6 & B12
    B11 ~~~ INFRA

    B5 <-->|"F22"| EXT_API1
    B6 -->|"F23"| EXT_API2
    B8 <-->|"F25"| EXT_API3
    B8 -->|"F26"| EXT_API4
    EXT_API2 & EXT_API4 -.->|"F38/F39: Hooks"| EP6
    CAPA4 ~~~ CAPA5
"""

MERMAID_02 = MERMAID_INIT + """
flowchart LR
    classDef cli fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef m2m fill:#fafafa,stroke:#000000,stroke-width:2px,stroke-dasharray:5 3,color:#000000
    classDef gw fill:#f4f4f4,stroke:#000000,stroke-width:3px,color:#000000
    classDef ep fill:#ffffff,stroke:#000000,stroke-width:1.8px,color:#000000
    classDef ext fill:#fafafa,stroke:#000000,stroke-width:2px,stroke-dasharray:4 3,color:#000000

    subgraph FRONT["ENTRY POINTS FRONTALES & M2M (QUIÉN ACTÚA / POR DÓNDE ENTRA)"]
        R_TUT["EP-01: /app/tutor/* PWA<br/>Apoderado • GUI-0007,14,16,20,23,26"]:::cli
        R_ADM["EP-02: /app/admin/* & /caja<br/>ACT-0005 • GUI-0001,05,06,09..11,13,24,27"]:::cli
        R_MED["EP-03: /app/medico/* SPA<br/>Especialista • 8 GUIs HCE + Alerta"]:::cli
        R_GOB["EP-04: /app/admin/gobernanza/*<br/>ACT-0001..04 • GUI-0002,04,28"]:::cli
        R_TEL["EP-05: /app/teleconsulta/:id<br/>WebRTC + GUI-0012 + WSS"]:::cli
        R_M2M["EP-06: Webhooks HMAC + Celery Beat<br/>/pagos/cb • /mensajeria/status/ • Cron T-24h/Mes"]:::m2m
    end

    GW["B0: NGINX DMZ + WAF + JWT RBAC<br/>HTTPS / WSS :443 TLS 1.3<br/>/api/v1/auth/jwt/* (exp 15m)<br/>RNF-0001, 0013, 0014, 0025"]:::gw

    subgraph APIS["CONTRATOS API INTERNA DJANGO 5 DRF :8000 + DAPHNE ASGI + CELERY"]
        API_ADM["Admitir & Agenda (B1, B3)<br/>/api/v1/pacientes/ (GUI-0007)<br/>/api/v1/apoderados/ (GUI-0014)<br/>/api/v1/especialistas/ (GUI-0009)<br/>/api/v1/horarios/disponibilidad/ <=2s (GUI-0010)"]:::ep
        API_PIZ["Triaje, Consentimiento & WSS (B2)<br/>/api/v1/pretriage/ (GUI-0016, RNF-0027)<br/>/api/v1/consentimientos/ (GUI-0020, RNF-0010)<br/>wss://.../ws/alertas-rojas/ <150ms (RNF-0006)"]:::ep
        API_CIT["Núcleo Orquestador Citas (B4)<br/>POST /api/v1/citas/ Lock <2s (GUI-0005, RNF-0004)<br/>PATCH /api/v1/citas/{id}/estado/ (GUI-0001)<br/>POST /api/v1/citas/{id}/reprogramar/ (GUI-0006)<br/>/api/v1/citas/{id}/modalidad/ (GUI-0011)"]:::ep
        API_COM["Canales & Gobernanza (B5, B6, B10)<br/>/api/v1/teleconsulta/salas/ (GUI-0012)<br/>/api/v1/notificaciones/ + /reenviar/ (GUI-0013)<br/>/api/v1/permisos/roles/ & /auditoria/ (GUI-0002,04)"]:::ep
        API_HCE["Historia Clínica Digital <=1.5s (B7)<br/>/api/v1/historias/ & /evoluciones/ 72h (GUI-0022,25)<br/>/api/v1/diagnosticos-cie10/ & /recetas/ (GUI-0021,19)<br/>/api/v1/documentos-adjuntos/ (GUI-0017)<br/>/api/v1/derivaciones/ & /interconsultas/ (GUI-0003,08,18)"]:::ep
        API_FIN["Finanzas, Tubería SUNAT & Lotes Batch (B8, B9)<br/>/api/v1/paquetes/ (90d) & /descuentos/ (GUI-0023,24)<br/>/api/v1/pagos/ & /pagos/cb (GUI-0026)<br/>/api/v1/facturacion/cpe/ UBL 2.1 (GUI-0027)<br/>/api/v1/liquidaciones/ (Batch 4 Lotes, GUI-0028)"]:::ep
    end

    subgraph EXT_GW["DESTINOS DE DATOS & APIS EXTERNAS"]
        DB_PG[("Vitalis_BD PG16 + PgBouncer 6432<br/>27 Tablas TB_* (RNF-0011)")]:::ext
        DB_S3["MinIO S3 9000 + Redis 6379<br/>Presigned 300s (RNF-0024) & Pizarra (RNF-0027)"]:::ext
        G_MEET["Google Meet REST v2 OAuth2 (RNF-0008)"]:::ext
        G_WA["Meta WhatsApp Cloud / Twilio + Hook (RNF-0009)"]:::ext
        G_SUNAT["SUNAT PSE/OSE XML UBL 2.1 X.509 (RNF-0023)"]:::ext
        G_PAY["Niubiz / Izipay / Yape / Plin + Hook PCI-DSS"]:::ext
    end

    R_TUT & R_ADM & R_MED & R_GOB & R_TEL & R_M2M -->|"HTTPS/WSS 443 + JWT/HMAC"| GW
    GW --> API_ADM & API_PIZ & API_CIT & API_COM & API_HCE & API_FIN

    API_ADM & API_CIT & API_HCE & API_FIN -->|"SQL Pool 6432"| DB_PG
    API_PIZ & API_HCE & API_FIN -->|"S3 / Redis 6379"| DB_S3
    API_COM -->|"OAuth2 /spaces"| G_MEET
    API_COM <-->|"REST + Hook EP-06"| G_WA
    API_FIN <-->|"SOAP/REST <3s"| G_SUNAT
    API_FIN <-->|"Charges + Hook EP-06"| G_PAY
"""

MERMAID_03 = MERMAID_INIT + """
flowchart LR
    classDef pil fill:#000000,stroke:#000000,color:#ffffff
    classDef rnf fill:#ffffff,stroke:#000000,stroke-width:1.8px,color:#000000
    classDef comp fill:#f4f4f4,stroke:#000000,stroke-width:2.2px,color:#000000

    P_SEC["SEGURIDAD Y PRIVACIDAD<br/>(ISO/IEC 25010)"]:::pil
    P_REN["RENDIMIENTO Y CONCURRENCIA"]:::pil
    P_INT["INTEROPERABILIDAD Y APIS"]:::pil
    P_USA["USABILIDAD Y PORTABILIDAD"]:::pil
    P_DAT["PERSISTENCIA Y PIZARRA CLINICA"]:::pil
    P_INF["INFRAESTRUCTURA Y CODIFICADORES"]:::pil

    R_S["RNF-0001 Acceso Doc/Interconsulta<br/>RNF-0002 Cifrado AES-256 Menores<br/>RNF-0003 Logs Auditoría Inmutables<br/>RNF-0013 JWT Stateless 15 min<br/>RNF-0014 Cifrado HTTPS TLS 1.3<br/>RNF-0024 MinIO Presigned URLs 300s<br/>RNF-0025 Red VPC, DMZ WAF & Puertos"]:::rnf

    R_R["RNF-0004 (A) Algoritmo Anticolisión <2s<br/>RNF-0004 (B) Concurrencia Citas <2s<br/>RNF-0005 Búsqueda HCE <= 1.5s<br/>RNF-0015 API Disponibilidad GET <= 2.0s"]:::rnf

    R_I["RNF-0008 Sync Auto Google Meet API<br/>RNF-0009 Notificaciones WhatsApp/SMS T-24h<br/>RNF-0023 Facturación SUNAT UBL 2.1 X.509 <3s"]:::rnf

    R_U["RNF-0006 Alertas Rojas Visuales Inmediatas<br/>RNF-0007 Calendario Reprogramación Drag&Drop<br/>RNF-0018 PWA Móvil Multi-Fabricante Android/iOS<br/>RNF-0019 Motores Blink / Gecko / WebKit W3C"]:::rnf

    R_D["RNF-0010 Restricción BD Consentimiento<br/>RNF-0011 Persistencia Relacional ACID PostgreSQL<br/>RNF-0027 Pizarra Blackboard Triaje SpO2<92%"]:::rnf

    R_M["RNF-0012 Stack Python/Django + React JS<br/>RNF-0016 Hardware Cliente i5/Ryzen 5 Win10/11<br/>RNF-0017 Memoria Virtual pagefile.sys + V8<=350MB<br/>RNF-0020 Servidores Ubuntu 24.04 + Docker 26 WAL<br/>RNF-0021 Modelado Procesos Bonita BPM 2024.1<br/>RNF-0022 Modelado UML 2.5 300 DPI + HTML5<br/>RNF-0026 Perfil Equipo Codificadores Full-Stack"]:::rnf

    P_SEC --> R_S --> C_SEC["EP-01..06 + B0 WAF/NGINX + B7 ACL + B10 RBAC + B11/B12 AES-256"]:::comp
    P_REN --> R_R --> C_REN["B3 Agenda + B4 SELECT FOR UPDATE + B7 HCE + B11 PgBouncer"]:::comp
    P_INT --> R_I --> C_INT["EP-06 Hooks + B5 Meet + B6 Celery + B8 Tubería SUNAT OSE"]:::comp
    P_USA --> R_U --> C_USA["28 GUIs (EP-01..05) + B2 WSS Alertas + B4 Calendario + B5 WebRTC"]:::comp
    P_DAT --> R_D --> C_DAT["B2 Pre-Triaje + B4 Citas + B11 Vitalis_BD 27 TB_* + B12 Redis KSs"]:::comp
    P_INF --> R_M --> C_INF["Zona 1 HW + Zona 2 DMZ + Zona 3 App/Bonita + Zona 4 Ubuntu/Docker"]:::comp
"""

MERMAID_04 = MERMAID_INIT + """
flowchart TD
    classDef core fill:#f0f0f0,stroke:#000000,stroke-width:3px,color:#000000
    classDef blk fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef alert fill:#000000,stroke:#000000,color:#ffffff

    subgraph PIZ["1. PLANTILLA 6 — PIZARRA CLÍNICA BLACKBOARD (B2 + B12 - RNF-0027 & ILA-0062)"]
        BB["Memoria Compartida Redis HSET + TB_PRETRIAJE_CLINICO<br/>GUI-0016 (TRIAJE_001) • SpO2, FC, PA, Temp, Antecedentes TEA/TDAH"]:::core
        KS1["KS_AlertaRoja: SpO2<92%, epilepsia, ideación"]:::blk
        KS2["KS_Neuropediatria: Cribado TEA/TDAH"]:::blk
        KS3["KS_Consentimiento: Verifica GUI-0020 (RNF-0010)"]:::blk
        KS4["KS_Disponibilidad: Franjas B3"]:::blk
        CTRL["Controlador Heurístico -> Riesgo Vital"]:::core
        ALERT["ALERTA ROJA <2s wss://.../ws/alertas-rojas/ -> EP-03 / EP-05 (RNF-0006)"]:::alert

        BB <--> KS1 & KS2 & KS3 & KS4
        BB --> CTRL -->|"Si Riesgo Vital"| ALERT
    end

    subgraph PIPE["2. PLANTILLA 8 — TUBERÍAS Y FILTROS: FACTURACIÓN SUNAT (B8 - EDU-0037 / GUI-0027)"]
        direction LR
        P_IN["Payload Pago"]:::blk --> F1["1. Validador DNI/RUC"]:::blk --> F2["2. XML UBL 2.1"]:::blk --> F3["3. Firma X.509"]:::blk --> F4["4. ZIP Nomenc."]:::blk --> F5["5. SOAP OSE <3s"]:::core --> F6["6. CDR + PDF QR / Ctrl Interno"]:::blk
    end

    subgraph BATCH["3. PLANTILLA 8 — LOTES SECUENCIALES: LIQUIDACIÓN MENSUAL (B9 - EDU-0038 / GUI-0028)"]
        direction LR
        L1["Lote 1: Citas 'Atendida'"]:::blk --> L2["Lote 2: Tarifación Modalidad"]:::blk --> L3["Lote 3: Comisión 20% + Retenc. 8%"]:::blk --> L4["Lote 4: TB_LIQUIDACIONES + PDF -> EP-04"]:::core
    end

    PIZ ~~~ PIPE ~~~ BATCH
"""

MERMAID_05 = MERMAID_INIT + """
flowchart LR
    classDef act fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    classDef ep fill:#f4f4f4,stroke:#000000,stroke-width:3px,color:#000000
    classDef gui fill:#ffffff,stroke:#000000,stroke-width:1.6px,color:#000000
    classDef blk fill:#f0f0f0,stroke:#000000,stroke-width:2.5px,color:#000000
    classDef m2m fill:#fafafa,stroke:#000000,stroke-width:2px,stroke-dasharray:5 3,color:#000000

    subgraph ACTORES["1. QUIÉN ACTÚA (CATÁLOGO + OPERATIVOS)"]
        A1["EXT-A1: Apoderado / Paciente Menor"]:::act
        A2["EXT-A2: Asistente / Secretaria (ACT-0005)"]:::act
        A3["EXT-A3: Especialista Clínico (Med/Nut/Psic)"]:::act
        A4["EXT-A4: Gerencia & Jefaturas (ACT-0001..0004)"]:::act
        A_M2M["APIs Externas & Cron Interno (Sin Usuario)"]:::m2m
    end

    subgraph EPS["2. POR DÓNDE ENTRA (ENTRY POINTS)"]
        EP1["EP-01: PWA Móvil<br/>/app/tutor/* (:443 JWT)"]:::ep
        EP2["EP-02: Consola Admisión & Caja<br/>/app/admin/* & /caja (:443 JWT)"]:::ep
        EP3["EP-03: Estación Clínica<br/>/app/medico/* (:443 JWT + RNF-0001)"]:::ep
        EP4["EP-04: Consola Gobernanza & BI<br/>/auditoria & /liquidaciones"]:::ep
        EP5["EP-05: Sala WebRTC + Alerta WSS<br/>/app/teleconsulta/:id"]:::ep
        EP6["EP-06: Webhooks & Beat Cron<br/>/pagos/cb • /mensajeria/status/"]:::m2m
    end

    GW["B0: DMZ WAF + NGINX<br/>JWT 15m + RBAC Guard"]:::ep

    subgraph GUIS["3. ESTA GUI VA ACÁ (27 ACTIVAS + 1 EN BLANCO / 140 MDL)"]
        G_B1["Bloque B1: GUI-0007 (Pacientes)<br/>GUI-0014 (Apoderados)"]:::gui
        G_B2["Bloque B2: GUI-0016 (Pre-Triaje TRIAJE_001)<br/>GUI-0020 (Consentimiento Informado)"]:::gui
        G_B3["Bloque B3: GUI-0009 (Especialistas/Tarifas)<br/>GUI-0010 (Horarios Semanales)"]:::gui
        G_B4["Bloque B4: GUI-0001 (Estados), GUI-0005 (Citas)<br/>GUI-0006 (Reprog.), GUI-0011 (Modalidad)"]:::gui
        G_B5["Bloque B5: GUI-0012 (Videoconf. Meet)"]:::gui
        G_B6["Bloque B6: GUI-0013 (Mensajería T-24h)"]:::gui
        G_B7["Bloque B7: GUI-0003, 0008, 0017, 0018,<br/>GUI-0019, 0021, 0022, 0025 (40 MDL)"]:::gui
        G_B8["Bloque B8: GUI-0023 (Paq), GUI-0024 (Dscto)<br/>GUI-0026 (Pagos), GUI-0027 (Fact. SUNAT)"]:::gui
        G_B9["Bloque B9: GUI-0028 (Liquidación Mensual)"]:::gui
        G_B10["Bloque B10: GUI-0002 (Historial)<br/>GUI-0004 (Permisos RBAC)"]:::gui
        G_CAT["Catálogo Base: GUI-0015 / EDU-0022<br/>(en blanco: MDL-0071..0075)"]:::m2m
    end

    A1 --> EP1 & EP5
    A2 --> EP2
    A3 --> EP3 & EP5
    A4 --> EP4
    A_M2M --> EP6

    EP1 & EP2 & EP3 & EP4 & EP5 & EP6 --> GW

    GW --> G_B1 & G_B2 & G_B3 & G_B4 & G_B5 & G_B6 & G_B7 & G_B8 & G_B9 & G_B10
    G_B1 ~~~ G_CAT
"""


def build_all_mermaid():
    os.makedirs(VL_DIR, exist_ok=True)
    os.makedirs(COMP_DIR, exist_ok=True)
    os.makedirs(VISOR_DIR, exist_ok=True)

    files = {
        "mermaid_01_arquitectura_integral_definitiva.mmd": MERMAID_01.strip(),
        "mermaid_02_mapa_apis_y_flujos.mmd": MERMAID_02.strip(),
        "mermaid_03_matriz_rnf_sistema.mmd": MERMAID_03.strip(),
        "mermaid_04_pizarra_y_circuitos_criticos.mmd": MERMAID_04.strip(),
        "mermaid_05_entry_points_y_guis.mmd": MERMAID_05.strip(),
    }

    for fname, content in files.items():
        with open(os.path.join(VL_DIR, fname), "w", encoding="utf-8") as f:
            f.write(content + "\n")

    md_doc = f"""# Diagrama de Bloques Funcionales Definitivo en Mermaid — NexoVitalis360 (v02.10)

**Proyecto:** NexoVitalis360 (RuwayLabs Perú / UNSA — EPIS)  
**Cobertura Integral Verificada:** **Entry Points (`EP-01..EP-06`)** • **27/27 Educciones** • **108/108 Ilaciones** • **104/108 Especificaciones (`ESP-*`)** • **113 Pruebas (`T-001..T-020`)** • **28/28 Entradas RNF** • **28 Secciones GUI / 140 Modales (`GUI-0001..0028`)** • **27 Tablas `TB_*`** • **Plantilla 8 (Tuberías y Lotes)**.

---

## 1. Diagrama Definitivo Maestro Integral (Zonas + Entry Points + B0..B12 + APIs + RNF)

> Fuente editable: [`mermaid_01_arquitectura_integral_definitiva.mmd`](file:///home/marco/Projects/NexoVitalis360/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/mermaid_01_arquitectura_integral_definitiva.mmd)

```mermaid
{MERMAID_01.strip()}
```

---

## 2. Mapa de Entry Points (`EP-01..06`), Actores y Ubicación de las 28 GUIs

> Fuente editable: [`mermaid_05_entry_points_y_guis.mmd`](file:///home/marco/Projects/NexoVitalis360/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/mermaid_05_entry_points_y_guis.mmd)

```mermaid
{MERMAID_05.strip()}
```

---

## 3. Contrato Exhaustivo de APIs Internas (REST / WSS / Webhooks / Celery) y Gateways Externos

> Fuente editable: [`mermaid_02_mapa_apis_y_flujos.mmd`](file:///home/marco/Projects/NexoVitalis360/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/mermaid_02_mapa_apis_y_flujos.mmd)

```mermaid
{MERMAID_02.strip()}
```

---

## 4. Matriz Completa de Trazabilidad RNF-0001 a RNF-0027 (ISO/IEC 25010)

> Fuente editable: [`mermaid_03_matriz_rnf_sistema.mmd`](file:///home/marco/Projects/NexoVitalis360/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/mermaid_03_matriz_rnf_sistema.mmd)

```mermaid
{MERMAID_03.strip()}
```

---

## 5. Patrón Pizarra (RNF-0027) + Tuberías/Filtros & Lotes Secuenciales (Plantilla 8)

> Fuente editable: [`mermaid_04_pizarra_y_circuitos_criticos.mmd`](file:///home/marco/Projects/NexoVitalis360/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/mermaid_04_pizarra_y_circuitos_criticos.mmd)

```mermaid
{MERMAID_04.strip()}
```
"""
    out_md_vl = os.path.join(VL_DIR, "DIAGRAMA_BLOQUES_FUNCIONALES_DEFINITIVO_MERMAID.md")
    out_md_comp = os.path.join(COMP_DIR, "DIAGRAMA_BLOQUES_FUNCIONALES_DEFINITIVO_MERMAID.md")
    with open(out_md_vl, "w", encoding="utf-8") as f:
        f.write(md_doc)
    with open(out_md_comp, "w", encoding="utf-8") as f:
        f.write(md_doc)

    print(f"Generados {len(files)} archivos .mmd y {out_md_vl}")
    return files


if __name__ == "__main__":
    build_all_mermaid()

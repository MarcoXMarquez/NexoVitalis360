# Control de Versiones y Trazabilidad de Diagramas Arquitectónicos (NexoVitalis360)

Este documento describe la estructura organizativa, el esquema de versionamiento y la matriz de trazabilidad de los artefactos visuales y diagramas contenidos en `05_DIAGRAMAS_Y_RECURSOS_EDITABLES` para el proyecto **NexoVitalis360** (Universidad Nacional de San Agustín - EPIS / RuwayLabs).

---

## 1. Esquema de Versionamiento

| Versión | Denominación | Formato | Descripción |
| :---: | :--- | :---: | :--- |
| **`v00.10`** | Diagramas Preliminares / Borrador | `.png` | Diagramas iniciales de trabajo derivados de las primeras iteraciones de diseño y bosquejos conceptuales. |
| **`v00.20`** | Diagramas Oficiales de Hito | `.png` / `.html` | Diagramas vectoriales de alta resolución generados desde los modelos HTML interactivos en estado nativo (*sharp edges*, paleta B&W pura, flujos correlativos y textos optimizados). |
| **`v01.00`** | Visor Integrado y Documento Consolidado | `.html` / `.docx` | Suite interactiva unificada con navegación por plantillas y documento Word formal con especificación completa. |

---

## 2. Estructura Jerárquica por Plantillas del Curso

La carpeta se encuentra organizada en subdirectorios correspondientes a las **8 plantillas arquitectónicas** del curso de Diseño y Arquitectura de Software:

```text
05_DIAGRAMAS_Y_RECURSOS_EDITABLES/
├── 01_Arquitectura_Generica/
│   ├── diagrama_arquitectura_generica_v00.10.png
│   ├── Figura_2_1_Arquitectura_Generica_v00.20.png
│   └── Figura_2_1_Arquitectura_Generica_v00.20.html
│
├── 02_Diagrama_Comportamiento/
│   ├── [v00.10 - 8 diagramas históricos preliminares]
│   │   ├── Figura_1_Comportamiento_General_v00.10.png
│   │   ├── Figura_2_Maquina_Estados_Cita_Medica_v00.10.png
│   │   ├── Figura_3_Secuencia_Registro_Cita_v00.10.png
│   │   ├── Figura_4_Secuencia_Reprogramacion_Cita_v00.10.png
│   │   ├── Figura_5_Secuencia_Teleconsulta_Recordatorio_v00.10.png
│   │   ├── Figura_6_Actividad_Pretriaje_Consentimiento_v00.10.png
│   │   ├── Figura_7_Actividad_Liquidacion_Profesional_v00.10.png
│   │   └── Figura_8_Maquina_Estados_Recordatorio_Cita_v00.10.png
│   └── [v00.20 - 5 diagramas oficiales de arquitectura]
│       ├── Figura_7_1_Contexto_Modular_Citas_v00.20.png (.html)
│       ├── Figura_7_2_Contexto_Global_Nivel0_v00.20.png (.html)
│       ├── Figura_7_3_Bloques_Funcionales_Nivel1_v00.20.png (.html)
│       ├── Figura_7_4_Maquina_Estados_Cita_v00.20.png (.html)
│       └── Figura_7_5_Secuencia_Arquitectura_v00.20.png (.html)
│
├── 03_Vista_Logica/                      (En preparación / Hito 1)
├── 04_Vista_Procesos/                    (Planificado / Hito 2)
├── 05_Vista_Fisica/                      (Planificado / Hito 2)
├── 06_Arquitectura_Centrada_Datos/       (Planificado / Hito 2)
├── 07_GUIs_Interfaces/                   (Planificado / Hito 2)
├── 08_Flujo_Datos/                       (Planificado / Hito 3)
└── VISOR_HTML_ARQUITECTURA_v01.00/       (Suite interactiva unificada con menú de carpetas)
    ├── index.html
    ├── fig2_1_arquitectura_generica.html
    ├── fig7_1_contexto_modular_citas.html
    ├── fig7_2_contexto_global_nivel0.html
    ├── fig7_3_bloques_funcionales_nivel1.html
    ├── fig7_4_maquina_estados_cita.html
    ├── fig7_5_secuencia_agendamiento.html
    └── README.md
```

---

## 3. Matriz de Trazabilidad: Requisitos vs. Diagramas Oficiales (`v00.20`)

| Figura | Nombre del Diagrama Oficial | Archivo v00.20 | Requisitos del Catálogo (EDUs / RNFs) |
| :---: | :--- | :--- | :--- |
| **Fig 2.1** | Arquitectura Genérica de Software | `Figura_2_1_Arquitectura_Generica_v00.20.png` | Arquitectura multicapa desacoplada (Capas 1 a 5), JWT, RBAC, PostgreSQL ACID. |
| **Fig 7.1** | Contexto Modular (Subsistema B4 Citas) | `Figura_7_1_Contexto_Modular_Citas_v00.20.png` | EDU-0008, EDU-0012, EDU-0013, EDU-0018, RNF-0004 (Anticolisión). |
| **Fig 7.2** | Contexto Global Nivel 0 (Caja Negra) | `Figura_7_2_Contexto_Global_Nivel0_v00.20.png` | Cobertura perimetral total: EDU-0008 a EDU-0038, SUNAT, Meet, Pasarela. |
| **Fig 7.3** | Bloques Funcionales Nivel 1 | `Figura_7_3_Bloques_Funcionales_Nivel1_v00.20.png` | 11 Bloques funcionales (B1 a B11), 28 flujos correlativos (F1 a F28), 100% de requisitos. |
| **Fig 7.4** | Máquina de Estados del Ciclo de Vida | `Figura_7_4_Maquina_Estados_Cita_v00.20.png` | EDU-0008, EDU-0012, EDU-0013, RNF-0004 (8 estados, guardas formales, 3 finales). |
| **Fig 7.5** | Diagrama de Agendamiento | `Figura_7_5_Secuencia_Arquitectura_v00.20.png` | EDU-0012, EDU-0019, RNF-0004 (Traza sincrónica/asincrónica de 14 pasos en 5 capas). |

---

## 4. Trazabilidad de Evolución (`v00.10` $\rightarrow$ `v00.20`)

1. **Eliminación de Redundancia y Ambigüedad:**
   - En `v00.10`, existían tres diagramas de secuencia separados (`Figura_3`, `Figura_4`, `Figura_5`). En `v00.20`, se unificaron formalmente bajo el **Diagrama de Agendamiento (Figura 7.5)**, cubriendo el ciclo completo transaccional de agendamiento y aprovisionamiento de Google Meet en 14 pasos estrictamente cronológicos.
   - En `v00.10`, las actividades de pretriaje y liquidación estaban fragmentadas. En `v00.20`, se integraron sistémicamente como flujos correlativos (F2, F8, F10, F28) en el **Diagrama de Bloques Funcionales Nivel 1 (Figura 7.3)**.
2. **Estandarización Notacional:**
   - La versión `v00.20` adopta estrictamente la notación UML 2.5 y diagramas de bloques formales con esquinas filosas (*sharp edges*), grosor vectorial de 2.8px y eliminación de elementos extra-estándar en el lienzo.

## Entrega Hito 2: Vistas Lógica, Procesos y Física (v01.10 - Actualización por Feedback Docente)

Conforme a las recomendaciones del docente M.Sc. Percy Oscar Huertas Niquén:
1. El **Diagrama de Bloques Funcionales Nivel 1** se integra al cuerpo principal de la **Vista Lógica** (Sección 7.3) para representar formalmente la descomposición funcional modular.
2. El **Diagrama de Clases UML 2.5** se traslada como **Anexo 1** (Sección 11) como especificación técnica de bajo nivel.
3. Se corrigen las flechas en el Proceso 01 (`ILA-0017`) y se eliminan los títulos flotantes del canvas.

| Código | Diagrama Oficial | Archivo HTML Interactivo | Archivo PNG 300 DPI | Cobertura Formal |
| :--- | :--- | :--- | :--- | :--- |
| **FIG-3.1** | Vista Lógica: Interconexión Modular | `fig3_1_vista_logica_educciones.html` | `Figura_3_1_Vista_Logica_Educciones_v01.00.png` | 27 Educciones (EDU-0008 a EDU-0038) en 6 Paquetes (Cero RNF) |
| **FIG-3.2** | Vista Lógica: Bloques Funcionales Nivel 1 | `fig7_3_bloques_funcionales_nivel1.html` / `fig3_3_vista_logica_bloques_funcionales.html` | `Figura_3_3_Vista_Logica_Bloques_Funcionales_v01.00.png` | 11 Bloques (B1 a B11), 28 Flujos Correlativos (F1 a F28) y Frontera del Sistema |
| **FIG-4.1** | Vista Procesos: ILA-0017 Cita Médica | `fig4_1_vista_procesos_ila0017.html` | `Figura_4_1_Vista_Procesos_ILA0017_v01.00.png` | BPMN 2.0 en Bonita BPM, 5 Carriles y Lock Pesimista (Flechas reparadas) |
| **FIG-4.2** | Vista Procesos: ILA-0062 Alerta Roja | `fig4_2_vista_procesos_ila0062.html` | `Figura_4_2_Vista_Procesos_ILA0062_v01.00.png` | BPMN 2.0 en Bonita BPM, 4 Carriles y WebSockets |
| **FIG-4.3** | Vista Procesos: ILA-0106 Facturación | `fig4_3_vista_procesos_ila0106.html` | `Figura_4_3_Vista_Procesos_ILA0106_v01.00.png` | BPMN 2.0 en Bonita BPM, XML UBL 2.1, Firma X.509 y CDR |
| **FIG-5.1** | Vista Física: Despliegue UML | `fig5_1_vista_fisica_despliegue.html` | `Figura_5_1_Vista_Fisica_Despliegue_v01.00.png` | 4 Zonas Físicas, pagefile.sys, Puertos y RNF-0001 a RNF-0025 |
| **ANX-1** | Anexo 1: Clases UML 2.5 y Dominio | `fig3_2_vista_logica_clases_uml.html` / `Anexo_1_Vista_Logica_Clases_UML.html` | `fig3_2_vista_logica_clases_uml.png` | Modelo de Dominio Clínico de Bajo Nivel, Herencia Persona y Tablas TB_* |

---

## Entrega Hito 3 / Fase 1: Arquitectura Centrada en Datos y GUIs/Interfaces (v01.20)

Conforme a la directiva pedagógica de diseño del docente M.Sc. Percy Oscar Huertas Niquén (*"La arquitectura se elabora pensando en el equipo de codificadores"*), se incorporan las Plantillas 6 y 7 sincronizadas con los nuevos requisitos no funcionales `RNF-0026` (Perfil del Equipo de Codificadores) y `RNF-0027` (Arquitectura de Pizarra para Soporte a Decisiones Clínicas):

1. **Plantilla 6 (Arquitectura Centrada en Datos):** Modela tanto el Repositorio Central Pasivo (`Vitalis_BD`) con PostgreSQL 16 y MinIO, como el patrón colaborativo Pizarra (*Blackboard*) para pre-triaje y Alerta Roja con 4 Fuentes de Conocimiento (KSs) autónomas (según Diapositiva 70).
2. **Plantilla 7 (GUIs e Interfaces):** Modela el Árbol de Navegación Jerárquico por Roles (RBAC) y el Flujo Operacional de Pantallas y Modales de Seguridad, garantizando cumplimiento de las Heurísticas de Jakob Nielsen y las 8 Reglas de Oro de Ben Shneiderman.

| Código | Diagrama Oficial | Archivo Vectorial SVG | Visor Interactivo HTML | Render Oficial PNG 300 DPI | Trazabilidad de Requisitos y Cobertura |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FIG-6.1** | Arquitectura Centrada en Datos: Repositorio Centralizado (`Vitalis_BD`) | `fig6_1_arquitectura_repositorio_datos.svg` | `fig6_1_arquitectura_repositorio_datos.html` | `Figura_6_1_Arquitectura_Repositorio_Datos_v01.00.png` | Repositorio pasivo PostgreSQL 16 ACID, PgBouncer, MinIO Object Storage, sharding mensual de auditoría y 6 subsistemas backend activos (`RNF-0003`, `RNF-0006`, `RNF-0016`, `RNF-0021`, `RNF-0026`). |
| **FIG-6.2** | Arquitectura Centrada en Datos: Estilo Pizarra / Blackboard para Triaje y Alerta Roja | `fig6_2_arquitectura_pizarra_clinica.svg` | `fig6_2_arquitectura_pizarra_clinica.html` | `Figura_6_2_Arquitectura_Pizarra_Clinica_v01.00.png` | Patrón Pizarra de Hayes-Roth/Tao con Pizarra Central de Estado multinivel, 4 Fuentes de Conocimiento (`KS-01` a `KS-04`), Control Heurístico y Despachador de Alerta Roja (`RNF-0027`, `EDU-0018`, `EDU-0022`, Diapositiva 70). |
| **FIG-7.1** | GUIs e Interfaces: Árbol de Navegación Jerárquico por Roles (RBAC) | `fig7_1_arbol_navegacion_roles.svg` | `fig7_1_arbol_navegacion_roles.html` | `Figura_7_1_Arbol_Navegacion_Roles_v01.00.png` | Jerarquía de navegación para 3 portales: Tutor Legal (`/app/tutor/*`), Profesional Médico (`/app/medico/*`), Administrador (`/app/admin/*`) y Sala WebRTC común (`RNF-0018`, `RNF-0026`, Nielsen). |
| **FIG-7.2** | GUIs e Interfaces: Flujo de Interacción y Gestión de Modales Clínicos | `fig7_2_flujo_interfaces_modales.svg` | `fig7_2_flujo_interfaces_modales.html` | `Figura_7_2_Flujo_Interfaces_Modales_v01.00.png` | Flujo operacional de interfaz, microinteracciones, modales no descartables de consentimiento informado, pre-triaje y Alerta Roja (`RNF-0018`, `RNF-0026`, `RNF-0027`, Shneiderman). |

---

## Entrega Hito 3 / Arquitectura Definitiva Integral: Entry Points + GUIs + ESP/Pruebas + Mermaid (v02.10)

Consolida sobre la frontera del Diagrama de Bloques Funcionales (`EP-01..EP-06`, `B0..B12`, `EXT-A1..A4`, `EXT-API1..4`, `INFRA-STD`, `CTX-CAT` y `LEGEND`) la trazabilidad completa e inspeccionable hacia todo el Catálogo de Requisitos (`v01.00`), APIs REST/WSS/Webhooks, persistencia PostgreSQL/MinIO/Redis, Pizarra Blackboard (`RNF-0027`), Tuberías/Filtros (`B8`) y Lotes Secuenciales (`B9`, Plantilla 8), procesos Bonita (`ILA-0017`, `ILA-0062`, `ILA-0106`) y perfil técnico del equipo codificador (`RNF-0026`), acompañado de la suite oficial Mermaid:

| Código | Artefacto Definitivo (`v02.10`) | Ubicación Principal / Visor | Ubicación Espejo / Editable | Cobertura Exacta Verificada |
| :--- | :--- | :--- | :--- | :--- |
| **DEF-HTML** | Diagrama Definitivo de Bloques Funcionales Integral | `VISOR_HTML_ARQUITECTURA_v01.00/fig_definitivo_bloques_funcionales_integral.html` | `03_Vista_Logica/Figura_3_4_Bloques_Funcionales_Integral_Definitivo_v02.00.html` y `02_Diagrama_Comportamiento/Figura_7_6_Bloques_Funcionales_Definitivo_v02.00.html` | `30` tarjetas (`EP-01..06` + `B0..B12` + `EXT-*`), `39` flujos (`F1`..`F39`), `27/27` EDU, `108/108` ILA + Riesgos, `104/108` fichas ESP (`CAPTURA_EVENTO`/`BTN_*`), `113` Pruebas (`T-001..T-020`), `28/28` RNF (`01..27`), ubicación exacta de `28` GUI / `140` MDL y `27` Tablas `TB_*`. |
| **DEF-MMD** | Suite Oficial de 5 Diagramas Mermaid (.md + .mmd) | Embebida 100% offline en `fig_definitivo_bloques_funcionales_integral.html` (`vendor/mermaid.min.js`) | `03_Vista_Logica/DIAGRAMA_BLOQUES_FUNCIONALES_DEFINITIVO_MERMAID.md` + `mermaid_01..05.mmd` (`02_Diagrama_Comportamiento/` copia `.md`) | Vista Integral Zonas/EP/5 Capas (`m1`), Mapa Entry Points & 28 GUIs (`m5`), APIs REST/WSS/Hooks (`m2`), Matriz RNF `01..27` (`m3`) y Pizarra Blackboard + Tuberías/Lotes Plantilla 8 (`m4`). |

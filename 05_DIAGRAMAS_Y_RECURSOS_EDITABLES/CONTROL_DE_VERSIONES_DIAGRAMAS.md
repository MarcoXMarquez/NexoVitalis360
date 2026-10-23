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

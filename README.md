# NexoVitalis360 - Diseño y Arquitectura de Software

**Universidad Nacional de San Agustín de Arequipa (UNSA)**  
**Facultad de Ingeniería de Producción y Servicios**  
**Escuela Profesional de Ingeniería de Sistemas (EPIS)**  
*Semestre 2026-B &bull; Equipo RuwayLabs (Grupo RUWAY)*

---

## 🏥 Descripción del Proyecto

**NexoVitalis360** es un sistema hospitalario integral especializado en neuropediatría, atención clínica asistencial y agendamiento multimodal (presencial, teleconsulta criptográfica WebRTC y atención domiciliaria). El sistema orquesta flujos clínicos, pre-triaje asistencial, consentimiento informado, historia clínica electrónica con codificación CIE-10, liquidación médica periódica y facturación electrónica integrada con SUNAT.

---

## 👥 Equipo de Trabajo (Grupo RUWAY / RuwayLabs)

- **Turpo Huanca, Wilson Josue**
- **Huamani Condori, Jeanpiero Sixto**
- **Arce Mayhua, Leonardo Ruben**
- **Venero Guevara, Christian Henry**
- **Alfonso Huacasi, Alejandro Sebastian**
- **Marquez Herrera, Marco Antonio**
- **Payehuanca Riquelme, Jhastyn Jefferson**
- **Gallegos Condori, Anette Isabel**

---

## 📁 Estructura del Repositorio

El repositorio se encuentra estructurado formalmente conforme a las fases y plantillas del curso:

```text
NexoVitalis360/
├── 00_ADMINISTRACION_Y_GESTION_EQUIPO/       # Actas, planificación y cronogramas
├── 01_LINEA_BASE_REQUERIMIENTOS/             # Catálogo oficial de requerimientos (EDUs / RNFs)
├── 02_FASE_1_ARQUITECTURA_GENERICA_Y_PATRONES/ # Entregables Fase 1 (Arquitectura Genérica y Comportamiento)
│   ├── Entregable_01_Arquitectura_Generica/
│   ├── Entregable_02_Arquitectura_Especifica/
│   │   └── DIAGRAMA_DE_COMPORTAMIENTO/       # Documento Word oficial consolidado (v01.00)
│   ├── Entregable_03_Patrones_Arquitectura/
│   └── Entregable_04_Patrones_Diseno/
├── 03_FASE_2_ESTILOS_Y_SERVICIOS_AVANZADOS/  # Planificación Fase 2 (Vistas Lógica, Procesos, Física)
├── 04_FASE_3_EVALUACION_Y_FRAMEWORKS/        # Planificación Fase 3 (Evaluación ATAM / Frameworks)
├── 05_DIAGRAMAS_Y_RECURSOS_EDITABLES/        # Modelos gráficos, versionamiento y visor interactivo
│   ├── 01_Arquitectura_Generica/             # Versiones v00.10 y v00.20 (PNG / HTML)
│   ├── 02_Diagrama_Comportamiento/           # Versiones v00.10 y v00.20 (PNG / HTML)
│   ├── 03_Vista_Logica/ a 08_Flujo_Datos/    # Carpetas preparadas para los siguientes hitos
│   ├── VISOR_HTML_ARQUITECTURA_v01.00/       # Suite interactiva HTML/SVG con menú por carpetas
│   └── CONTROL_DE_VERSIONES_DIAGRAMAS.md     # Matriz de trazabilidad y control de versiones
├── 06_ENTREGAS_OFICIALES_Y_FEEDBACK/         # Evaluaciones continuas e hitos de entrega
└── Material del curso/                       # Diapositivas, rúbricas y guías de cátedra
```

---

## 🖥️ Visor Interactivo de Arquitectura

Se incluye una suite navegable completa en HTML5/SVG interactivo con zoom semántico, renderizado B&W puro y esquinas rectas (*sharp edges*), accesible localmente abriendo:

📁 `05_DIAGRAMAS_Y_RECURSOS_EDITABLES/VISOR_HTML_ARQUITECTURA_v01.00/index.html`

### Diagramas Oficiales Incorporados (v00.20 / v01.00)
1. **Figura 2.1:** Arquitectura Genérica de Software (5 Capas Desacopladas y Servicios Externos).
2. **Figura 7.1:** Diagrama de Contexto Modular del Subsistema B4 (Gestión de Citas y Agendas).
3. **Figura 7.2:** Diagrama de Contexto Global Nivel 0 (NexoVitalis360 como Caja Negra).
4. **Figura 7.3:** Diagrama de Bloques Funcionales Nivel 1 (11 Bloques B1-B11 y 28 Flujos F1-F28).
5. **Figura 7.4:** Diagrama de Máquina de Estados del Ciclo de Vida de la Cita Médica (8 estados deterministas).
6. **Figura 7.5:** Diagrama de Secuencia de Arquitectura (Escenario de Agendamiento en 14 pasos a través de las 5 capas).

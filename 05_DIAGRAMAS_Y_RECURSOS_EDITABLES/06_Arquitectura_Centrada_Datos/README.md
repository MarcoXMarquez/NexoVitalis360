# 06 - Arquitectura Centrada en Datos (Plantilla 6 / Hito 3)

## Descripción General
Este directorio contiene los modelos arquitectónicos oficiales, especificaciones técnicas y diagramas correspondientes a la **Plantilla 6: Arquitectura Centrada en Datos** del proyecto **NexoVitalis360** (Universidad Nacional de San Agustín - EPIS / RuwayLabs).

En concordancia con los lineamientos del docente M.Sc. Percy Oscar Huertas Niquén y las diapositivas del curso (*Software Architecture Illuminated*, Diapositiva 70), los sistemas modernos no se limitan a un único estilo arquitectónico para los datos. En NexoVitalis360 se han formalizado **dos estilos complementarios de arquitectura centrada en datos**:
1. **Estilo Repositorio Pasivo:** Para la persistencia transaccional ACID, almacenamiento seguro de expedientes clínicos y sincronización multiproceso.
2. **Estilo Pizarra (Blackboard):** Para el soporte colaborativo a decisiones diagnósticas complejas y triaje asistido en tiempo real mediante fuentes de conocimiento autónomas.

---

## 1. Catálogo de Diagramas Oficiales

| Código | Diagrama Oficial | Archivo Vectorial SVG | Visor Interactivo HTML | Render Oficial PNG 300 DPI | Trazabilidad de Requisitos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FIG-6.1** | Arquitectura Centrada en Datos: Repositorio Centralizado (`Vitalis_BD`) | `fig6_1_arquitectura_repositorio_datos.svg` | `fig6_1_arquitectura_repositorio_datos.html` | `Figura_6_1_Arquitectura_Repositorio_Datos_v01.00.png` | `RNF-0003`, `RNF-0006`, `RNF-0016`, `RNF-0021`, `RNF-0026` |
| **FIG-6.2** | Arquitectura Centrada en Datos: Estilo Pizarra / Blackboard para Triaje y Alerta Roja | `fig6_2_arquitectura_pizarra_clinica.svg` | `fig6_2_arquitectura_pizarra_clinica.html` | `Figura_6_2_Arquitectura_Pizarra_Clinica_v01.00.png` | `RNF-0027`, `EDU-0018`, `EDU-0022`, `EDU-0025`, Diapositiva 70 |

---

## 2. Especificación Técnica de los Modelos

### 2.1 FIG-6.1: Estilo Repositorio Centralizado (`Vitalis_BD`)
- **Topología de Repositorio:** El repositorio pasivo centraliza la persistencia relacional estricta en PostgreSQL 16 con aislamiento transaccional `READ COMMITTED` y `SERIALIZABLE` para evitar colisiones en reservas de citas (`RNF-0004`).
- **Gestión de Conexiones:** Se intercala un Connection Pooler PgBouncer en modo transacción (`pool_size=50`, `max_client_conn=1000`) para mitigar el consumo de memoria en picos de concurrencia.
- **Almacenamiento de Documentos e Imágenes Clínicas:** MinIO Object Storage (compatible con S3) gestiona expedientes PDF firmados, recetas médicas y multimedia, desacoplado del motor relacional mediante URIs canónicas.
- **Sharding y Auditoría Temporal:** Esquema `audit_logs` particionado por rango mensual con retención garantizada de 5 años bajo estándar HIPAA/MINSA.
- **Acceso de Clientes Activos:** 6 subsistemas independientes del backend (Gestión de Citas, Expediente Clínico Electrónico, Facturación Electrónica UBL 2.1, Triaje Automatizado, Teleconsulta WebRTC y Notificaciones Push) interactúan con el repositorio centralizado mediante repositorios desacoplados (Patrón Repository).

### 2.2 FIG-6.2: Estilo Pizarra / Blackboard (Pre-Triaje y Alerta Roja)
- **Justificación Teórica:** Siguiendo la Diapositiva 70 del curso y el modelo clásico de Barbara Hayes-Roth (1985), el estilo Pizarra es la solución óptima cuando múltiples fuentes de conocimiento heterogéneas deben colaborar de forma oportunista sobre un problema de diagnóstico no determinista.
- **Componente 1 - Pizarra Central (Blackboard Data Store):**
  - Almacena el estado transitorio de la sesión diagnóstica estructurado en niveles de abstracción:
    - *Nivel 1 (Datos Crudos):* Signos vitales, saturación SpO2, temperatura, cuestionario de TEA/TDAH.
    - *Nivel 2 (Hipótesis Clínicas):* Probabilidad de descompensación neurológica/respiratoria, alertas tempranas.
    - *Nivel 3 (Decisión y Plan Asistencial):* Clasificación Manchester/ESI (Nivel I a V), activación de Alerta Roja.
- **Componente 2 - Fuentes de Conocimiento (Knowledge Sources - KS):**
  - Módulos autónomos e independientes que solo interactúan a través de la pizarra:
    - `KS-01: Analizador de Signos Vitales y Triaje Pediátrico` (Monitorea frecuencias cardíacas y SpO2).
    - `KS-02: Evaluador Heurístico TEA/TDAH` (Pondera indicadores de neurodesarrollo).
    - `KS-03: Validador de Reglas Bioéticas y Consentimiento Informado` (Inspecciona la validez legal del tutor).
    - `KS-04: Gestor de Disponibilidad de Especialistas de Guardia` (Consulta agendas en tiempo real).
- **Componente 3 - Módulo de Control Heurístico (Blackboard Controller):**
  - Monitoriza los cambios en la pizarra, evalúa la agenda de KSs elegibles, resuelve prioridades mediante cola heurística y despacha la ejecución del KS óptimo.
  - Al detectar condiciones de riesgo vital inminente (ej. SpO2 < 90% o shock anafiláctico), dispara inmediatamente el flujo de **Alerta Roja** hacia la central de emergencias y el especialista asignado.

---

## 3. Formatos y Recursos Editables
- Todos los diagramas cuentan con:
  - Archivo fuente vectorial `.svg` generado bajo estándares XML estrictos, paleta 100% monocromática (B&W puro) y esquinas 100% rectas (*sharp edges*).
  - Interfaz web interactiva `.html` con HUD de control de zoom semántico, navegación panorámica (*pan*), visualización a pantalla completa y modal de inspección dual-view.
  - Compilación rasterizada oficial `.png` a **300 DPI** generada directamente mediante el motor Inkscape, apta para inclusión en memorias técnicas y documentos Word de alta fidelidad.

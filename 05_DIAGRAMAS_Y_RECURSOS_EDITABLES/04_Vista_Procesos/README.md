# 04 - Vista de Procesos (Hito 2 / NexoVitalis360)

## 1. Directriz y Regla Estricta de Cátedra (M.Sc. Percy Oscar Huertas Niquén)
> *"¿Dónde están los procesos dentro del catálogo de requisitos? En la **Ilación**. Las ilaciones en la parte de la descripción tienen unos numeritos que van en orden: 1, 2, 3... Esos son procesos. Si las ilaciones les causan cierto nivel de desconocimiento o complejidad, para esa ilación se hace la vista de procesos. Escojan 3 ilaciones representativas en un diagrama de procesos o diagrama de flujo con **Bonita BPM**."*

---

## 2. Artefactos y Procesos Modelados en BPMN 2.0 (Bonita BPM)

### Figura 7.1: Proceso 01 — ILA-0017 Crear Registro de Cita Médica
- **Archivo Interactivo HTML:** [`Figura_4_1_Vista_Procesos_ILA0017_v01.00.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/Figura_4_1_Vista_Procesos_ILA0017_v01.00.html) / [`fig4_1_vista_procesos_ila0017.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/fig4_1_vista_procesos_ila0017.html)
- **Render Gráfico Oficial (300 DPI):** [`Figura_4_1_Vista_Procesos_ILA0017_v01.00.png`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/Figura_4_1_Vista_Procesos_ILA0017_v01.00.png)
- **Script Generador Python:** `scripts/09_diagrama_vista_procesos_ila0017.py`
- **Carriles BPMN (Swimlanes):**
  1. *Paciente / Tutor:* Solicitud de cita médica y selección de modalidad en PWA.
  2. *Recepción / Admisión:* Comprobación de filiación, consentimientos y tutela legal.
  3. *Backend NexoVitalis360:* Orquestación de reglas de negocio en Spring Boot / Bonita Engine.
  4. *Base de Datos PostgreSQL:* Bloqueo pesimista anticolisión de turnos (`SELECT FOR UPDATE`) y commit transaccional ACID.
  5. *Servicios Externos:* Generación síncrona de enlaces de Google Meet API (OAuth2) y notificación vía WhatsApp Gateway.

---

### Figura 7.2: Proceso 02 — ILA-0062 Crear Pre-Triaje Clínico y Alerta Roja
- **Archivo Interactivo HTML:** [`Figura_4_2_Vista_Procesos_ILA0062_v01.00.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/Figura_4_2_Vista_Procesos_ILA0062_v01.00.html) / [`fig4_2_vista_procesos_ila0062.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/fig4_2_vista_procesos_ila0062.html)
- **Render Gráfico Oficial (300 DPI):** [`Figura_4_2_Vista_Procesos_ILA0062_v01.00.png`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/Figura_4_2_Vista_Procesos_ILA0062_v01.00.png)
- **Script Generador Python:** `scripts/10_diagrama_vista_procesos_ila0062.py`
- **Carriles BPMN (Swimlanes):**
  1. *Personal de Enfermería / Triaje:* Captura táctil de signos vitales pediátricos (SpO2, FC, FR, Temp, GCS) en tablet hospitalaria.
  2. *Motor de Reglas Clínicas:* Evaluación automatizada contra tablas percentiladas pediátricas y detección de umbrales de shock.
  3. *Médico Especialista / Guardia:* Interrupción prioritaria en pantalla de consultorio y preparación de box de reanimación.
  4. *Servicio de Alertas y WebSockets:* Emisión de evento STOMP prioritario y alarma persistente sonora y visual en la estación médica.

---

### Figura 7.3: Proceso 03 — ILA-0106 Crear Comprobante de Pago Electrónico SUNAT UBL 2.1
- **Archivo Interactivo HTML:** [`Figura_4_3_Vista_Procesos_ILA0106_v01.00.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/Figura_4_3_Vista_Procesos_ILA0106_v01.00.html) / [`fig4_3_vista_procesos_ila0106.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/fig4_3_vista_procesos_ila0106.html)
- **Render Gráfico Oficial (300 DPI):** [`Figura_4_3_Vista_Procesos_ILA0106_v01.00.png`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/04_Vista_Procesos/Figura_4_3_Vista_Procesos_ILA0106_v01.00.png)
- **Script Generador Python:** `scripts/11_diagrama_vista_procesos_ila0106.py`
- **Carriles BPMN (Swimlanes):**
  1. *Cajero / Facturación:* Selección de prestación atendida, ingreso de medio de pago e impresión de ticket térmico con código QR.
  2. *Módulo de Cobros y Caja:* Aplicación de convenios, cálculo tributario de IGV y correlativo oficial (B001 / F001).
  3. *Facturador Electrónico UBL 2.1 (Docker):* Construcción del XML OASIS UBL 2.1, firma digital X.509 SHA-256 y compresión en ZIP.
  4. *Servicio Web OSE / SUNAT:* Validación tributaria reglamentaria, emisión de Constancia de Recepción (CDR) y resguardo en MinIO S3.

---

## 3. Características del Visor Interactivo
- **Diseño BPMN 2.0 Estricto:** Carriles claramente delimitados, compuertas exclusivas XOR en rombo, eventos de inicio y fin reglamentarios.
- **Zoom Semántico:** Vista macro con títulos claros de tareas y vista cercana con descripciones operativas completas de cada paso.
- **Acceso Dual-View:** Botón en el HUD para desplegar la imagen PNG renderizada a 300 DPI generada por el script de Matplotlib.

# 07 - GUIs e Interfaces (Plantilla 7 / Hito 3)

## Descripción General
Este directorio contiene los modelos arquitectónicos oficiales, especificaciones de interacción y diagramas de navegación correspondientes a la **Plantilla 7: GUIs e Interfaces** del proyecto **NexoVitalis360** (Universidad Nacional de San Agustín - EPIS / RuwayLabs).

En apego estricto a las directivas del docente M.Sc. Percy Oscar Huertas Niquén (*"La arquitectura se prepara para los codificadores y desarrolladores; si se requiere una vista de pantallas e interfaces, es para que el equipo de implementación tenga una guía inequívoca y atómica del producto"*), esta plantilla modela con máxima granularidad:
1. La jerarquía de rutas, vistas y segregación de navegación según los roles de seguridad (RBAC).
2. Los flujos operacionales entre pantallas, la gestión reactiva de ventanas modales críticas y la aplicación de principios de usabilidad clínica (Heurísticas de Jakob Nielsen y las 8 Reglas de Oro de Ben Shneiderman).

---

## 1. Catálogo de Diagramas Oficiales

| Código | Diagrama Oficial | Archivo Vectorial SVG | Visor Interactivo HTML | Render Oficial PNG 300 DPI | Trazabilidad de Requisitos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FIG-7.1** | GUIs e Interfaces: Árbol de Navegación Jerárquico por Roles (RBAC) | `fig7_1_arbol_navegacion_roles.svg` | `fig7_1_arbol_navegacion_roles.html` | `Figura_7_1_Arbol_Navegacion_Roles_v01.00.png` | `RNF-0018`, `RNF-0026`, `EDU-0008` a `EDU-0038`, Nielsen / Shneiderman |
| **FIG-7.2** | GUIs e Interfaces: Flujo de Interacción y Gestión de Modales Clínicos | `fig7_2_flujo_interfaces_modales.svg` | `fig7_2_flujo_interfaces_modales.html` | `Figura_7_2_Flujo_Interfaces_Modales_v01.00.png` | `RNF-0018`, `RNF-0026`, `RNF-0027`, `ILA-0017`, `ILA-0062`, `ILA-0106` |

---

## 2. Especificación Técnica de los Modelos

### 2.1 FIG-7.1: Árbol de Navegación Jerárquico por Roles (RBAC)
- **Topología de Navegación:** Estructura jerárquica de árbol con layout compartido para componentes comunes (Barra de estado, header de usuario, notificaciones en tiempo real) y ramificaciones segregadas mediante guardas de ruta (`AuthGuard` y `RoleGuard`).
- **Rol 1 — Portal Tutor Legal (`/app/tutor/*`):**
  - Vistas principales: Dashboard Familiar, Agendamiento de Citas Médicas (`/citas/nueva`), Cuestionario de Pre-Triaje Clínico (`/citas/:id/pretriaje`), Historial de Consultas y Descarga de Recetas/Comprobantes SUNAT (`/expediente`).
- **Rol 2 — Estación Profesional de Salud (`/app/medico/*`):**
  - Vistas principales: Agenda del Día y Lista de Pacientes en Espera, Estación de Trabajo de Consulta (`/consulta/:id`), Formulario de Historia Clínica Electrónica con diagnósticos CIE-10/CIE-11, Generador de Prescripción Farmacológica con firma digital y Módulo de Liquidaciones Quincenales.
- **Rol 3 — Consola de Administración (`/app/admin/*`):**
  - Vistas principales: Panel de Control Asistencial, Gestión de Usuarios y Especialistas (`/usuarios`), Configuración de Tarifarios y Reglas de Negocio, Auditoría del Sistema y Trazabilidad Transaccional (`/auditoria`).
- **Módulo Transversal Crítico — Teleconsulta y Alerta Roja (`/app/teleconsulta/:id`):**
  - Sala Virtual WebRTC de alta definición con panel de signos vitales en vivo, chat encriptado de soporte y botón flotante de disparo manual de **Alerta Roja**.

### 2.2 FIG-7.2: Flujo de Interacción y Gestión de Modales Clínicos
- **Flujo Operacional y Modales:** Modela los estados transicionales de la interfaz de usuario, desde la exploración de profesionales hasta la finalización de la atención asistencial, destacando las bifurcaciones y bloqueos de seguridad mediante diálogos modales.
- **Puntos Críticos de Interacción Modelados:**
  1. *Modal de Selección de Horario:* Previene colisiones mediante refresco de slots en tiempo real.
  2. *Modal de Consentimiento Informado Legal:* Bloqueo estricto que exige firma digital o aceptación explícita del tutor antes de iniciar cualquier procedimiento pediátrico (`RNF-0018`).
  3. *Pre-Triaje Reactivo y Alerta Temprana:* Captura dinámica de síntomas y constantes vitales con validación inmediata en cliente.
  4. *Modal Crítico de Alerta Roja:* Interrupción modal no descartable que activa señalética de emergencia, notificación visual y auditiva, enlace WebRTC inmediato y despacho de llamada prioritaria a la central de ambulancias.
  5. *Modal de Pasarela de Pagos y Emisión SUNAT:* Integración con Culqi/Niubiz y generación síncrona de comprobante electrónico UBL 2.1 con código QR.
- **Fundamentos de Usabilidad Aplicados:**
  - *Heurísticas de Jakob Nielsen:* Visibilidad del estado del sistema (spinners, barras de progreso y toasts), prevención de errores (confirmación previa a cobros o cancelaciones), y consistencia y estándares en toda la iconografía médica.
  - *8 Reglas de Oro de Shneiderman:* Reducción de la carga de memoria a corto plazo (autocompletado CIE-10), soporte de control interno al usuario (botones claros de regreso y cierre) y feedback informativo en cada acción transaccional.

---

## 3. Formatos y Recursos Editables
- Todos los diagramas cuentan con:
  - Archivo fuente vectorial `.svg` generado bajo estándares XML estrictos, paleta 100% monocromática (B&W puro) y esquinas 100% rectas (*sharp edges*).
  - Interfaz web interactiva `.html` con HUD de control de zoom semántico, navegación panorámica (*pan*), visualización a pantalla completa y modal de inspección dual-view.
  - Compilación rasterizada oficial `.png` a **300 DPI** generada directamente mediante el motor Inkscape, apta para inclusión en memorias técnicas y documentos Word de alta fidelidad.

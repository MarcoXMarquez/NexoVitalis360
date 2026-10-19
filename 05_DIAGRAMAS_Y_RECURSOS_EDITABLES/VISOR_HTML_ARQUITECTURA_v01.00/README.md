# Visor Interactivo de Arquitectura de Software v01.00 (NexoVitalis360)

Este directorio contiene el portal interactivo y la suite completa de diagramas de arquitectura en formato HTML/SVG navegable con zoom semántico, renderizado B&W puro, esquinas 100% rectas (*sharp edges*) y soporte de visualización Dual-View (vectorial interactivo y render oficial en 300 DPI).

---

## Estructura de Archivos y Cobertura de Plantillas

### 1. Plantilla 1: Arquitectura Genérica
- **`fig2_1_arquitectura_generica.html`**: Diagrama de Arquitectura Genérica en 5 capas desacopladas, API Gateway con JWT/RBAC, 6 subsistemas clínicos y persistencia ACID.

### 2. Plantilla 2: Diagramas de Comportamiento
- **`fig7_1_contexto_modular_citas.html`**: Diagrama de Contexto Modular del Subsistema B4 (Gestión de Citas y Agendas).
- **`fig7_2_contexto_global_nivel0.html`**: Diagrama de Contexto Global Nivel 0 (NexoVitalis360 como Caja Negra y 8 entidades perimetrales).
- **`fig7_3_bloques_funcionales_nivel1.html`**: Diagrama de Bloques Funcionales Nivel 1 (11 bloques B1-B11 y 28 flujos correlativos F1-F28).
- **`fig7_4_maquina_estados_cita.html`**: Diagrama de Máquina de Estados del Ciclo de Vida de la Cita Médica (8 estados, guardas y 3 finales).
- **`fig7_5_secuencia_agendamiento.html`**: Diagrama de Agendamiento (Escenario transaccional en 14 pasos a través de las 5 capas).

### 3. Plantilla 3: Vista Lógica (Hito 2)
- **`fig3_1_vista_logica_educciones.html`**: Interconexión Modular de las 27 Educciones activas (EDU-0008 a EDU-0038) en 6 paquetes funcionales (`PKG-01` a `PKG-06`) y dependencias lógicas «use» y «import» (Cumple la regla estricta de CERO RNF).
- **`fig3_2_vista_logica_clases_uml.html`**: Diagrama de Clases UML 2.5 y Modelo de Dominio Clínico con herencia Persona, operaciones CRUD, relaciones de composición/agregación y mapeo a tablas físicas `TB_*`.

### 4. Plantilla 4: Vista de Procesos (Hito 2)
- **`fig4_1_vista_procesos_ila0017.html`**: Proceso 01 — `ILA-0017` Crear Registro de Cita Médica en Bonita BPM / BPMN 2.0 (5 carriles horizontales, compuertas XOR y bloqueo pesimista en base de datos).
- **`fig4_2_vista_procesos_ila0062.html`**: Proceso 02 — `ILA-0062` Crear Pre-Triaje Clínico y Alerta Roja en Bonita BPM / BPMN 2.0 (4 carriles, Drools Rule Engine y WebSockets prioritarios).
- **`fig4_3_vista_procesos_ila0106.html`**: Proceso 03 — `ILA-0106` Crear Comprobante de Pago Electrónico SUNAT UBL 2.1 en Bonita BPM / BPMN 2.0 (4 carriles, firma digital X.509 y CDR de SUNAT).

### 5. Plantilla 5: Vista Física (Hito 2)
- **`fig5_1_vista_fisica_despliegue.html`**: Diagrama de Despliegue UML 2.5 con topología en 4 zonas físicas, affordance visual de hardware (PC, Laptop, Smartphone multi-fabricante, Tablet, Servidor Rack, Cilindros BD), software base, memoria virtual `pagefile.sys 8GB`, puertos TCP y correspondencia 100% con `RNF-0001` a `RNF-0025`.

---

## Funcionalidades del Visor y Motor de Interacción

1. **Zoom Semántico Gradual:**
   - **Modo Macro (Sin zoom o zoom alejado):** Las tarjetas muestran exclusivamente títulos limpios y tipografía de alto impacto para una visión holística sin saturación.
   - **Modo Detalle (Zoom $\ge 1.18\times$ o botón *Modo: SIEMPRE DETALLES*):** Se despliegan automáticamente los atributos, métodos, ilaciones asociadas, especificaciones de hardware y memorias de paginación.
2. **Navegación Focalizada (*Focus on Click*):**
   - Al hacer clic en cualquier tarjeta (`.box-card`), la cámara realiza una transición suave hacia su centro geométrico, activando la clase `.focused` con borde grueso y sombra B&W, revelando sus detalles inmediatos.
3. **Modo Dual-View (Vectorial + Render Oficial 300 DPI):**
   - Cada diagrama HTML cuenta en su barra superior (HUD) con el botón **"Render PNG 300-DPI"**, que permite superponer o inspeccionar el render oficial de alta definición generado por Matplotlib.
4. **Navegación con Ratón y Teclado:**
   - **Arrastrar lienzo:** Panorámica libre (*Pan*).
   - **Rueda del ratón:** Zoom continuo hacia la posición exacta del cursor.
   - **Tecla `0` o botón `Ajustar`:** Ajuste perfecto a la resolución del monitor (*Fit-to-screen*).
   - **Tecla `+` / `-`:** Zoom escalonado in / out.
   - **Tecla `Escape`:** Cierra modales de imagen y restablece el enfoque.
   - **Tecla `M` o botón `◀`:** Contrae la barra lateral para visualización inmersiva.

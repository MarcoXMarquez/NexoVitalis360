# 03 - Vista Lógica (Hito 2 / NexoVitalis360)

## 1. Directriz y Regla Estricta de Cátedra (M.Sc. Percy Oscar Huertas Niquén)
> *"La Vista Lógica contiene una mirada de todo el sistema que se va a construir desde el ángulo de vista de sus aspectos de funcionalidad. ¿Dónde están los aspectos de funcionalidad? En las **Educciones**. Es un bloque compacto que muestra cómo se conectan los módulos. ¿Tiene algo que ver con los requisitos no funcionales? **No tiene nada que ver. Por lo tanto, en esta vista lógica no tiene que aparecer nada con respecto a los requisitos no funcionales**."*

---

## 2. Artefactos y Diagramas Oficiales

### Figura 7.1: Interconexión Modular de las 27 Educciones en 6 Paquetes
- **Archivo Interactivo HTML:** [`Figura_3_1_Vista_Logica_Educciones_v01.00.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/Figura_3_1_Vista_Logica_Educciones_v01.00.html) / [`fig3_1_vista_logica_educciones.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/fig3_1_vista_logica_educciones.html)
- **Render Gráfico Oficial (300 DPI):** [`Figura_3_1_Vista_Logica_Educciones_v01.00.png`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/Figura_3_1_Vista_Logica_Educciones_v01.00.png)
- **Script Generador Python:** `scripts/07_diagrama_vista_logica_educciones.py`
- **Descripción:** Mapea el 100% de las 27 educciones activas del catálogo de requerimientos (EDU-0008 a EDU-0038) organizadas en 6 subsistemas modulares («subsystem»):
  1. `PKG-01: Módulo de Filiación y Pre-Triaje` (EDU-0014, EDU-0021, EDU-0022, EDU-0023, EDU-0035)
  2. `PKG-02: Módulo de Citas y Agendas Médicas` (Núcleo Central: EDU-0008, EDU-0012, EDU-0013, EDU-0016, EDU-0017, EDU-0018)
  3. `PKG-03: Módulo de Historia Clínica y Terapias` (EDU-0010, EDU-0015, EDU-0020, EDU-0025, EDU-0026, EDU-0027, EDU-0034)
  4. `PKG-04: Módulo de Teleconsulta y Encuestas` (EDU-0019, EDU-0036)
  5. `PKG-05: Módulo de Pagos, Facturación y Caja` (EDU-0024, EDU-0028, EDU-0029, EDU-0037)
  6. `PKG-06: Módulo de Permisos, Auditoría y BI` (EDU-0009, EDU-0011, EDU-0038)
- **Dependencias Lógicas:** Relaciones formales `«use»` y `«import»` entre subsistemas que garantizan bajo acoplamiento y alta cohesión.

---

### Figura 7.2: Diagrama de Clases UML 2.5 y Modelo de Dominio
- **Archivo Interactivo HTML:** [`Figura_3_2_Vista_Logica_Clases_UML_v01.00.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/Figura_3_2_Vista_Logica_Clases_UML_v01.00.html) / [`fig3_2_vista_logica_clases_uml.html`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/fig3_2_vista_logica_clases_uml.html)
- **Render Gráfico Oficial (300 DPI):** [`Figura_3_2_Vista_Logica_Clases_UML_v01.00.png`](file:///C:/Users/marco/Desktop/TEO-DAS/DAS-GITHUB/05_DIAGRAMAS_Y_RECURSOS_EDITABLES/03_Vista_Logica/Figura_3_2_Vista_Logica_Clases_UML_v01.00.png)
- **Script Generador Python:** `scripts/08_diagrama_vista_logica_clases_uml.py`
- **Descripción:** Diagrama formal UML 2.5 que modela las entidades del dominio clínico, atributos con visibilidad tipada, operaciones CRUD, estereotipos arquitectónicos (`«entity»`, `«boundary»`, `«controller»`), multiplicidades y mapeo relacional a tablas físicas (`TB_*`):
  - **Jerarquía de Generalización:** Superclase abstracta `Persona` heredada por `Paciente`, `Apoderado` y `Especialista`.
  - **Relaciones de Composición:** `HistoriaClinica` $\blacklozenge$--- `EvolucionSesion`, `EvolucionSesion` $\blacklozenge$--- `DiagnosticoCIE10`, `HistoriaClinica` $\blacklozenge$--- `RecetaMedica`, `ComprobantePago` $\blacklozenge$--- `PagoVoucher`.
  - **Relaciones de Agregación:** `Especialista` $\diamond$--- `HorarioDisponibilidad`, `CitaMedica` $\diamond$--- `TeleconsultaSession`.
  - **Núcleo Transaccional:** `CitaMedica` vinculada con `Paciente`, `Especialista`, `PreTriajeClinico` y `ComprobantePago`.

---

## 3. Instrucciones de Navegación Interactiva
1. Haga doble clic en los archivos `.html` para abrirlos en cualquier navegador moderno.
2. Utilice la **rueda del ratón** para zoom continuo y **clic + arrastrar** para desplazamiento panorámico (*pan*).
3. **Zoom Semántico:**
   - En vista general o zoom reducido: Muestra de manera limpia los títulos de paquetes y entidades.
   - En zoom cercano ($\ge 1.18\times$) o haciendo **clic sobre cualquier tarjeta**: Se despliegan automáticamente los atributos, métodos, ilaciones asociadas y notas funcionales.
4. Presione el botón **"Render PNG 300-DPI"** en la barra superior para inspeccionar el render gráfico oficial de alta resolución.

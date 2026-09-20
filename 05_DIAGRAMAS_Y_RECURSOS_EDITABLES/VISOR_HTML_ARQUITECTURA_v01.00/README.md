# Visor Interactivo de Arquitectura de Software v01.00 (NexoVitalis360)

Este directorio contiene el portal interactivo y la suite completa de diagramas de arquitectura en formato HTML/SVG navegable con zoom semántico, renderizado B&W puro y esquinas 100% rectas (*sharp edges*).

## Estructura de Archivos

- **`index.html`**: Portal centralizador con barra lateral de navegación organizada por carpetas (según las 8 plantillas del curso de Diseño y Arquitectura de Software - UNSA).
- **`fig2_1_arquitectura_generica.html`**: Diagrama de Arquitectura Genérica en 5 capas desacopladas, API Gateway y servicios externos.
- **`fig7_1_contexto_modular_citas.html`**: Diagrama de Contexto Modular del Subsistema B4 (Gestión de Citas y Agendas).
- **`fig7_2_contexto_global_nivel0.html`**: Diagrama de Contexto Global Nivel 0 (NexoVitalis360 como Caja Negra).
- **`fig7_3_bloques_funcionales_nivel1.html`**: Diagrama de Bloques Funcionales Nivel 1 (11 bloques B1-B11 y 28 flujos correlativos F1-F28).
- **`fig7_4_maquina_estados_cita.html`**: Diagrama de Máquina de Estados del Ciclo de Vida de la Cita Médica (8 estados, guardas y 3 finales).
- **`fig7_5_secuencia_agendamiento.html`**: Diagrama de Secuencia de Arquitectura (Escenario de Agendamiento en 14 pasos a través de las 5 capas).

## Instrucciones de Uso Local

1. Abrir `index.html` en cualquier navegador web moderno (Google Chrome, Microsoft Edge, Mozilla Firefox).
2. Utilizar la barra lateral izquierda para explorar los diagramas organizados por plantilla.
3. En cada diagrama:
   - **Arrastre con clic izquierdo:** Desplazamiento panorámico (*Pan*).
   - **Rueda del ratón:** Acercar / Alejar (*Zoom* fluido centrado en el cursor).
   - **Clic en cualquier caja:** Centra y enfoca la caja revelando su detalle asistencial.
   - **Botón `Modo: AUTO / DETALLES`:** Alterna entre el modo macro (solo títulos) y el modo detallado.
   - **Tecla `0` o botón `Ajustar`:** Restablece la vista a pantalla completa.
   - **Tecla `M` o botón `◀ Ocultar Menú`:** Oculta la barra lateral para maximizar el lienzo del diagrama.

## Publicación en GitHub Pages (Opcional)

Este visor está optimizado para funcionar como sitio estático sin dependencias externas:
1. Activar GitHub Pages en el repositorio apuntando a la rama correspondiente.
2. Navegar a la URL pública de GitHub Pages para interactuar en línea.

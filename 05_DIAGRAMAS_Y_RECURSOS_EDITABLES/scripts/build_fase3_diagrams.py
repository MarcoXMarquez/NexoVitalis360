#!/usr/bin/env python3
"""
build_fase3_diagrams.py
Generador de diagramas vectoriales SVG, renders PNG a 300 DPI y suites interactivas HTML5
para la Fase 3 de NexoVitalis360 (Plantilla 6: Datos y Plantilla 7: GUIs).
Estilo: 100% Blanco y Negro Puro, Sharp Edges (0px radius), Tipografía Técnica.
"""

import os
import subprocess

def create_interactive_html(svg_content, title, width, height):
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | NexoVitalis360</title>
  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      border-radius: 0 !important;
    }}
    html, body {{
      width: 100vw;
      height: 100vh;
      overflow: hidden;
      background-color: #ffffff;
      color: #000000;
      font-family: Arial, "Helvetica Neue", Helvetica, sans-serif;
      user-select: none;
    }}
    .viewport {{
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      overflow: hidden;
      cursor: grab;
      background-color: #ffffff;
    }}
    .viewport:active {{
      cursor: grabbing;
    }}
    .canvas-world {{
      position: absolute;
      top: 0;
      left: 0;
      transform-origin: 0 0;
      background-color: #ffffff;
    }}
    .hud-bar {{
      position: fixed;
      top: 10px;
      right: 16px;
      z-index: 2000;
      display: flex;
      align-items: center;
      gap: 8px;
      background: #ffffff;
      border: 1.5px solid #000000;
      padding: 5px 12px;
      font-size: 11.5px;
      box-shadow: 2px 2px 0px #000000;
    }}
    .hud-status-badge {{
      background: #000000;
      color: #ffffff;
      font-size: 10px;
      font-weight: bold;
      padding: 3px 7px;
      text-transform: uppercase;
    }}
    .btn-hud {{
      background: #ffffff;
      color: #000000;
      border: 1.5px solid #000000;
      padding: 4px 10px;
      font-size: 11px;
      font-weight: bold;
      cursor: pointer;
    }}
    .btn-hud:hover {{
      background: #000000;
      color: #ffffff;
    }}
  </style>
</head>
<body>
  <div class="hud-bar">
    <span class="hud-status-badge">OFICIAL V01.00</span>
    <div style="font-weight:bold;">{title}</div>
    <button class="btn-hud" id="btn-fit">Ajustar Vista</button>
    <button class="btn-hud" id="btn-reset">Reset</button>
    <button class="btn-hud" id="btn-zoomin">+</button>
    <button class="btn-hud" id="btn-zoomout">-</button>
  </div>
  <div class="viewport" id="viewport">
    <div class="canvas-world" id="canvas-world">
      {svg_content}
    </div>
  </div>
  <script>
    const viewport = document.getElementById('viewport');
    const world = document.getElementById('canvas-world');
    let scale = 1, panX = 0, panY = 0;
    let isDragging = false, startX = 0, startY = 0;

    function updateTransform() {{
      world.style.transform = `translate(${{panX}}px, ${{panY}}px) scale(${{scale}})`;
    }}

    function fitView() {{
      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;
      const dw = {width};
      const dh = {height};
      scale = Math.min((vw - 60) / dw, (vh - 60) / dh, 1.0);
      panX = (vw - dw * scale) / 2;
      panY = (vh - dh * scale) / 2;
      updateTransform();
    }}

    viewport.addEventListener('mousedown', (e) => {{
      if (e.target.closest('.hud-bar')) return;
      isDragging = true;
      startX = e.clientX - panX;
      startY = e.clientY - panY;
    }});

    window.addEventListener('mousemove', (e) => {{
      if (!isDragging) return;
      panX = e.clientX - startX;
      panY = e.clientY - startY;
      updateTransform();
    }});

    window.addEventListener('mouseup', () => {{ isDragging = false; }});

    viewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.1 : 0.9;
      const mouseX = e.clientX;
      const mouseY = e.clientY;
      panX = mouseX - (mouseX - panX) * zoomFactor;
      panY = mouseY - (mouseY - panY) * zoomFactor;
      scale *= zoomFactor;
      scale = Math.max(0.2, Math.min(scale, 4.0));
      updateTransform();
    }}, {{ passive: false }});

    document.getElementById('btn-fit').onclick = fitView;
    document.getElementById('btn-reset').onclick = () => {{ scale = 1; panX = 40; panY = 60; updateTransform(); }};
    document.getElementById('btn-zoomin').onclick = () => {{ scale = Math.min(scale * 1.2, 4.0); updateTransform(); }};
    document.getElementById('btn-zoomout').onclick = () => {{ scale = Math.max(scale * 0.8, 0.2); updateTransform(); }};

    window.addEventListener('load', fitView);
    window.addEventListener('resize', fitView);
  </script>
</body>
</html>"""

print("Módulo cargado.")

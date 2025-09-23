# Animação embutida (GLB + USDZ)
1) Blender 3.6+ → Scripting → `scripts/blender_make_mars_system.py` → Run.
2) Exporta GLB com animações: File → Export → glTF 2.0 (GLB) → `models/mars_system.glb`.
3) Converte para iOS: Reality Converter → `models/mars_system.usdz` (ou `xcrun usdz_converter`).
4) Publica. Android usa GLB animado (Scene Viewer), iOS usa USDZ (Quick Look).

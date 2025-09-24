
# Planetas AR — Mars System Animado (GLB + USDZ)

Gere o `mars_system.glb` com animações embutidas (Marte a rodar ~60s; Fobos ~12s; Deimos ~20s) e converta para `mars_system.usdz`.

## GLB (Android / Scene Viewer)
1. Blender 3.6+ → Scripting → abrir `scripts/blender_make_mars_system.py` → **Run**.
2. File → Export → glTF 2.0 → **GLB** + **Animation** → guardar como `/models/mars_system.glb`.

## USDZ (iOS / Quick Look)
- Reality Converter: abrir `mars_system.glb` → Export → `mars_system.usdz`.
- Ou Terminal: `xcrun usdz_converter mars_system.glb mars_system.usdz`.

## No projeto
- `planets.json` aponta para `/models/mars_system_textured.glb` (placeholder detalhado) e `/models/mars_system.usdz` (quando tiver).
- Quando exportares o animado, podes trocar no `planets.json` para apontar para `/models/mars_system.glb`.


# Planetas AR — Animação (GLB + USDZ)

**Objetivo**: ter Marte e luas a mexer **em AR nativo** (Android/iOS).

## Android (Scene Viewer)
1. Blender 3.6+ → Scripting → `scripts/blender_make_mars_system.py` → Run.
2. File → Export → glTF 2.0 → **GLB Binary (.glb)** + **✓ Animation** → guarda como `models/mars_system.glb`.

## iOS (Quick Look)
- Reality Converter: abre `mars_system.glb` → Export → `mars_system.usdz`.
- Ou Terminal (Xcode): `xcrun usdz_converter mars_system.glb mars_system.usdz`.

Depois atualiza `planets.json` se quiseres apontar para o GLB animado:
```json
"marte": { "glb": "/models/mars_system.glb", "usdz": "/models/mars_system.usdz", ... }
```

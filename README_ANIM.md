
# Kit de Animação — Mars System (GLB + USDZ)

Este kit gera um `mars_system.glb` **com animação embutida** (Marte a rodar, Fobos e Deimos em órbita) para Android (incl. Scene Viewer). Depois converta para USDZ para iOS.

## Exportar GLB (Android / Scene Viewer)
1. Instale **Blender 3.6+**.
2. Blender → **Scripting** → crie um novo texto.
3. Cole o conteúdo de `scripts/blender_make_mars_system.py` → **Run**.
4. **File → Export → glTF 2.0 (.glb)**:
   - *Format*: **GLB Binary (.glb)**
   - *Include*: ✓ Animation, ✓ Apply Modifiers
   - *Transform*: +Y Up (padrão)
   - Guarde como `/models/mars_system.glb` no projeto.

## Exportar USDZ (iOS / Quick Look)
- **Reality Converter (macOS)**: abra `mars_system.glb` → Export → `mars_system.usdz`.
- **Linha de comando**: `xcrun usdz_converter mars_system.glb mars_system.usdz`.

## No projeto
- `planets.json` já aponta para `/models/mars_system.glb` e `/models/mars_system.usdz`.
- Depois de gerar os ficheiros, publique e teste:
  - Android: abre `?planet=marte` e toca **Ativar AR** (Scene Viewer).  
  - iOS (quando tiveres o USDZ): abre e toca **Ativar AR** (Quick Look).

## Performance
- Se precisar reduzir tamanho, baixe segmentos das esferas das luas e/ou texturas.

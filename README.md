
# Planetas AR — WebAR (Shopping Center)

Experiência de Realidade Aumentada ativada por QR Codes, sem app. Cada QR abre `index.html?planet=marte` (ou outro) e mostra o planeta correspondente em AR, com ficha de curiosidades.

## Estrutura
```
/assets            # imagens, logos (opcional)
/models            # coloque aqui os ficheiros .glb (Android/Web) e .usdz (iOS)
/scripts           # scripts custom (opcional)
index.html         # página única (usa ?planet=)
planets.json       # nomes, bullets, caminhos dos modelos
styles.css         # estilos
```
> Substitua os caminhos em `planets.json` pelos nomes reais dos seus modelos.

## Como publicar
1. Hospede a pasta num servidor estático com HTTPS (Cloudflare Pages, Netlify, Vercel, S3+CloudFront, etc.).
2. Garanta que a URL base é algo como `https://exemplo.com`.
3. Teste num iPhone (Safari) e num Android (Chrome).

## QR Codes
Crie um QR por planeta e por localização (para métricas). Exemplo de URLs:
- `https://exemplo.com/index.html?planet=marte&utm_source=qr_praca_marte`
- `https://exemplo.com/index.html?planet=jupiter&utm_source=qr_piso2_jupiter`
- `https://exemplo.com/index.html?planet=plutao&utm_source=qr_piso1_plutao`

Recomendações de impressão:
- Tamanho mínimo 3×3 cm (ideal 4–5 cm), margem branca, contraste alto.
- Vinil fosco, evitar superfícies refletoras.

## Modelos 3D
- Formatos: `.glb` (Android/Web) e `.usdz` (iOS). Um par por planeta.
- Orçamento de tamanho: 3–8 MB por planeta (máx. 20 MB).
- Dicas: use texturas 2K, normal maps, comprima com Draco/meshopt (GLB).

## Personalização
- Texto/curiosidades: edite `planets.json`.
- Identidade visual: o logo do shopping já está referenciado no `index.html` via link externo. Se preferir hospedar localmente, coloque `assets/logo.png` e troque o `src`.

## Fallback
Se o dispositivo não suportar AR, o `<model-viewer>` mostra o modelo 3D interativo no browser.

## Analytics
- Os parâmetros `utm_*` na URL podem ser usados no seu analytics (Google Analytics 4, etc.).
- Eventos sugeridos: page_view, ar_activate, snapshot, planet_id, location_id.

## Segurança e privacidade
- Evite recolher dados pessoais. Use apenas métricas anónimas.
- Adicione um link para Política de Privacidade se integrar analytics de terceiros.

## Suporte de dispositivos (resumo)
- Android (Chrome): WebXR / Scene Viewer (AR nativo)
- iOS (Safari): Quick Look via `ios-src` (USDZ)
- Desktop: apenas 3D no browser (sem AR)

## Problemas comuns
- AR não ativa no iOS: confirme que o ficheiro .usdz está acessível via HTTPS e com `ios-src` no `<model-viewer>`.
- Modelo gigante ou minúsculo: ajuste `scale` no `planets.json`.
- QR não lê: aumente o tamanho e contraste, ou simplifique a URL.

Bom evento!

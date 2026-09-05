# OpenRouter :free survival — playbook vendável

**Regen:** 2026-09-05 20:23 -03 · Receita Alpha · teto US$0 · só docs oficiais + smoke cost 0

## Fontes oficiais
- Docs: https://openrouter.ai/docs
- Pricing: https://openrouter.ai/pricing
- Limits (constantes no HTML oficial):
  - `FREE_MODEL_RATE_LIMIT_RPM=20`
  - `FREE_MODEL_NO_CREDITS_RPD=50`
  - `FREE_MODEL_HAS_CREDITS_RPD=1000`
  - `FREE_MODEL_CREDITS_THRESHOLD=10`

## Conta (sem secrets)
- `GET /api/v1/credits`: total_credits=0 · total_usage≈0.052
- Banda: purchased credits < 10 → **20 RPM / 50 RPD**
- UI saldo negativo (~−$0.05) → risco **402 mesmo em :free**
- Catálogo live: **19** IDs `*:free` · pricing prompt/completion **0** em todos

## Smoke desta regen (prova cost 0)
| Campo | Valor |
| --- | --- |
| Modelo | `dots-studio/dots-3-note-preview:free` |
| HTTP | 200 |
| usage.cost | **0** |
| Tokens | prompt 62 / completion 259 / total 321 |
| finish | stop |

Resposta (content):
> Use uma única API OpenRouter para acessar múltiplos modelos de IA.
> Teste gratuitamente com o modelo :free, sem necessidade de cartão, ideal para MVP.
> Troque entre modelos de IA diretamente pela API, sem precisar reescrever seu código.

Rodada anterior (18:50): `poolside/laguna-s-2.1:free` OK cost 0; `z-ai/glm-5.2:free` 429 one-shot; `thinkingmachines/inkling-small:free` 403 harness.

## Regras de sobrevivência
| Sintoma | Ação |
| --- | --- |
| cost > 0 | abortar já |
| 402 | parar API · pivot chat/apps web · sem top-up |
| 429 | 1 tentativa · trocar ID :free · sem loop |
| 200 + content null | reasoning comeu max_tokens · outro ID / subir max_tokens |
| 403 harness | sem retry (inkling*) |

## Catálogo :free (19)
`cohere/north-mini-code:free` · `dots-studio/dots-3-note-preview:free` · `google/gemma-4-26b-a4b-it:free` · `google/gemma-4-31b-it:free` · `inclusionai/ling-3.0-flash-fin:free` · `inclusionai/ling-3.0-flash-sante:free` · `liquid/lfm-2.5-2.6b:free` · `minimax/minimax-m2.7:free` · `minimax/minimax-m3:free` · `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` · `nvidia/nemotron-3-super-120b-a12b:free` · `nvidia/nemotron-3-ultra-550b-a55b:free` · `nvidia/nemotron-3.5-content-safety:free` · `nvidia/nemotron-3.5-lightning:free` · `poolside/laguna-s-2.1:free` · `poolside/laguna-xs-2.1:free` · `thinkingmachines/inkling-small:free` · `thinkingmachines/inkling:free` · `z-ai/glm-5.2:free`

## Mini-curso (5 aulas)
1. Cotas oficiais (20 RPM / 50 vs 1000 RPD)
2. Smoke 2 IDs :free (provar cost 0)
3. Playbook 402 / 429 / content-null
4. Roteamento entre IDs free
5. PIX por valor EMV (nunca índice qr_0)

## Preços PIX LUIZ (por valor EMV)
- **R$20** — ebook + smoke → `pix_r20` / `qr_r20.png` (tag54=20.00)
- **R$50** — curso + script → `pix_r50` / `qr_r50.png` (tag54=50.00)
- **NUNCA** pagar `qr_0` (EMV = R$100)

### Copia-cola R$20
```
00020126330014br.gov.bcb.pix011108030362994520400005303986540520.005802BR5920LUIZ GUSTAVO CORREIA6009SAO PAULO62100506padrao63043835
```

### Copia-cola R$50
```
00020126330014br.gov.bcb.pix011108030362994520400005303986540550.005802BR5920LUIZ GUSTAVO CORREIA6009SAO PAULO62080504Pack63044E58
```

## Links
- Landing: https://ziuluiziul.github.io/openrouter-free-oferta/
- Curso: https://ziuluiziul.github.io/openrouter-free-oferta/curso.html
- Space: https://huggingface.co/spaces/Ziulluizziul/openrouter-free-oferta
- HUB: https://ziuluiziul.github.io/round1-cumulunimbus/

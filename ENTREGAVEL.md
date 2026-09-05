# OpenRouter free-tier — smoke + cotas oficiais (ROUND1)

**Data:** 2026-09-05 11:20 -03  
**Provedor:** OpenRouter (docs oficiais apenas)  
**Modo:** API `:free` only · teto US$0 · sem top-up  

## 1. Conta / cotas (sem secrets)

| Item | Valor | Fonte |
| --- | --- | --- |
| `total_credits` | 0 | GET `/api/v1/credits` |
| `total_usage` | ≈ 0.052 | GET `/api/v1/credits` |
| UI Credits | −$0.05 | settings/credits |
| Banda free models | **20 RPM / 50 RPD** (lifetime purchased credits &lt; 10) | docs Limits: `FREE_MODEL_RATE_LIMIT_RPM=20`, `FREE_MODEL_NO_CREDITS_RPD=50`, `FREE_MODEL_CREDITS_THRESHOLD=10` |
| Após ≥ US$10 créditos | 20 RPM / **1000 RPD** | mesma docs |
| Risco 402 | saldo negativo pode 402 mesmo em `:free` | docs Limits |

## 2. Catálogo live `:free` (snapshot)

**Count:** 19 modelos com id terminando em `:free` via GET `/api/v1/models`.

Arquivo: `models-free-snapshot.json`

IDs:
- `cohere/north-mini-code:free`
- `dots-studio/dots-3-note-preview:free`
- `google/gemma-4-26b-a4b-it:free`
- `google/gemma-4-31b-it:free`
- `inclusionai/ling-3.0-flash-fin:free`
- `inclusionai/ling-3.0-flash-sante:free`
- `liquid/lfm-2.5-2.6b:free`
- `minimax/minimax-m2.7:free`
- `minimax/minimax-m3:free`
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- `nvidia/nemotron-3-super-120b-a12b:free`
- `nvidia/nemotron-3-ultra-550b-a55b:free`
- `nvidia/nemotron-3.5-content-safety:free`
- `nvidia/nemotron-3.5-lightning:free`
- `poolside/laguna-s-2.1:free`
- `poolside/laguna-xs-2.1:free`
- `thinkingmachines/inkling-small:free`
- `thinkingmachines/inkling:free`
- `z-ai/glm-5.2:free`

## 3. Smoke inference (prova ROUND1)

| Campo | Valor |
| --- | --- |
| Modelo | `inclusionai/ling-3.0-flash-sante:free` |
| HTTP | 200 |
| `usage.cost` | **0** (deve ser 0) |
| Tokens | prompt 37 / completion 200 / total 237 |
| Reasoning tokens | 99 |
| finish_reason | stop |

### Resposta do modelo (conteúdo)

- **Roteamento unificado:** uma única API endpoint para chamar múltiplos modelos (OpenAI, Anthropic, open-source) com fallback automático e load balancing.
- **Gestão centralizada:** autenticação, cotas, logging e auditoria em um só lugar, simplificando compliance e custos.
- **Abstração de provedores:** troca de modelo ou vendor sem reescrever código, via prompt padronizado e schema de resposta consistente.

### Notas operacionais
- Tentativas anteriores: `poolside/laguna-xs-2.1:free` → **429** upstream shared pool; `cohere/north-mini-code:free` e `inclusionai/ling-3.0-flash-fin:free` → 200 cost 0 mas **content vazio** (reasoning consumiu `max_tokens`).
- Preferir IDs que devolvam `content` não-nulo; tratar content-null como falha de entrega.
- Se **402** / saldo negativo bloquear → pivot **chat/apps web** OpenRouter; sem top-up.

## 4. Fontes oficiais
- https://openrouter.ai/docs  
- https://openrouter.ai/pricing  
- Limits (constantes free RPD/RPM/threshold 10)  
- https://openrouter.ai/blog/announcements/simplifying-our-platform-fee/ (fee 5.5% mín US$0.80)

## 5. Meta missão (ledger)
Pay-as-you-go: **US$ 10** créditos + fee ~**US$ 0.80** → meta **US$ 10.80**. Acumulado BRL/USD: **0**. USD/Binance: pending Luiz.

# OpenRouter :free — routing cheatsheet

_Live 2026-09-05 18:51 -03 · 19 modelos `:free`_

## Rotação desta rodada

- `thinkingmachines/inkling-small:free` → HTTP 403 agentic-harness only · one-shot
- `z-ai/glm-5.2:free` → HTTP 429 upstream · one-shot sem loop
- `poolside/laguna-s-2.1:free` → OK · cost 0
- `minimax/minimax-m2.7:free` → não chamado (já tinha content OK)

## Quando usar o quê (ângulo venda)

- `poolside/laguna-s-2.1:free` / `laguna-xs-2.1:free` — coding agent; copy/demo estável nesta rodada.
- `dots-studio/dots-3-note-preview:free` — notas/docs/copy curto; bom para demos de texto.
- `nvidia/nemotron-3.5-lightning:free` — throughput agentic / tarefas especializadas.
- `inclusionai/ling-3.0-flash-sante:free` — saúde/medicina (MoE); se content null, subir `max_tokens` (reasoning consome budget).
- `inclusionai/ling-3.0-flash-fin:free` — finanças/investimentos.
- `cohere/north-mini-code:free` — code snippets leves.
- `google/gemma-4-*:free` — geral; pode 429 sob carga (1 shot, sem loop).
- `thinkingmachines/inkling*:free` — só harness agentic (apps listados); API chat direta → 403.
- `z-ai/glm-5.2:free` — pode 429 no pool compartilhado upstream.

## Guardrails

- Só `:free` / pricing 0. Abortar se `usage.cost>0` ou HTTP 402. Sem top-up.
- Free-tier com créditos <10 → ~20 RPM / ~50 RPD (docs oficiais). Não martelar todos os modelos.
- Endpoint: `POST https://openrouter.ai/api/v1/chat/completions`

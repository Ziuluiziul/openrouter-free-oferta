# OpenRouter :free — routing cheatsheet

_Live 2026-09-05 16:46 -03 · 19 modelos `:free`_

## Rotação desta rodada

- `inclusionai/ling-3.0-flash-sante:free` → null-content · cost 0
- `dots-studio/dots-3-note-preview:free` → OK · cost 0
- `nvidia/nemotron-3.5-lightning:free` → OK · cost 0

## Quando usar o quê (ângulo venda)

- `inclusionai/ling-3.0-flash-sante:free` — saúde/medicina (MoE); se content null, subir `max_tokens` (reasoning consome budget).
- `dots-studio/dots-3-note-preview:free` — notas/docs/copy curto; bom para demos de texto.
- `nvidia/nemotron-3.5-lightning:free` — throughput agentic / tarefas especializadas.
- `inclusionai/ling-3.0-flash-fin:free` — finanças/investimentos.
- `cohere/north-mini-code:free` — code snippets leves.
- `google/gemma-4-*:free` — geral; pode 429 sob carga (1 shot, sem loop).
- `poolside/laguna-s-2.1:free` / `laguna-xs-2.1:free` — coding agent.

## Guardrails

- Só `:free` / pricing 0. Abortar se `usage.cost>0` ou HTTP 402. Sem top-up.
- Free-tier com créditos <10 → ~20 RPM / ~50 RPD (docs oficiais). Não martelar todos os modelos.
- Endpoint: `POST https://openrouter.ai/api/v1/chat/completions`


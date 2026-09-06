# OpenRouter :free — routing cheatsheet

_Live 2026-09-05 22:47 -03 · 19 modelos `:free`_

## Rotação desta rodada

- `liquid/lfm-2.5-2.6b:free` → OK · cost 0 · copy vendável (1 chamada útil)

## Quando usar o quê (ângulo venda)

- `liquid/lfm-2.5-2.6b:free` — leve/geral; OK nesta rodada (copy curto).
- `minimax/minimax-m3:free` / `minimax/minimax-m2.7:free` — geral/copy.
- `poolside/laguna-s-2.1:free` / `poolside/laguna-xs-2.1:free` — coding agent; copy/demo estável.
- `dots-studio/dots-3-note-preview:free` — notas/docs/copy curto; bom para demos de texto.
- `nvidia/nemotron-3.5-lightning:free` — throughput agentic / tarefas especializadas.
- `inclusionai/ling-3.0-flash-sante:free` — saúde/medicina (MoE); se content null, subir `max_tokens` (reasoning consome budget).
- `inclusionai/ling-3.0-flash-fin:free` — finanças/investimentos.
- `cohere/north-mini-code:free` — code snippets leves; pode gastar budget em reasoning (content null).
- `google/gemma-4-*:free` — geral; pode 429 sob carga (1 shot, sem loop).
- `thinkingmachines/inkling*:free` — só harness agentic (apps listados); API chat direta → 403.
- `z-ai/glm-5.2:free` — pode 429 no pool compartilhado upstream.

## Guardrails

- Só `:free` / pricing 0. Abortar se `usage.cost>0` ou HTTP 402. Sem top-up.
- Free-tier com créditos <10 → ~20 RPM / ~50 RPD (docs oficiais). Não martelar todos os modelos.
- Endpoint: `POST https://openrouter.ai/api/v1/chat/completions`

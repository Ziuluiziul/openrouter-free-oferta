# Cheat-sheet roteamento :free (amostra produto)
Snapshot: 2026-09-05 11:43 -03 · 19 modelos

Use `openrouter/free` ou IDs abaixo. Preferir quem devolve `content` não-nulo; 429 upstream = trocar ID.

- `cohere/north-mini-code:free` · ctx 256000
- `dots-studio/dots-3-note-preview:free` · ctx 512000
- `google/gemma-4-26b-a4b-it:free` · ctx 262144
- `google/gemma-4-31b-it:free` · ctx 262144
- `inclusionai/ling-3.0-flash-fin:free` · ctx 262144
- `inclusionai/ling-3.0-flash-sante:free` · ctx 262144
- `liquid/lfm-2.5-2.6b:free` · ctx 65536
- `minimax/minimax-m2.7:free` · ctx 196608
- `minimax/minimax-m3:free` · ctx 1048576
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` · ctx 256000
- `nvidia/nemotron-3-super-120b-a12b:free` · ctx 262144
- `nvidia/nemotron-3-ultra-550b-a55b:free` · ctx 1000000
- `nvidia/nemotron-3.5-content-safety:free` · ctx 128000
- `nvidia/nemotron-3.5-lightning:free` · ctx 1000000
- `poolside/laguna-s-2.1:free` · ctx 262144
- `poolside/laguna-xs-2.1:free` · ctx 262144
- `thinkingmachines/inkling-small:free` · ctx 1048576
- `thinkingmachines/inkling:free` · ctx 1048576
- `z-ai/glm-5.2:free` · ctx 256000

## Heurística prática
- Smoke/copy curto: `inclusionai/ling-3.0-flash-sante:free` (provado cost 0 + content)
- Evitar retries em loop em 429 (Poolside etc.) — queima RPD
- Saldo negativo → risco 402 → chat web

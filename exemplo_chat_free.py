#!/usr/bin/env python3
"""Exemplo mínimo OpenRouter :free — key via env OPENROUTER_API_KEY (nunca no chat)."""
import json, os, urllib.request

API = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "inclusionai/ling-3.0-flash-sante:free"  # ajustar se o catálogo mudar

def main():
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        raise SystemExit("Defina OPENROUTER_API_KEY no ambiente")
    body = {
        "model": MODEL,
        "messages": [{"role": "user", "content": "3 bullets curtos em PT sobre gateway LLM."}],
        "max_tokens": 512,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        API,
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/Ziuluiziul/A.N.E",
            "X-Title": "A.N.E",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read().decode())
    msg = data["choices"][0]["message"]
    print("cost:", (data.get("usage") or {}).get("cost"))
    print(msg.get("content") or "(content vazio — tente outro :free)")

if __name__ == "__main__":
    main()

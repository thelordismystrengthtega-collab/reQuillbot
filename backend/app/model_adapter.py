import os
import httpx
import asyncio
from typing import Optional

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
PROVIDER_URL = os.getenv("PROVIDER_URL")  # optional custom provider

async def paraphrase_via_openai(text: str, mode: str = "fluency", length: Optional[str] = None) -> str:
    """
    Basic adapter calling an OpenAI-compatible chat completions endpoint.
    Switches to PROVIDER_URL if provided; otherwise uses api.openai.com.
    """
    system_message = (
        "You are a high-quality paraphrasing assistant. Preserve the original meaning exactly, "
        "avoid adding facts, and produce output according to the requested mode. "
        "Respond only with the rewritten text (no commentary)."
    )

    # Add a short instruction based on mode/length
    user_instructions = f"Paraphrase this text. Mode: {mode}."
    if length:
        user_instructions += f" Target length: {length}."

    user_instructions += f"\n\nText:\n\"\"\"\n{text}\n\"\"\"\n"

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_instructions}
        ],
        "temperature": 0.7,
        "max_tokens": 1024
    }

    headers = {"Content-Type": "application/json"}
    if OPENAI_API_KEY:
        headers["Authorization"] = f"Bearer {OPENAI_API_KEY}"

    url = PROVIDER_URL or "https://api.openai.com/v1/chat/completions"

    async with httpx.AsyncClient(timeout=30.0) as client:
        resp = await client.post(url, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    # OpenAI-style response parsing
    try:
        return data["choices"][0]["message"]["content"].strip()
    except Exception:
        # fallback if provider returns slightly different envelope
        return data.get("output_text") or data.get("text") or ""

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import ParaphraseRequest, ParaphraseResponse
from .model_adapter import paraphrase_via_openai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Paraphrase MVP")

# Allow frontend dev server and docker-compose default network
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/api/paraphrase", response_model=ParaphraseResponse)
async def paraphrase(req: ParaphraseRequest):
    if not req.text or req.text.strip() == "":
        raise HTTPException(status_code=400, detail="text is required")

    try:
        out = await paraphrase_via_openai(req.text, mode=req.mode or "fluency", length=req.length)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    return ParaphraseResponse(original=req.text, paraphrase=out, mode=req.mode or "fluency")

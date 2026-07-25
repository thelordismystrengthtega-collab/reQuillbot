from pydantic import BaseModel
from typing import Optional

class ParaphraseRequest(BaseModel):
    text: str
    mode: Optional[str] = "fluency"   # e.g., "fluency", "formal", "concise", "creative"
    length: Optional[str] = None      # "short", "medium", "long"

class ParaphraseResponse(BaseModel):
    original: str
    paraphrase: str
    mode: str

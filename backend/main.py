from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="reQuillbot API",
    description="AI-powered writing assistant API",
    version="0.1.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AnalysisRequest(BaseModel):
    text: str


class AnalysisResponse(BaseModel):
    text: str
    word_count: int
    char_count: int
    readability_score: float
    suggestions: list


@app.get("/")
async def root():
    return {
        "message": "Welcome to reQuillbot API",
        "version": "0.1.0"
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """
    Analyze the provided text and return writing suggestions.
    """
    text = request.text
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    
    # Placeholder for readability score calculation
    readability_score = 0.85
    
    # Placeholder suggestions
    suggestions = [
        "Consider breaking long sentences into shorter ones",
        "Good use of varied vocabulary",
        "Check for passive voice usage"
    ]
    
    return AnalysisResponse(
        text=text,
        word_count=word_count,
        char_count=char_count,
        readability_score=readability_score,
        suggestions=suggestions
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

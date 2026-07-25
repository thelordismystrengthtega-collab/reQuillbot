# Paraphrase MVP (React + FastAPI)

What this is
- Minimal paraphrase/rewrite MVP:
  - FastAPI backend with /api/paraphrase endpoint that calls an OpenAI-compatible API.
  - React + TypeScript frontend (Vite) with a simple UI to submit text and select paraphrase mode.
  - Dockerfiles + docker-compose for local development.

Quick start (Docker)
1. Copy files into a project directory preserving the paths in the repo layout.
2. Create backend/.env from the example and set your API key:
   - Copy backend/.env.example -> backend/.env
   - Edit backend/.env and set OPENAI_API_KEY
3. Build and run:
   - docker-compose up --build
4. Open frontend at http://localhost:5173 and try it.

Local (without docker)
- Backend:
  - cd backend
  - python -m venv .venv && source .venv/bin/activate
  - pip install -r requirements.txt
  - export OPENAI_API_KEY=...
  - uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
- Frontend:
  - cd frontend
  - npm install
  - npm run dev -- --host

Environment
- backend/.env:
  - OPENAI_API_KEY (required for hosted-provider mode)
  - MODEL_NAME (optional, default: gpt-3.5-turbo)
  - PROVIDER_URL (optional, leave blank to use OpenAI)

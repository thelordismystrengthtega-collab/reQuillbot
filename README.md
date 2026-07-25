# reQuillbot MVP Scaffold

AI-powered writing assistant with React frontend and FastAPI backend.

## Project Structure

```
.
├── frontend/              # React application
│   ├── public/           # Static files
│   ├── src/              # React components and logic
│   ├── Dockerfile        # Frontend container
│   └── package.json      # Frontend dependencies
├── backend/              # FastAPI application
│   ├── main.py          # Main application file
│   ├── Dockerfile       # Backend container
│   └── requirements.txt  # Python dependencies
├── docker-compose.yml    # Multi-container setup
└── README.md            # This file
```

## Quick Start

### Using Docker Compose (Recommended)

1. Ensure Docker and Docker Compose are installed
2. From the project root, run:

```bash
docker-compose up --build
```

3. Access the application:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Manual Setup

#### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`

#### Frontend

```bash
cd frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000`

## API Endpoints

- `GET /` - Welcome message
- `GET /health` - Health check
- `POST /api/analyze` - Analyze text content

### Example Request

```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text here"}'
```

## Development

### Backend Development

- API documentation available at `http://localhost:8000/docs`
- Use hot reload in development mode
- Add new endpoints in `backend/main.py`

### Frontend Development

- Components are located in `frontend/src/components/`
- Add new pages in `frontend/src/pages/`
- Styling uses CSS modules and inline styles

## Next Steps

- [ ] Implement text analysis algorithms
- [ ] Add user authentication
- [ ] Set up database (PostgreSQL)
- [ ] Implement caching
- [ ] Add comprehensive error handling
- [ ] Create unit tests
- [ ] Set up CI/CD pipeline
- [ ] Deploy to production

## Technologies

- **Frontend**: React 18, CSS3
- **Backend**: FastAPI, Uvicorn
- **Containerization**: Docker, Docker Compose
- **Package Management**: npm (frontend), pip (backend)

## License

MIT

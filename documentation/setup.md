# Setup

## Local backend run
1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Start Ollama and pull a llama model:
   ```bash
   ollama serve
   ollama pull llama3.1
   ```
4. (Optional) override model/runtime settings:
   ```bash
   set OLLAMA_BASE_URL=http://127.0.0.1:11434
   set OLLAMA_MODEL=llama3.1
   set OLLAMA_TIMEOUT_SECONDS=60
   ```
5. Run API:
   ```bash
   uvicorn backend.main:app --reload
   ```
6. Check health endpoint:
   ```bash
   curl http://127.0.0.1:8000/api/v1/health
   ```
5. Verify chat uses Ollama:
   ```bash
   curl -X POST http://127.0.0.1:8000/api/v1/chat -H "Content-Type: application/json" -d "{\"message\":\"hello\"}"
   ```

## Local frontend run
1. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the UI:
   ```bash
   npm run dev
   ```
3. Open the Vite URL shown in the terminal.

## Docker development
```bash
cd docker
docker compose up --build
```

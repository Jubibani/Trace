# Setup

## Local backend run
1. Create a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r backend/requirements.txt
   ```
3. Run API:
   ```bash
   uvicorn backend.main:app --reload
   ```
4. Check health endpoint:
   ```bash
   curl http://127.0.0.1:8000/api/v1/health
   ```

## Docker development
```bash
cd docker
docker compose up --build
```

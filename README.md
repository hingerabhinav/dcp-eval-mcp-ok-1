# dcp-eval-mcp-ok-1

Python 3.11 microservice owned by **harness**, scaffolded by the DCP Golden Path.

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Health check endpoint: `GET /healthz`

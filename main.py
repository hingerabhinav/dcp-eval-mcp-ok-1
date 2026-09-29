from fastapi import FastAPI

app = FastAPI(title="dcp-eval-mcp-ok-1")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "dcp-eval-mcp-ok-1", "owner": "harness"}

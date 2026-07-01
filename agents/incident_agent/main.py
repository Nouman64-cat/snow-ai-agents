from fastapi import FastAPI

app = FastAPI(title="Incident Agent")


@app.get("/health")
def health():
    return {"status": "ok"}

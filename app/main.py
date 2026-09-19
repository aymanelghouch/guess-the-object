from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes import prediction

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"

app = FastAPI(
    title="GuessTheObject AI",
    description="Sube una imagen y un Vision Transformer intenta identificar el objeto.",
    version="0.1.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(prediction.router)

app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
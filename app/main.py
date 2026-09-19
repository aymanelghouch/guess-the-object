from fastapi import FastAPI

from app.routes import prediction

app = FastAPI(
    title="AI Guess",
    description="Sube una imagen y una vision Transformer intenta identificar el objeto",

    version="0.1.0",
)

@app.get("/health")
def health():
   return {
    "status": "ok",
   }

app.include_router(prediction.router)
import io

from fastapi import APIRouter, UploadFile, File, HTTPException
from PIL import Image, UnidentifiedImageError, ImageOps




from app.model import predict
from app.schemas import PredictionResponse

router = APIRouter()


@router.post("/predict", response_model=PredictionResponse)
def predict_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El Arcivo debe ser una imagen")

    data = file.file.read()

    try:
        image = Image.open(io.BytesIO(data))
        image = ImageOps.exif_transpose(image).convert("RGB")
        
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="No se pudo leer la imagen.")



    return {"predictions": predict(image)}





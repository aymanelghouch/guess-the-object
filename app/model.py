import torch
from PIL import Image
from transformers import ViTForImageClassification, ViTImageProcessor

MODEL_NAME = "google/vit-base-patch16-224"

processor = ViTImageProcessor.from_pretrained(MODEL_NAME)
model = ViTForImageClassification.from_pretrained(MODEL_NAME)
model.eval()

def predict(image: Image.Image, top_k: int = 5) -> list[dict]:
    inputs = processor(images=image, return_tensors="pt")

    with torch.no_grad():
        logits = model(**inputs).logits

    probs = torch.softmax(logits, dim=-1)
    
    top_probs, top_ids = torch.topk(probs, k=top_k)

    return [
        {"label": model.config.id2label[i.item()], "confidence": p.item()}
        for p, i in zip(top_probs[0], top_ids[0])
    ]

    
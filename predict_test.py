import torch
from PIL import Image

from transformers import ViTForImageClassification, ViTImageProcessor

MODEL_NAME = "google/vit-base-patch16-224"
IMAGE_PATH = "image_text.jpg"

processor = ViTImageProcessor.from_pretrained(MODEL_NAME)
model = ViTForImageClassification.from_pretrained(MODEL_NAME)
model.eval()

image = Image.open(IMAGE_PATH).convert("RGB")

inputs = processor(images=image, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

logits = outputs.logits
print("Forma de los logits", logits.shape)

probs = torch.softmax(logits, dim=-1)
top_probs, top_ids = torch.topk(probs, k=5)

print("\nTop 5:")
for p, i in zip(top_probs[0], top_ids[0]):
    print(f"  {model.config.id2label[i.item()]:40s} {p.item():.2%}")
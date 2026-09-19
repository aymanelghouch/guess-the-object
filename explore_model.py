from transformers import ViTForImageClassification, ViTImageProcessor

MODEL_NAME = "google/vit-base-patch16-224"

processor = ViTImageProcessor.from_pretrained(MODEL_NAME)
model = ViTForImageClassification.from_pretrained(MODEL_NAME)
model.eval()


n_params = sum(p.numel() for p in model.parameters())

n_params = sum(p.numel() for p in model.parameters())
print(f"Parámetros: {n_params:,}")
print(f"Número de clases: {len(model.config.id2label)}")
print(f"Tamaño de entrada: {processor.size}")
print(f"Media de normalización: {processor.image_mean}")
print(f"Desviación de normalización: {processor.image_std}")

print("\nAlgunas clases:")
for i in (0, 1, 207, 817):
    print(f"  {i}: {model.config.id2label[i]}")
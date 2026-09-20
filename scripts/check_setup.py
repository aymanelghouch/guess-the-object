import torch
import transformers
import PIL
import fastapi

print("torch:", torch.__version__)
print("transformers:", transformers.__version__)
print("pillow:", PIL.__version__)
print("fastapi:", fastapi.__version__)

x = torch.tensor([1.0, 2.0, 3.0])
print("tensor de prueba:", x * 2)
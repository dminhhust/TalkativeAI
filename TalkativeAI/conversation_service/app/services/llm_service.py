from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from app.config import *

print("Loading LLM model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float32
)

model.eval()

print("Model loaded.")


def generate_response(prompt):

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        temperature=0.7
    )

    response = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return response

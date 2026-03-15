from transformers import AutoTokenizer, AutoModelForCausalLM

model = "microsoft/phi-3-mini-4k-instruct"

AutoTokenizer.from_pretrained(model)
AutoModelForCausalLM.from_pretrained(model)

print("Model downloaded.")

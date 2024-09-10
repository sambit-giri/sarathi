from transformers import AutoTokenizer, AutoModelForCausalLM

# Replace 'mistral-model-name' with the actual model name from the Hugging Face model hub
model_name = 'mistral-model-name'

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load the model
model = AutoModelForCausalLM.from_pretrained(model_name)

# Example input text
input_text = "Once upon a time"

# Tokenize the input text
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate text
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode the generated text
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)

from transformers import GPT2Tokenizer, GPT2Model
from transformers import pipeline, set_seed


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generation_text= generator("Hi my name is", max_length=10, num_return_sequences=5)

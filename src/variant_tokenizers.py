import os
from huggingface_hub import login
from transformers import AutoTokenizer

HF_TOKEN = os.getenv('HF_TOKEN')
login(HF_TOKEN, add_to_git_credential=True)

tokenizer = AutoTokenizer.from_pretrained('meta-llama/Meta-Llama-3.1-8B-Instruct', trust_remote_code=True)
messages = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Tell a light-heated joke for a room of Data Scientists"}
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
#print(prompt)

PHI3_MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
QWEN2_MODEL_NAME = "Qwen/Qwen2-7B-Instruct"
STARCODER2_MODEL_NAME = "bigcode/starcoder2-3b"

phi3_tokenizer = AutoTokenizer.from_pretrained(PHI3_MODEL_NAME)
text = "I am excited to show Tokenizers in action to my LLM engineers"
# print(tokenizer.encode(text))
# print()
tokens = phi3_tokenizer.encode(text)
# print(phi3_tokenizer.batch_decode(tokens))

# print(tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))
# print()
# print(phi3_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))

qwen2_tokenizer = AutoTokenizer.from_pretrained(QWEN2_MODEL_NAME)
# print(tokenizer.encode(text))
# print()
# print(phi3_tokenizer.encode(text))
# print()
# print(qwen2_tokenizer.encode(text))

# print(tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))
# print()
# print(phi3_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))
# print()
# print(qwen2_tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True))

starcoder2_tokenizer = AutoTokenizer.from_pretrained(STARCODER2_MODEL_NAME, trust_remote_code=True)
code = """
def hello_world(person):
  print("Hello", person)
"""
tokens = starcoder2_tokenizer.encode(code)
for token in tokens:
  print(f"{token}={starcoder2_tokenizer.decode(token)}")
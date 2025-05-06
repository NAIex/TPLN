import requests

url = "https://ai-qa-tpln.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2023-12-01"

headers = {
    "Content-Type": "application/json",
    "api-key": "FGPKhsolNFibhawfeZJHo4V0fzMSSoOE1krJgaARLmTdZB10RD2JJQQJ99BEACYeBjFXJ3w3AAAAACOGFu9p"
}

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)
print(response.json())


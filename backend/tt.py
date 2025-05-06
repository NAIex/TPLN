import requests
import json

# Replace with your actual values
api_key = "FGPKhsolNFibhawfeZJHo4V0fzMSSoOE1krJgaARLmTdZB10RD2JJQQJ99BEACYeBjFXJ3w3AAAAACOGFu9p"
endpoint = "https://ai-qa-tpln.openai.azure.com/"
deployment_name = "gpt-4o-mini-2024-07-18"
api_version = "2024-02-15-preview"

url = f"{endpoint}openai/deployments/{deployment_name}/chat/completions?api-version={api_version}"

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a fun fact about space."}
    ],
    "temperature": 0.7,
    "max_tokens": 100
}

response = requests.post(url, headers=headers, json=data)
print(response.json())

import requests

url = "https://ai-qa-tpln.openai.azure.com/openai/models?api-version=2024-10-21"

headers = {
    "Content-Type": "application/json",
    "api-key": "FGPKhsolNFibhawfeZJHo4V0fzMSSoOE1krJgaARLmTdZB10RD2JJQQJ99BEACYeBjFXJ3w3AAAAACOGFu9p"
}


response = requests.get(url, headers=headers)
print(response.json())



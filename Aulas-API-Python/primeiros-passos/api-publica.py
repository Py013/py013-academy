# Importando bibliotecas
import requests
import json

perfil_github = "luanfelixcoding" # Coloque o nome do seu perfil do github para acessar suas informações

URL = f"https://api.github.com/users/{perfil_github}" #? ENDPOINT com PATH PARAMETER como o perfil_github
response = requests.get(URL) #? Response através da API URL
print(f"HEADERS NÃO FORMATADO\n{response.headers}") #? Printando os Headers do Response que nos retornou

print() # Separar linha

#* Headers Formatado
print("HEADERS FORMATADO")
for key, value in response.headers.items():
    print(f"{key} : {value}")
    
print() # Separar linha

#* Json
response_json = response.json()
print(f"JSON NÃO FORMATADO\n{response_json}")

print() # Separar linha

#* Json Formatado
print(f"JSON FORMATADO\n{json.dumps(response_json, indent=5, ensure_ascii=False)}")

#* Pegando informação específica do json
print(f"URL: {response_json["url"]}")
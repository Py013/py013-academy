import json

#* Python dict para string JSON (Serialização)
dados = {'nome': 'Maria', 'cidade': 'São Paulo'}
json_string = json.dumps(dados, indent=2) # indent para formatação
print(f"String JSON: {json_string}")

#* String JSON para Python dict (Desserialização)
json_data_string = '{"id": 1, "produto": "Notebook"}'
dicionario_objeto = json.loads(json_data_string)
print(f"Dicionário Python: {dicionario_objeto}")
print(f"Produto: {dicionario_objeto['produto']}")
from src.depotActions import *
import json

# Abre os arquivos JSON
with open("scripts/blueDjinn.json") as file:
    blueData = json.load(file)
with open("scripts/greenDjinn.json") as file:
    greenData = json.load(file)

# Obtém a lista de itens de cada um dos djinns
blueItens = blueData['itens']
greenItens = greenData['itens']

# Itera sobre cada item
print("Blue Djinn")
for item in blueItens:
    nome = item['nome']
    valor = item['valor']
    print(f"Item: {nome}, Valor: {valor}")
print("\n")

print("Green Djinn")
for item in greenItens:
    nome = item['nome']
    valor = item['valor']
    print(f"Item: {nome}, Valor: {valor}")



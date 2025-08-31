import json

def ler_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def escrever_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# Exemplo de uso:
# escrever_json('exemplo.json', {'nome': 'Ana', 'idade': 30})
# print(ler_json('exemplo.json'))

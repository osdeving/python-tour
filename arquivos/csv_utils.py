import csv

def ler_csv(caminho):
    with open(caminho, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

def escrever_csv(caminho, linhas):
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(linhas)

# Exemplo de uso:
# escrever_csv('exemplo.csv', [['nome', 'idade'], ['Ana', 30]])
# print(ler_csv('exemplo.csv'))

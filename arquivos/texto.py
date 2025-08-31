def ler_arquivo_texto(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return f.read()

def escrever_arquivo_texto(caminho, conteudo):
    with open(caminho, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Exemplo de uso:
# escrever_arquivo_texto('exemplo.txt', 'Olá, mundo!')
# print(ler_arquivo_texto('exemplo.txt'))

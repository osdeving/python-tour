def abrir_arquivo(caminho, modo='r'):
    return open(caminho, modo, encoding='utf-8')

def exemplo_leitura(caminho):
    with abrir_arquivo(caminho, 'r') as f:
        return f.read()

def exemplo_escrita(caminho, conteudo):
    with abrir_arquivo(caminho, 'w') as f:
        f.write(conteudo)

def exemplo_binario(caminho, dados):
    with open(caminho, 'wb') as f:
        f.write(dados)

# Exemplos:
# exemplo_escrita('exemplo.txt', 'Olá, mundo!')
# print(exemplo_leitura('exemplo.txt'))
# exemplo_binario('exemplo.bin', b'\x00\x01')

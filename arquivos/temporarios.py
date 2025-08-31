import tempfile
import os

# Arquivo temporário
def exemplo_arquivo_temp():
    with tempfile.NamedTemporaryFile('w+', delete=False) as tmp:
        tmp.write('Conteúdo temporário')
        tmp.seek(0)
        print('Arquivo temporário:', tmp.name)
        print('Conteúdo:', tmp.read())
    os.remove(tmp.name)

# Diretório temporário
def exemplo_diretorio_temp():
    with tempfile.TemporaryDirectory() as tmpdir:
        print('Diretório temporário:', tmpdir)
        caminho = os.path.join(tmpdir, 'arquivo.txt')
        with open(caminho, 'w') as f:
            f.write('Arquivo dentro do diretório temporário')
        with open(caminho, 'r') as f:
            print('Conteúdo:', f.read())

# Exemplos no README-temporarios.md

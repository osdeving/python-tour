import zipfile
import tarfile

# ZIP
def criar_zip(arquivos, destino):
    with zipfile.ZipFile(destino, 'w') as z:
        for arquivo in arquivos:
            z.write(arquivo)

def extrair_zip(caminho_zip, destino):
    with zipfile.ZipFile(caminho_zip, 'r') as z:
        z.extractall(destino)

# TAR
def criar_tar(arquivos, destino):
    with tarfile.open(destino, 'w') as t:
        for arquivo in arquivos:
            t.add(arquivo)

def extrair_tar(caminho_tar, destino):
    with tarfile.open(caminho_tar, 'r') as t:
        t.extractall(destino)

# Exemplos:
# criar_zip(['a.txt', 'b.txt'], 'exemplo.zip')
# extrair_zip('exemplo.zip', 'destino/')
# criar_tar(['a.txt', 'b.txt'], 'exemplo.tar')
# extrair_tar('exemplo.tar', 'destino/')

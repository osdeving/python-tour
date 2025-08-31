import gzip
import bz2
import lzma
import mmap

# Leitura streaming (linha a linha)
def ler_linha_a_linha(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        for linha in f:
            yield linha

# Leitura em chunks (blocos de bytes)
def ler_em_chunks(caminho, tamanho=1024):
    with open(caminho, 'rb') as f:
        while True:
            chunk = f.read(tamanho)
            if not chunk:
                break
            yield chunk

# mmap (memory-mapped files)
def ler_mmap(caminho):
    with open(caminho, 'rb') as f:
        mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        return mm[:100]  # exemplo: primeiros 100 bytes

# Compressão
def comprimir_gzip(caminho, destino):
    with open(caminho, 'rb') as f_in, gzip.open(destino, 'wb') as f_out:
        f_out.writelines(f_in)

def descomprimir_gzip(caminho, destino):
    with gzip.open(caminho, 'rb') as f_in, open(destino, 'wb') as f_out:
        f_out.write(f_in.read())

# bz2 e lzma seguem padrão similar

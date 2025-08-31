import struct
import pickle
import pandas as pd
import openpyxl

# struct: binário baixo nível
def escrever_binario(caminho, valores, formato):
    with open(caminho, 'wb') as f:
        f.write(struct.pack(formato, *valores))

def ler_binario(caminho, formato):
    with open(caminho, 'rb') as f:
        return struct.unpack(formato, f.read(struct.calcsize(formato)))

# pickle: serialização de objetos
def salvar_pickle(caminho, obj):
    with open(caminho, 'wb') as f:
        pickle.dump(obj, f)

def ler_pickle(caminho):
    with open(caminho, 'rb') as f:
        return pickle.load(f)

# Excel: pandas/openpyxl
def ler_excel(caminho):
    return pd.read_excel(caminho)

def escrever_excel(caminho, dados):
    df = pd.DataFrame(dados)
    df.to_excel(caminho, index=False)

# Exemplos no README-tabulares-binarios.md

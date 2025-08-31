from pathlib import Path
import os
import shutil

def criar_diretorio(caminho):
    Path(caminho).mkdir(exist_ok=True)

def criar_arquivo(caminho):
    Path(caminho).touch()

def info_arquivo(caminho):
    p = Path(caminho)
    return {
        'tamanho': p.stat().st_size,
        'modificado': p.stat().st_mtime
    }

def copiar_arquivo(origem, destino):
    shutil.copy2(origem, destino)

def mover_arquivo(origem, destino):
    shutil.move(origem, destino)

def apagar_arquivo(caminho):
    Path(caminho).unlink(missing_ok=True)

# Exemplos:
# criar_diretorio('teste')
# criar_arquivo('teste/arquivo.txt')
# print(info_arquivo('teste/arquivo.txt'))
# copiar_arquivo('teste/arquivo.txt', 'teste/copia.txt')
# mover_arquivo('teste/copia.txt', 'teste/copia2.txt')
# apagar_arquivo('teste/copia2.txt')

from pathlib import Path
import glob
import shutil

# Buscar arquivos (glob)
def buscar_arquivos(padrao):
    return list(Path('.').glob(padrao))

# Buscar e substituir em múltiplos arquivos
def buscar_substituir(padrao, busca, substitui):
    for caminho in Path('.').glob(padrao):
        if caminho.is_file():
            texto = caminho.read_text(encoding='utf-8')
            novo_texto = texto.replace(busca, substitui)
            caminho.write_text(novo_texto, encoding='utf-8')

# Deduplicar e filtrar linhas
def deduplicar_arquivo(caminho):
    linhas = Path(caminho).read_text(encoding='utf-8').splitlines()
    unicas = list(dict.fromkeys(linhas))
    Path(caminho).write_text('\n'.join(unicas), encoding='utf-8')

# Concatenar arquivos grandes
def concatenar_arquivos(arquivos, destino):
    with open(destino, 'w', encoding='utf-8') as f_out:
        for arq in arquivos:
            with open(arq, 'r', encoding='utf-8') as f_in:
                shutil.copyfileobj(f_in, f_out)

# Converter CSV para JSON
def csv_para_json(csv_path, json_path):
    import csv, json
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        dados = list(reader)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# Exemplos no README-tarefas-comuns.md

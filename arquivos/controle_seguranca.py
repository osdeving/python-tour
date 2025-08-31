import os
import stat
import tempfile

# Tratamento de exceções
def ler_arquivo_seguro(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return 'Arquivo não encontrado.'
    except PermissionError:
        return 'Permissão negada.'

# Escrita segura
def escrita_segura(caminho, conteudo):
    with tempfile.NamedTemporaryFile('w', delete=False, encoding='utf-8') as tmp:
        tmp.write(conteudo)
        tmp.flush()
        os.replace(tmp.name, caminho)

# Permissões
def alterar_permissao(caminho, modo):
    os.chmod(caminho, modo)

def info_permissao(caminho):
    return stat.filemode(os.stat(caminho).st_mode)

# File locking (Unix)
def lock_arquivo(caminho):
    import fcntl
    with open(caminho, 'w') as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.write('Arquivo bloqueado')
        fcntl.flock(f, fcntl.LOCK_UN)

# Exemplos no README-controle-seguranca.md

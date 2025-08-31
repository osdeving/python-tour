import logging
import sqlite3
import shelve

# Escrita contínua em logs
def configurar_log(caminho):
    logging.basicConfig(filename=caminho, level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.info('Log iniciado')

# Rotação de logs
def configurar_log_rotativo(caminho):
    from logging.handlers import RotatingFileHandler
    handler = RotatingFileHandler(caminho, maxBytes=10000, backupCount=3)
    logger = logging.getLogger('rotativo')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.info('Log rotativo iniciado')

# Persistência simples com sqlite3
def salvar_sqlite(caminho, dados):
    conn = sqlite3.connect(caminho)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS exemplo (id INTEGER, valor TEXT)')
    cur.executemany('INSERT INTO exemplo VALUES (?, ?)', dados)
    conn.commit()
    conn.close()

# Persistência simples com shelve
def salvar_shelve(caminho, dados):
    with shelve.open(caminho) as db:
        for k, v in dados.items():
            db[k] = v

# Exemplos no README-logs-persistencia.md

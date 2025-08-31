import requests
from ftplib import FTP
# Para SFTP: pip install paramiko
import paramiko

# Baixar arquivos HTTP
def baixar_arquivo_http(url, destino):
    r = requests.get(url)
    with open(destino, 'wb') as f:
        f.write(r.content)

# FTP
def baixar_arquivo_ftp(host, arquivo, destino, usuario='', senha=''):
    with FTP(host) as ftp:
        ftp.login(usuario, senha)
        with open(destino, 'wb') as f:
            ftp.retrbinary(f'RETR {arquivo}', f.write)

# SFTP
def baixar_arquivo_sftp(host, usuario, senha, arquivo, destino):
    client = paramiko.Transport((host, 22))
    client.connect(username=usuario, password=senha)
    sftp = paramiko.SFTPClient.from_transport(client)
    sftp.get(arquivo, destino)
    sftp.close()
    client.close()

# Exemplos no README-redes-remotos.md

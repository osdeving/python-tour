# 📂 Roadmap – Trabalhando com Arquivos em Python

> Guia prático para dominar manipulação de arquivos no Python.  
> Use os checkboxes `[ ]` para acompanhar seu progresso.

---

## 📑 Table of Contents
- [1. Fundamentos](#1-fundamentos)
- [2. Caminhos e Sistemas de Arquivos](#2-caminhos-e-sistemas-de-arquivos)
- [3. Trabalhando com Texto Estruturado](#3-trabalhando-com-texto-estruturado)
- [4. Arquivos Grandes e Performance](#4-arquivos-grandes-e-performance)
- [5. Arquivos Comprimidos e Arquivos-Container](#5-arquivos-comprimidos-e-arquivos-container)
- [6. Controle e Segurança](#6-controle-e-segurança)
- [7. Arquivos Temporários e Diretórios](#7-arquivos-temporários-e-diretórios)
- [8. Tarefas Comuns](#8-tarefas-comuns)
- [9. Dados Tabulares e Binários Estruturados](#9-dados-tabulares-e-binários-estruturados)
- [10. Redes e Arquivos Remotos](#10-redes-e-arquivos-remotos)
- [11. Logs e Persistência Simples](#11-logs-e-persistência-simples)
- [12. Ferramentas Avançadas](#12-ferramentas-avançadas)

---

## 1. Fundamentos
- [ ] Abrindo arquivos com `open()`  
- [ ] Modos de abertura (`r`, `w`, `a`, `x`, `b`, `+`)  
- [ ] Context manager (`with open(...) as f`)  
- [ ] Leitura e escrita em arquivos de texto  
- [ ] Manipulação de arquivos binários  

🔗 Referência: [Python Docs – Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

---

## 2. Caminhos e Sistemas de Arquivos
- [ ] `os` vs `pathlib`  
- [ ] Criando diretórios e arquivos (`mkdir`, `touch`)  
- [ ] Inspeção de arquivos (`stat`, tamanho, data)  
- [ ] Copiar, mover, apagar (`shutil`)  

🔗 Referência: [pathlib](https://docs.python.org/3/library/pathlib.html), [shutil](https://docs.python.org/3/library/shutil.html)

---

## 3. Trabalhando com Texto Estruturado
- [ ] CSV → módulo `csv`  
- [ ] JSON → `json`, `orjson`  
- [ ] YAML → `pyyaml`, `ruamel.yaml`  
- [ ] Configurações (`configparser`, `.env` com `python-dotenv`)  

🔗 Referência: [csv](https://docs.python.org/3/library/csv.html), [json](https://docs.python.org/3/library/json.html)

---

## 4. Arquivos Grandes e Performance
- [ ] Leitura streaming (linha a linha)  
- [ ] Leitura em chunks (blocos de bytes)  
- [ ] `mmap` (memory-mapped files)  
- [ ] Compressão (`gzip`, `bz2`, `lzma`)  

🔗 Referência: [mmap](https://docs.python.org/3/library/mmap.html), [gzip](https://docs.python.org/3/library/gzip.html)

---

## 5. Arquivos Comprimidos e Arquivos-Container
- [ ] Criar/ler `zip` (`zipfile`)  
- [ ] Criar/ler `tar` (`tarfile`)  
- [ ] Extração de múltiplos arquivos  

🔗 Referência: [zipfile](https://docs.python.org/3/library/zipfile.html), [tarfile](https://docs.python.org/3/library/tarfile.html)

---

## 6. Controle e Segurança
- [ ] Tratamento de exceções (`FileNotFoundError`, `PermissionError`)  
- [ ] Escrita segura (arquivos temporários + `os.replace`)  
- [ ] Permissões (`os.chmod`, `stat`)  
- [ ] File locking (`fcntl`, `portalocker`)  

🔗 Referência: [os](https://docs.python.org/3/library/os.html), [stat](https://docs.python.org/3/library/stat.html)

---

## 7. Arquivos Temporários e Diretórios
- [ ] `tempfile.NamedTemporaryFile`  
- [ ] `tempfile.TemporaryDirectory`  

🔗 Referência: [tempfile](https://docs.python.org/3/library/tempfile.html)

---

## 8. Tarefas Comuns
- [ ] Buscar arquivos (`glob`, `fnmatch`, `pathlib.glob`)  
- [ ] Buscar e substituir em múltiplos arquivos  
- [ ] Deduplicar e filtrar linhas  
- [ ] Concatenar e dividir arquivos grandes  
- [ ] Converter formatos (CSV ↔ JSON, TXT ↔ Excel)  

🔗 Referência: [glob](https://docs.python.org/3/library/glob.html)

---

## 9. Dados Tabulares e Binários Estruturados
- [ ] `struct` (binário baixo nível)  
- [ ] `pickle` (serialização de objetos)  
- [ ] Excel (`openpyxl`, `pandas`)  

🔗 Referência: [struct](https://docs.python.org/3/library/struct.html), [pickle](https://docs.python.org/3/library/pickle.html)

---

## 10. Redes e Arquivos Remotos
- [ ] Baixar arquivos (`requests`)  
- [ ] FTP/SFTP (`ftplib`, `paramiko`)  
- [ ] Cloud storage (S3/GCS/Azure Blob: `boto3`, `gcsfs`, `azure-storage-blob`)  

🔗 Referência: [requests](https://requests.readthedocs.io/)

---

## 11. Logs e Persistência Simples
- [ ] Escrita contínua em logs  
- [ ] Rotação de logs (`logging.handlers`)  
- [ ] Bancos simples baseados em arquivos (`sqlite3`, `shelve`)  

🔗 Referência: [logging](https://docs.python.org/3/library/logging.html), [sqlite3](https://docs.python.org/3/library/sqlite3.html)

---

## 12. Ferramentas Avançadas
- [ ] Watcher de arquivos (`watchdog`)  
- [ ] Parsing de XML/HTML (`lxml`, `BeautifulSoup`)  
- [ ] PDFs (`PyPDF2`, `pdfplumber`)  
- [ ] Imagens (`Pillow`)  
- [ ] Áudio (`wave`, `pydub`, `soundfile`)  

🔗 Referência: [watchdog](https://pypi.org/project/watchdog/), [pillow](https://pypi.org/project/Pillow/)

---

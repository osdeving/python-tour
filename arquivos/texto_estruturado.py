import csv
import json
import yaml
import configparser
from dotenv import dotenv_values

# CSV
def ler_csv(caminho):
    with open(caminho, newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

def escrever_csv(caminho, linhas):
    with open(caminho, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(linhas)

# JSON
def ler_json(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return json.load(f)

def escrever_json(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

# YAML
# pip install pyyaml

def ler_yaml(caminho):
    with open(caminho, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def escrever_yaml(caminho, dados):
    with open(caminho, 'w', encoding='utf-8') as f:
        yaml.safe_dump(dados, f, allow_unicode=True)

# ConfigParser

def ler_ini(caminho):
    config = configparser.ConfigParser()
    config.read(caminho)
    return config

def escrever_ini(caminho, config):
    with open(caminho, 'w', encoding='utf-8') as f:
        config.write(f)

# dotenv (.env)
def ler_env(caminho):
    return dotenv_values(caminho)

# Exemplos de uso estão no README-texto-estruturado.md

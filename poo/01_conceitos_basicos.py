# Tópico 1.1 — Conceitos básicos: classe, objeto, atributos, métodos
#
# Objetivo:
# - Entender o que é uma classe e um objeto (instância)
# - Diferenciar atributos de instância e de classe
# - Criar e usar métodos de instância
# - Boas práticas e dicas de uso em Python
#
# Nota sobre tipagem/anotações:
# - Este arquivo usa "from __future__ import annotations" e tipos do módulo typing
#   para facilitar exemplos e forward-references.
# - Para um guia completo e transversal sobre tipagem moderna (List vs list[int],
#   Union/|, Optional, Protocol, TypedDict, dataclasses, Self, Annotated, etc.),
#   veja: poo/00_typagem_anotacoes.py

from __future__ import annotations
from typing import List


# 1) Uma classe simples com atributos e métodos
class Pessoa:
    """
    Classe simples representando uma pessoa.
    - Atributos de instância: definidos no __init__ (nome, idade)
    - Atributo de classe: especie (compartilhado entre instâncias)
    """

    especie = "Humano"  # atributo de classe: comum a TODAS as pessoas

    def __init__(self, nome: str, idade: int):
        # Atributos de instância, pertencem a CADA objeto criado
        self.nome = nome
        self.idade = idade

    def cumprimentar(self) -> str:
        # Métodos sempre recebem self (a instância atual)
        return f"Olá, eu sou {self.nome} ({self.idade} anos)."

    def fazer_aniversario(self) -> None:
        self.idade += 1


# 2) Outra classe com operações (métodos) e estado interno
class ContaBancaria:
    """
    Exemplo de classe com operações básicas.
    Observações:
    - Em Python, não há atributos realmente privados, mas usamos convenções.
    - Vamos manter os atributos simples aqui e validar em métodos.
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = float(saldo_inicial)

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")
        self.saldo -= valor

    def extrato(self) -> str:
        return f"Titular: {self.titular} | Saldo: R$ {self.saldo:,.2f}"


# 3) Atributos de instância vs. Atributos de classe
class ConfiguracaoApp:
    # Atributos de classe: valores default/constantes compartilhadas
    VERSAO = "1.0.0"
    SUPORTA_CACHE = True

    def __init__(self, nome_modulo: str, ativos: List[str] | None = None):
        # Atributos de instância: variam por objeto
        self.nome_modulo = nome_modulo
        self.ativos = list(ativos or [])

    def ativar(self, nome: str) -> None:
        if nome not in self.ativos:
            self.ativos.append(nome)

    def desativar(self, nome: str) -> None:
        if nome in self.ativos:
            self.ativos.remove(nome)


# 4) Boas práticas e dicas:
# - Use nomes descritivos para classes (CamelCase) e métodos/atributos (snake_case).
# - Sempre inclua self como primeiro parâmetro de métodos de instância.
# - Prefira inicializar atributos no __init__.
# - Evite criar atributos "dinamicamente" fora do __init__ (pode confundir manutenção).


def demo_pessoa():
    print("\n[DEMO] Pessoa")
    p = Pessoa("Ana", 30)
    print(p.cumprimentar())
    p.fazer_aniversario()
    print(p.cumprimentar())

    # Acesso a atributo de classe (compartilhado)
    print("Espécie:", Pessoa.especie, p.especie)

    # Criação dinâmica de atributo (possível, mas não recomendado como prática geral)
    # Útil em scripts rápidos, porém evite em código de produção sem necessidade.
    p.altura_m = 1.70  # cuidado: não foi declarado no __init__
    print("Altura (dinâmica):", p.altura_m)


def demo_conta():
    print("\n[DEMO] ContaBancaria")
    conta = ContaBancaria("Carlos", 100.0)
    print(conta.extrato())
    conta.depositar(50)
    print(conta.extrato())
    try:
        conta.sacar(200)
    except ValueError as e:
        print("Erro no saque:", e)
    conta.sacar(120)
    print(conta.extrato())


def demo_config():
    print("\n[DEMO] ConfiguracaoApp: classe vs instância")
    cfg_api = ConfiguracaoApp("api", ["auth"])  # instância 1
    cfg_web = ConfiguracaoApp("web")            # instância 2

    cfg_api.ativar("ratelimit")
    cfg_web.ativar("cache")

    print("Versão (classe):", ConfiguracaoApp.VERSAO)
    print("API ativos:", cfg_api.ativos)
    print("WEB ativos:", cfg_web.ativos)


if __name__ == "__main__":
    # Execução de exemplos
    demo_pessoa()
    demo_conta()
    demo_config()

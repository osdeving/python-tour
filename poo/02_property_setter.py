# Tópico 2.2 — Uso de @property e setters
#
# - @property cria um atributo "calculado" com sintaxe de acesso de atributo
# - Use setter para validar e controlar escrita
# - Pode haver deleter (remover/limpar), mas raramente é necessário
# - Invariantes do objeto podem ser garantidos por propriedades

from __future__ import annotations
from datetime import date
from functools import cached_property


class Pessoa:
    def __init__(self, nome: str, ano_nascimento: int):
        self._nome = nome            # "protegido" por convenção
        self._ano_nascimento = ano_nascimento

    # property de leitura simples
    @property
    def nome(self) -> str:
        return self._nome

    # setter com validação
    @nome.setter
    def nome(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("Nome inválido")
        self._nome = valor.strip()

    # property somente leitura (sem setter declarado)
    @property
    def idade(self) -> int:
        ano_atual = date.today().year
        return ano_atual - self._ano_nascimento

    # property "caro" com cache (só calcula uma vez por instância)
    @cached_property
    def perfil_publico(self) -> str:
        # Simula uma operação cara (montagem complexa)
        return f"{self.nome} ({self.idade} anos)"


class Conta:
    def __init__(self, saldo_inicial: float = 0.0):
        self._saldo = float(saldo_inicial)

    @property
    def saldo(self) -> float:
        return self._saldo

    @saldo.setter
    def saldo(self, valor: float) -> None:
        # Evite expor set direto em domínios críticos; aqui é didático.
        if valor < 0:
            raise ValueError("Saldo não pode ser negativo")
        self._saldo = valor

    @saldo.deleter
    def saldo(self) -> None:  # type: ignore[no-redef]
        # Raramente usado, mas pode ser útil (ex.: revogar credenciais)
        self._saldo = 0.0


def demo_pessoa():
    print("\n[DEMO] Propriedades de Pessoa")
    p = Pessoa("Ana", 1990)
    print("Nome:", p.nome)
    print("Idade:", p.idade)
    p.nome = " Ana Maria "  # setter com strip e validação
    print("Nome atualizado:", p.nome)
    print("Perfil público (cached_property):", p.perfil_publico)
    print("Perfil público (cacheado):", p.perfil_publico)


def demo_conta():
    print("\n[DEMO] Propriedade com setter/deleter em Conta")
    c = Conta(100)
    print("Saldo:", c.saldo)
    c.saldo = 200
    print("Saldo atualizado:", c.saldo)
    try:
        c.saldo = -10
    except ValueError as e:
        print("Erro ao definir saldo:", e)
    del c.saldo
    print("Saldo após deleter:", c.saldo)


# Diretrizes:
# - Prefira propriedades para encapsular regras sem quebrar a API do chamador.
# - Use nomes simples (como atributos). Evite métodos get_/set_ desnecessários.
# - Evite efeitos colaterais pesados em getters (se necessário, considere cached_property).


if __name__ == "__main__":
    demo_pessoa()
    demo_conta()


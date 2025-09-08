# Tópico 1.2 — Encapsulamento
#
# Encapsular = esconder detalhes internos e expor uma interface estável.
# Em Python:
# - Não há "private" real; usamos CONVENÇÕES:
#   - nome_publico        -> parte da API
#   - _nome_protegido     -> detalhe interno (use com cuidado)
#   - __nome_privado      -> name mangling (_Classe__nome_privado)
# - Use propriedades (@property) para controlar leitura/escrita com validação.

from __future__ import annotations


class Conta:
    """
    Exemplo prático de encapsulamento com validação e API estável.
    - _saldo: atributo "protegido" por convenção (não use direto fora da classe).
    - Métodos depositar/sacar: únicos pontos de mutação.
    - Propriedade 'saldo' para leitura segura (somente leitura aqui).
    """

    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self._saldo = float(saldo_inicial)  # detalhe interno

    @property
    def saldo(self) -> float:
        # Leitura controlada. Poderíamos registrar métricas/log aqui.
        return self._saldo

    def depositar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Depósito deve ser positivo.")
        self._saldo += valor

    def sacar(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("Saque deve ser positivo.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor


class Cofre:
    """
    Demonstração de name mangling com __segredo.
    - __segredo vira _Cofre__segredo internamente (para evitar colisões com subclasses).
    - Ainda é acessível (não é segurança), mas sinaliza fortemente: NÃO USE DIRETO.
    """

    def __init__(self, segredo: str):
        self.__segredo = segredo  # "privado" via name mangling

    def verificar(self, tentativa: str) -> bool:
        return tentativa == self.__segredo

    def _rotacionar_segredo(self, novo: str) -> None:
        # Método "protegido": parte da API interna.
        self.__segredo = novo


def demo_conta():
    print("\n[DEMO] Encapsulamento com Conta")
    c = Conta("Alice", 100)
    print("Titular:", c.titular)
    print("Saldo (property):", c.saldo)
    c.depositar(50)
    print("Saldo após depósito:", c.saldo)
    try:
        c._saldo = 1_000_000  # possível (Python não impede), mas má prática!
        print("Acesso indevido alterou saldo:", c.saldo)
    finally:
        # Corrige o estado via API pública
        c._saldo = 150
        print("Saldo corrigido:", c.saldo)


def demo_cofre():
    print("\n[DEMO] Name mangling com Cofre")
    cof = Cofre("1234")
    print("1234 é correto?", cof.verificar("1234"))
    # Atributo sofre name mangling; ainda é acessível com o nome "mangleado":
    print("Acesso via name-mangling (NÃO RECOMENDADO):", getattr(cof, "_Cofre__segredo"))
    cof._rotacionar_segredo("abcd")
    print("abcd é correto?", cof.verificar("abcd"))


# Diretrizes rápidas:
# - Prefira expor métodos/propriedades para invariantes (regras) do objeto.
# - Use _nome para indicar "não faça isso em casa".
# - Use __nome para evitar colisão em herança múltipla (não para segurança real).
# - Garanta estados válidos apenas via API pública (métodos e propriedades).


if __name__ == "__main__":
    demo_conta()
    demo_cofre()


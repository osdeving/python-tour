# Tópico 1.4 — Polimorfismo
#
# Polimorfismo = múltiplas formas. Em Python, é natural via duck typing.
# Formas:
# - Duck typing: "se anda como pato e grasna como pato..."
# - Sobrescrita: subclasses implementam o mesmo método de forma diferente
# - ABCs (Abstract Base Classes): contratos com @abstractmethod
# - Protocols (typing): contratos estruturais, sem herança

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Protocol
import math


# 1) Duck typing simples
class Cachorro:
    def falar(self) -> str:
        return "Au au!"


class Gato:
    def falar(self) -> str:
        return "Miau!"


def fazer_falar(animais: Iterable[object]) -> None:
    # Não exigimos um tipo específico; só que tenha .falar()
    for a in animais:
        if hasattr(a, "falar"):
            print(a.falar())  # type: ignore[attr-defined]
        else:
            print("[silêncio]")


# 2) ABCs: contrato formal
class Forma(ABC):
    @abstractmethod
    def area(self) -> float:  # contrato: toda Forma deve ter area()
        raise NotImplementedError


class Retangulo(Forma):
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura


class Circulo(Forma):
    def __init__(self, raio: float):
        self.raio = raio

    def area(self) -> float:
        return math.pi * (self.raio ** 2)


def soma_areas(formas: Iterable[Forma]) -> float:
    return sum(f.area() for f in formas)


# 3) Protocol (tipagem estrutural)
class Falante(Protocol):
    def falar(self) -> str:  # não implementa, só define a "forma"
        ...


def eco(ser: Falante) -> str:
    # Aceita qualquer coisa que TENHA falar() -> str
    return f"Eco: {ser.falar()}"


def demo_duck_typing():
    print("\n[DEMO] Duck typing")
    fazer_falar([Cachorro(), Gato(), object()])


def demo_abstratas():
    print("\n[DEMO] ABCs")
    formas = [Retangulo(2, 3), Circulo(1.5)]
    print("Soma das áreas:", soma_areas(formas))


def demo_protocol():
    print("\n[DEMO] Protocol")

    class Papagaio:
        def falar(self) -> str:
            return "Curió!"

    print(eco(Papagaio()))  # Papagaio "bate" com Falante sem herdar nada


# Diretrizes:
# - Prefira duck typing quando possível: código mais flexível e pythonico.
# - Use ABC quando quiser exigir implementação (bibliotecas, plugins).
# - Protocols ajudam o type checker sem forçar herança.


if __name__ == "__main__":
    demo_duck_typing()
    demo_abstratas()
    demo_protocol()


# Tópico 2.3 — Dunder methods comuns (__str__, __repr__, __len__, __eq__)
#
# - __repr__: representação não-ambígua (debug/log); idealmente que permita reconstrução
# - __str__: representação amigável ao usuário (legível)
# - __len__: define len(obj)
# - __eq__: igualdade lógica; retorne NotImplemented quando tipo não for suportado

from __future__ import annotations
from typing import Any, Iterable, List


class Ponto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        # Representação "oficial" para debug; idealmente inequívoca
        return f"Ponto(x={self.x!r}, y={self.y!r})"

    def __str__(self) -> str:
        # Representação amigável
        return f"({self.x}, {self.y})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Ponto):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)


class CarrinhoDeCompras:
    def __init__(self):
        self._itens: List[str] = []

    def adicionar(self, item: str) -> None:
        self._itens.append(item)

    def __len__(self) -> int:
        # Permite usar len(carrinho)
        return len(self._itens)

    def __repr__(self) -> str:
        return f"CarrinhoDeCompras(itens={self._itens!r})"

    def __str__(self) -> str:
        return ", ".join(self._itens) or "(vazio)"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, CarrinhoDeCompras):
            return NotImplemented
        # Igualdade por conteúdo (ordem importa)
        return self._itens == other._itens


def demo_ponto():
    print("\n[DEMO] Ponto: __repr__, __str__, __eq__")
    p1 = Ponto(1, 2)
    p2 = Ponto(1, 2)
    p3 = Ponto(2, 3)
    print("repr:", repr(p1))
    print("str:", str(p1))
    print("p1 == p2:", p1 == p2)
    print("p1 == p3:", p1 == p3)
    print("p1 == (1,2):", p1 == (1, 2))  # NotImplemented -> False no Python


def demo_carrinho():
    print("\n[DEMO] Carrinho: __len__, __str__, __eq__")
    a = CarrinhoDeCompras()
    b = CarrinhoDeCompras()
    a.adicionar("arroz")
    a.adicionar("feijão")
    b.adicionar("arroz")
    print("a:", a, "| len:", len(a))
    print("b:", b, "| len:", len(b))
    print("a == b:", a == b)
    b.adicionar("feijão")
    print("a == b (agora):", a == b)


# Diretrizes:
# - __repr__ para debug: inclua o máximo de informação útil e inequívoca.
# - __str__ para usuários: mantenha legível.
# - Em __eq__, retorne NotImplemented para tipos desconhecidos (permite simetria).
# - Se definir __eq__, avalie também __hash__ (imutáveis) ou defina objetos como não-hashables.


if __name__ == "__main__":
    demo_ponto()
    demo_carrinho()


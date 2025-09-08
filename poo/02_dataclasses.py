# Tópico 2.4 — Dataclasses
#
# - Reduz boilerplate para classes de dados
# - Gera __init__, __repr__, __eq__, etc. automaticamente
# - Suporte a defaults, default_factory, frozen (imutável), order, slots

from __future__ import annotations
from dataclasses import dataclass, field, asdict, astuple, replace
from typing import List


@dataclass
class Produto:
    nome: str
    preco: float
    tags: List[str] = field(default_factory=list)

    def aplicar_desconto(self, pct: float) -> None:
        self.preco *= (1 - pct)


@dataclass(frozen=True)
class Coordenada:
    x: float
    y: float

    # Em frozen=True, os atributos não podem ser alterados após criação.


@dataclass(order=True)
class Prioridade:
    nivel: int
    descricao: str
    # Com order=True, gera ordering com base nos campos na ordem declarada.


@dataclass(slots=True)
class Usuario:
    nome: str
    email: str
    # slots=True economiza memória e evita criação dinâmica de atributos.


def demo_basico():
    print("\n[DEMO] Básico")
    p = Produto("Camiseta", 80.0)
    print("repr:", p)  # __repr__ auto
    p.aplicar_desconto(0.1)
    print("dict:", asdict(p))
    print("tuple:", astuple(p))


def demo_frozen():
    print("\n[DEMO] Frozen (imutável)")
    c = Coordenada(1, 2)
    print(c)
    try:
        c.x = 10  # type: ignore[misc]
    except Exception as e:
        print("Erro esperado ao alterar frozen:", e)


def demo_order():
    print("\n[DEMO] Order")
    itens = [Prioridade(3, "baixo"), Prioridade(1, "alto"), Prioridade(2, "médio")]
    print(sorted(itens))  # ordena por nivel


def demo_slots():
    print("\n[DEMO] Slots na dataclass")
    u = Usuario("Ana", "ana@example.com")
    print(u)
    try:
        u.idade = 30  # type: ignore[attr-defined]
    except AttributeError as e:
        print("Atributo dinâmico proibido em slots:", e)


def demo_replace():
    print("\n[DEMO] replace() para cópias modificadas")
    p = Produto("Livro", 50.0, ["promo"]) 
    p2 = replace(p, preco=45.0)  # cópia com campo alterado
    print(p, "->", p2)


# Diretrizes:
# - Use dataclasses quando o foco for dados/comportamento simples.
# - frozen=True para imutabilidade (bom para chaves, cache, concorrência).
# - order=True quando precisar comparar/ordenar instâncias.
# - slots=True quando quiser economia de memória e impedir atributos dinâmicos.


if __name__ == "__main__":
    demo_basico()
    demo_frozen()
    demo_order()
    demo_slots()
    demo_replace()


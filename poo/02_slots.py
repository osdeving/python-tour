# Tópico 2.5 — __slots__
#
# - __slots__ limita os atributos permitidos e elimina __dict__ por padrão
# - Reduz uso de memória e acelera acesso em alguns cenários
# - Impede adição dinâmica de atributos (AttributeError)
# - Cuidado em herança múltipla; inclua '__weakref__' se precisar de weakrefs

from __future__ import annotations


class PontoComSlots:
    __slots__ = ("x", "y")  # somente estes atributos serão permitidos

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def mover(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy


class PontoComSlotsWeakref:
    # Inclua __weakref__ se quiser permitir weak references
    __slots__ = ("x", "y", "__weakref__")

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def demo_slots_basico():
    print("\n[DEMO] __slots__ básico")
    p = PontoComSlots(1, 2)
    print(p.x, p.y)
    p.mover(1, -1)
    print("Movido:", p.x, p.y)
    try:
        p.z = 10  # type: ignore[attr-defined]
    except AttributeError as e:
        print("Atributo dinâmico bloqueado:", e)


# Herança com slots:
class Base:
    __slots__ = ("a",)

    def __init__(self):
        self.a = 1


class Mixin:
    # Não define slots; possui __dict__
    def mix(self):
        return "ok"


class Derivada(Base, Mixin):
    # A classe final terá __dict__ por causa de Mixin (sem __slots__).
    # Para manter slots, TODAS as classes na hierarquia devem declarar __slots__.
    __slots__ = ("b",)

    def __init__(self):
        super().__init__()
        self.b = 2


def demo_heranca_slots():
    print("\n[DEMO] __slots__ em herança")
    d = Derivada()
    print("a:", d.a, "b:", d.b, "tem __dict__?", hasattr(d, "__dict__"))


# Diretrizes:
# - Use __slots__ quando há MUITAS instâncias e memória é crítica.
# - Evite em classes que precisam de flexibilidade/extensibilidade via atributos dinâmicos.
# - Em herança, alinhe __slots__ em toda a hierarquia para manter o benefício.


if __name__ == "__main__":
    demo_slots_basico()
    demo_heranca_slots()


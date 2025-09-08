# Tópico 1.3 — Herança simples e múltipla
#
# Objetivo:
# - Usar herança simples com super()
# - Entender herança múltipla, MRO e mixins
# - Boas práticas para evitar confusão

from __future__ import annotations
from typing import Any, Dict
import json


# 1) Herança simples
class Veiculo:
    def __init__(self, marca: str):
        self.marca = marca

    def mover(self) -> str:
        return f"{self.marca}: o veículo está em movimento"


class Carro(Veiculo):
    def __init__(self, marca: str, portas: int = 4):
        super().__init__(marca)  # chama construtor da base
        self.portas = portas

    def mover(self) -> str:
        # Sobrescrita (override) com extensão de comportamento
        base = super().mover()
        return f"{base} (dirigindo um carro de {self.portas} portas)"


class CarroEletrico(Carro):
    def __init__(self, marca: str, portas: int = 4, autonomia_km: int = 300):
        super().__init__(marca, portas)
        self.autonomia_km = autonomia_km

    def mover(self) -> str:
        return f"{self.marca}: rodando silenciosamente (autonomia {self.autonomia_km} km)"


# 2) Mixins e herança múltipla
class LogavelMixin:
    """
    Mixin: fornece comportamento adicional para ser herdado junto com outra classe.
    - Não deve ser instanciado sozinho
    - Não mantém estado próprio complexo (em geral)
    """

    def log(self, msg: str) -> None:
        print(f"[LOG:{self.__class__.__name__}] {msg}")


class JSONSerializableMixin:
    def to_json(self) -> str:
        # Converte dicionário de atributos "públicos" em JSON
        data: Dict[str, Any] = {
            k: v for k, v in self.__dict__.items() if not k.startswith("_")
        }
        return json.dumps(data, ensure_ascii=False)


class CarroComLogJSON(CarroEletrico, LogavelMixin, JSONSerializableMixin):
    # Ordem importa! MRO define como super() resolve os métodos.
    def mover(self) -> str:
        self.log("Iniciando movimento")
        res = super().mover()  # segue MRO: CarroEletrico -> Carro -> Veiculo
        self.log("Movimento concluído")
        return res


def demo_heranca_simples():
    print("\n[DEMO] Herança simples")
    v = Veiculo("Genérico")
    c = Carro("Toyota", 4)
    e = CarroEletrico("Tesla", 4, 500)
    print(v.mover())
    print(c.mover())
    print(e.mover())


def demo_heranca_multipla():
    print("\n[DEMO] Herança múltipla e MRO")
    cj = CarroComLogJSON("BYD", 4, 420)
    print(cj.mover())
    print("JSON:", cj.to_json())
    print("MRO:", [cls.__name__ for cls in CarroComLogJSON.mro()])


# Diretrizes:
# - Prefira composição a herança quando a relação não for "é-um" (IS-A).
# - Mixins devem ser pequenos, focados e sem estado complexo.
# - Em herança múltipla, chame super() nas cadeias para respeitar o MRO.


if __name__ == "__main__":
    demo_heranca_simples()
    demo_heranca_multipla()


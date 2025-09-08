# Guia transversal — Tipagem e Anotações no Python moderno
#
# Objetivo:
# - Explicar por que e como usar type hints (PEP 484/526 e evoluções)
# - Mostrar boas práticas modernas (3.9+, 3.10+) e compatibilidade
# - Demonstrar "from __future__ import annotations", generics, Union/|, Optional,
#   Protocol, TypedDict, NewType, Literal, Final, ClassVar, Annotated, overload,
#   TypeVar/Generic, ParamSpec/Callable, get_type_hints e limites em runtime

from __future__ import annotations  # Adia a avaliação das anotações (armazenadas como str)

# Observações importantes:
# - Anotações de tipo são opcionais e não mudam a execução por padrão.
# - Elas servem para documentação, IDEs e validadores estáticos (mypy, pyright, ruff).
# - Em Python 3.7–3.10, "from __future__ import annotations" torna as anotações strings.
#   Em runtimes recentes (3.11+), essa é a semântica padrão; o import vira no-op.
# - Para avaliar (resolver) tipos em runtime, use typing.get_type_hints.

from typing import (
    Any,
    Optional,
    Union,
    List, Dict, Tuple, Set, Callable,
    Iterable, Iterator,
    TypeVar, Generic,
    Protocol, runtime_checkable,
    TypedDict, NewType,
    Literal,
    Final, ClassVar,
    Annotated,
    get_type_hints,
    TypeAlias,
)

# Recursos mais novos que podem não existir em versões < 3.11
try:  # Self: 3.11+ (disponível em typing_extensions para versões anteriores)
    from typing import Self  # type: ignore
except Exception:  # fallback seguro para rodar exemplos
    try:
        from typing_extensions import Self  # type: ignore
    except Exception:
        Self = Any  # type: ignore

try:  # ParamSpec/Concatenate: 3.10+ (em versões mais antigas via typing_extensions)
    from typing import ParamSpec, Concatenate
except Exception:
    try:
        from typing_extensions import ParamSpec, Concatenate  # type: ignore
    except Exception:
        ParamSpec = TypeVar("ParamSpecFallback")  # type: ignore
        def Concatenate(*args: Any) -> Any:  # type: ignore
            return Any


# 1) Noções básicas de anotações
def soma(a: int, b: int) -> int:
    return a + b


valor: int = 10  # PEP 526 — anotação de variável


# 2) List/Dict/Set/Tuple — formas moderna e legada
# - Moderno (3.9+): list[int], dict[str, int], set[str], tuple[int, str]
# - Legado (compat): List[int], Dict[str, int], Set[str], Tuple[int, str]

def upper_todos(nomes: list[str]) -> list[str]:
    return [n.upper() for n in nomes]


def somar_valores(mapa: Dict[str, int]) -> int:  # forma legada (ainda ok)
    return sum(mapa.values())


# 3) Uniões e opcionais
# - Moderno (3.10+): int | None; str | int
# - Legado: Optional[int] == Union[int, None]

def parse_int(texto: str | None) -> Optional[int]:
    if texto is None:
        return None
    try:
        return int(texto)
    except ValueError:
        return None


# 4) Literal, Final e ClassVar
TIPO_FIXO: Final[str] = "constante"  # não deve ser reatribuída (checada estaticamente)

class Config:
    VERSAO: ClassVar[str] = "1.0"  # atributo da classe (não da instância)
    modo: Literal["dev", "prod"] = "dev"


# 5) TypedDict para dicionários com shape conhecido
class UsuarioTD(TypedDict):
    id: int
    nome: str
    admin: bool


def is_admin(u: UsuarioTD) -> bool:
    return u["admin"]


# 6) Protocol e duck typing com contratos estruturais
class Enviavel(Protocol):
    def enviar(self, destino: str) -> bool: ...


@runtime_checkable
class Logavel(Protocol):
    def log(self, msg: str) -> None: ...


class Email:
    def enviar(self, destino: str) -> bool:
        return True

    def log(self, msg: str) -> None:
        print("[EMAIL]", msg)


def processa_envio(item: Enviavel) -> None:
    ok = item.enviar("destino@example.com")
    if isinstance(item, Logavel):  # runtime_checkable permite checagem em runtime
        item.log(f"enviado? {ok}")


# 7) NewType para criar tipos semânticos
UserId = NewType("UserId", int)


def carregar_usuario(user_id: UserId) -> str:
    # Evita confundir com int comum em checadores estáticos
    return f"usuario-{int(user_id)}"


# 8) Annotated para metadados de tipos (útil em validadores/Frameworks)
from math import sqrt

PositiveFloat = Annotated[float, "> 0"]  # metadado livre (interpretação por terceiros)


def hipotenusa(cat_a: PositiveFloat, cat_b: PositiveFloat) -> float:
    return sqrt(cat_a ** 2 + cat_b ** 2)


# 9) TypeAlias para declarar aliases explícitos
JSONDict: TypeAlias = dict[str, "JSONValue"]
JSONValue: TypeAlias = Union[str, int, float, bool, None, List["JSONValue"], JSONDict]


# 10) TypeVar/Generic: funções e classes genéricas
T = TypeVar("T")


def primeiro(it: Iterable[T]) -> T | None:
    for x in it:
        return x
    return None


class Caixa(Generic[T]):
    def __init__(self, valor: T):
        self.valor = valor

    def get(self) -> T:
        return self.valor


# 11) ParamSpec/Callable: tipando funções de ordem superior
P = ParamSpec("P")
R = TypeVar("R")


def chama_duas_vezes(fn: Callable[P, R], *args: P.args, **kwargs: P.kwargs) -> tuple[R, R]:
    return fn(*args, **kwargs), fn(*args, **kwargs)


# 12) overload: assinaturas alternativas para melhor inferência
from typing import overload


@overload
def to_list(x: None) -> list[None]: ...


@overload
def to_list(x: T) -> list[T]: ...


def to_list(x: T | None) -> list[T | None]:  # implementação única
    return [x]


# 13) Self para métodos fluentes (3.11+ ou typing_extensions)
class Builder:
    def __init__(self) -> None:
        self._partes: list[str] = []

    def add(self, p: str) -> Self:  # retorna a própria instância
        self._partes.append(p)
        return self

    def build(self) -> str:
        return "/".join(self._partes)


# 14) Forward references e get_type_hints
class Nodo:
    def __init__(self, valor: int, prox: Nodo | None = None):
        self.valor = valor
        self.prox = prox


def mostrar_type_hints() -> None:
    # Com __future__.annotations, __annotations__ guarda strings; get_type_hints resolve para objetos
    hints = get_type_hints(Nodo.__init__)
    print("get_type_hints(Nodo.__init__):", hints)


# 15) Limites em runtime
# - isinstance(x, list[int]) NÃO funciona; generics de typing não servem para isinstance.
# - Para checagens em runtime, use classes reais ou collections.abc.
from collections.abc import Sequence


def aceita_sequencia(xs: Sequence[int]) -> int:
    # Sequence é checável em runtime via isinstance(x, Sequence)
    return sum(xs)


def demo_rapida() -> None:
    print("soma(2,3) ->", soma(2, 3))
    print("upper_todos ->", upper_todos(["a", "b"]))
    print("parse_int('10')->", parse_int("10"), ", parse_int(None)->", parse_int(None))
    processa_envio(Email())
    print("carregar_usuario(UserId(5)) ->", carregar_usuario(UserId(5)))
    print("hipotenusa(3,4) ->", hipotenusa(3.0, 4.0))
    print("primeiro([1,2,3]) ->", primeiro([1, 2, 3]))
    c = Caixa("ok")
    print("Caixa[str].get() ->", c.get())
    print("to_list(42) ->", to_list(42))
    b = Builder().add("home").add("docs").add("api")
    print("Builder.build() ->", b.build())
    mostrar_type_hints()
    print("aceita_sequencia([1,2,3]) ->", aceita_sequencia([1, 2, 3]))


# Diretrizes rápidas
# - Prefira builtins genéricos (list[int]) no 3.9+; use typing.List em bases antigas.
# - Prefira | (Union) e X | None em vez de Optional[X] no 3.10+.
# - Evite Any quando possível; prefira tipos concretos, Protocols ou object.
# - Use Protocol para contratos; TypedDict para dicts estruturados; NewType para semântica.
# - Annotated para metadados (validação, docs); overload para APIs com múltiplas formas.
# - Use get_type_hints quando precisar de tipos resolvidos em runtime.
# - Lembre: type hints não validam sozinhos em runtime — combine com validadores quando necessário.


if __name__ == "__main__":
    demo_rapida()


# Tópico 2.1 — Métodos de instância, classe e estáticos
#
# - Métodos de instância: recebem self (acessam estado da instância)
# - Métodos de classe: recebem cls (acessam estado/classe; fábricas alternativas)
# - Métodos estáticos: não recebem self/cls (funções utilitárias relacionadas)

from __future__ import annotations
from datetime import datetime


class Usuario:
    plataforma = "web"  # atributo de classe

    def __init__(self, nome: str, criado_em: datetime | None = None):
        self.nome = nome
        self.criado_em = criado_em or datetime.utcnow()

    # 1) Método de instância: usa self
    def saudacao(self) -> str:
        return f"Olá, {self.nome}!"  # usa estado da instância

    # 2) Método de classe: usa cls e geralmente retorna instância
    @classmethod
    def convidado(cls) -> "Usuario":
        # Fábrica alternativa (named constructor)
        return cls("Convidado")  # respeita herança (retorna subtipo se chamado no filho)

    @classmethod
    def from_string(cls, raw: str, sep: str = ":") -> "Usuario":
        # Ex: "Maria:2024-01-01T10:00:00"
        nome, _, ts = raw.partition(sep)
        dt = datetime.fromisoformat(ts) if ts else None
        return cls(nome.strip(), dt)

    # 3) Método estático: utilitário sem dependência de estado
    @staticmethod
    def validar_nome(nome: str) -> bool:
        return bool(nome and nome.strip())


class Admin(Usuario):
    @classmethod
    def convidado(cls) -> "Admin":
        # Herda a ideia de fábrica, mas especializa o valor
        return cls("Admin Convidado")


def demo_instancia_classe_estatico():
    print("\n[DEMO] Métodos de instância/classe/estáticos")
    u = Usuario("Ana")
    print(u.saudacao())
    print("Plataforma (classe):", Usuario.plataforma)

    # Fábricas com @classmethod
    visitante = Usuario.convidado()
    print("Visitante:", visitante.nome)

    raw = "Maria:2024-01-01T10:00:00"
    maria = Usuario.from_string(raw)
    print("Maria criada em:", maria.criado_em.isoformat())

    # Utilitário com @staticmethod
    print("Nome válido?", Usuario.validar_nome("  ") is False)

    # Herança + classmethod: retorna subtipo automaticamente
    a = Admin.convidado()
    print("Admin convidado:", a.nome, type(a).__name__)


# Diretrizes:
# - Prefira @classmethod para fábricas alternativas (ex.: parsers, padrões, mocks).
# - Use @staticmethod para helpers relacionados, sem estado.
# - Métodos de instância operam no estado da instância; evite acessar atributos de classe por self.


if __name__ == "__main__":
    demo_instancia_classe_estatico()


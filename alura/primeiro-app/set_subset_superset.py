# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "rich",
# ]
# ///
from rich.console import Console
from rich.table import Table

console = Console()

# ==============================
# Cenários por relação (edite aqui)
# Cada valor é uma tupla: (textoA, textoB)
# ==============================
scenarios = {
    "Subconjunto": ("azul amarelo", "azul amarelo verde roxo"),          # A ⊆ B
    "Superconjunto": ("azul amarelo verde roxo", "azul amarelo"),        # A ⊇ B
    "Igualdade": ("azul amarelo", "amarelo azul"),                       # A = B
    "Disjunto": ("gato cachorro", "vermelho azul"),                      # A ∩ B = ∅
}

# ---------------------------------
# Helpers de formatação e cor
# ---------------------------------
def build_sets(textA: str, textB: str):
    s1 = set(textA.lower().split())
    s2 = set(textB.lower().split())
    intersec = s1 & s2
    only_s1 = s1 - s2
    only_s2 = s2 - s1
    return s1, s2, intersec, only_s1, only_s2

def make_colorizer(intersec, only_s1, only_s2):
    def colorize(word: str) -> str:
        if word in intersec:
            return f"[bold green]{word}[/bold green]"   # comum
        if word in only_s1:
            return f"[red]{word}[/red]"                 # só em A
        if word in only_s2:
            return f"[yellow]{word}[/yellow]"           # só em B
        return word
    return colorize

def format_set(words, colorize):
    return "{ " + ", ".join(colorize(w) for w in sorted(words)) + " }"

# ---------------------------------
# Monta a tabela (cada linha usa seu próprio par A,B)
# ---------------------------------
table = Table(title="Comparação de Conjuntos (Cenários por Relação)", show_lines=True)
table.add_column("Relação", style="bold magenta")
table.add_column("Conjunto A", style="cyan")
table.add_column("Conjunto B", style="cyan")
table.add_column("Resultado", justify="center", style="bold")

for relation, (textA, textB) in scenarios.items():
    s1, s2, intersec, only_s1, only_s2 = build_sets(textA, textB)
    colorize = make_colorizer(intersec, only_s1, only_s2)
    s1_fmt = format_set(s1, colorize)
    s2_fmt = format_set(s2, colorize)

    # Decide o booleano conforme a relação
    if relation == "Subconjunto":
        result = s1.issubset(s2)
    elif relation == "Superconjunto":
        result = s1.issuperset(s2)
    elif relation == "Igualdade":
        result = (s1 == s2)
    elif relation == "Disjunto":
        result = s1.isdisjoint(s2)
    else:
        result = False  # fallback

    emoji = "✔️" if result else "❌"
    table.add_row(
        relation,
        s1_fmt,
        s2_fmt,
        f"[green]{emoji}[/green]" if result else f"[red]{emoji}[/red]"
    )

console.print(table)

# Legenda
console.print("\n[bold underline]Legenda:[/bold underline]")
console.print(f"[bold green]verde[/bold green] = elemento em comum (A ∩ B)")
console.print(f"[red]vermelho[/red] = elemento só em A (A - B)")
console.print(f"[yellow]amarelo[/yellow] = elemento só em B (B - A)")

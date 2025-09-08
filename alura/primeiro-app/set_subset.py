# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "rich",
# ]
# ///
from rich.console import Console

console = Console()

text1 = 'azul amarelo'
text2 = 'azul amarelo verde roxo'

s1 = set(text1.lower().split())
s2 = set(text2.lower().split())

# Palavras em comum e diferenças
intersec = s1 & s2
only_s1 = s1 - s2
only_s2 = s2 - s1

# --- Funções para colorir ---
def colorize_subset(word):
    if word in intersec:
        return f"[bold green]{word}[/bold green]"
    elif word in only_s1:
        return f"[red]{word}[/red]"
    else:
        return f"[white]{word}[/white]"

def colorize_superset(word):
    if word in intersec:
        return f"[bold cyan]{word}[/bold cyan]"
    elif word in only_s2:
        return f"[yellow]{word}[/yellow]"
    else:
        return f"[white]{word}[/white]"

def colorize_equal(word):
    return f"[bold green]{word}[/bold green]" if word in intersec else f"[red]{word}[/red]"

def colorize_disjoint(word, other_set):
    return f"[red]{word}[/red]" if word in other_set else f"[white]{word}[/white]"

# --- Função auxiliar para montar conjuntos coloridos ---
def format_set(s, color_func, other_set=None):
    return "{ " + ", ".join(
        color_func(w) if other_set is None else color_func(w, other_set)
        for w in s
    ) + " }"

# --- Operações ---
subset = s1.issubset(s2)
superset = s1.issuperset(s2)
equal = s1 == s2
disjoint = s1.isdisjoint(s2)

# --- Impressão com prova visual ---
console.print("\n[bold underline]Resultados:[/bold underline]\n")

# Subconjunto
s1_col = format_set(s1, colorize_subset)
s2_col = format_set(s2, colorize_subset)
console.print(f"{s1_col} {'é' if subset else 'não é'} subconjunto de {s2_col}\n")

# Superconjunto
s1_col = format_set(s1, colorize_superset)
s2_col = format_set(s2, colorize_superset)
console.print(f"{s1_col} {'é' if superset else 'não é'} superconjunto de {s2_col}\n")

# Igualdade
s1_col = format_set(s1, colorize_equal)
s2_col = format_set(s2, colorize_equal)
console.print(f"{s1_col} e {s2_col} {'são' if equal else 'não são'} iguais\n")

# Disjunto
s1_col = format_set(s1, colorize_disjoint, s2)
s2_col = format_set(s2, colorize_disjoint, s1)
console.print(f"{s1_col} e {s2_col} {'são' if disjoint else 'não são'} disjuntos\n")

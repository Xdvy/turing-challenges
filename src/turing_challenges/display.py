from typing import Generator

# ------------------------
# Activation automatique de Rich
# ------------------------
try:
    from rich.console import Console
    from rich.table import Table
    from rich import box
    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False
    console = None

# ------------------------
# Fonctions d'affichage centralisées
# ------------------------
def print_challenges(challenges_state: dict):
    """
    Affiche la liste des challenges.
    Si rich est disponible et full=True, utilise un tableau coloré.
    """
    
    if RICH_AVAILABLE :
        # A modifier en fonction de la valeur de solved
        table = Table(title="Turing Challenges", box=box.ROUNDED)
        table.add_column("Numéro", justify="right", style="cyan")
        table.add_column("État", style="yellow")
        table.add_column("Titre", style="green")
        for num, (title,solved) in sorted(challenges_state.items()):
            table.add_row(f"{num}", f"{title}")
        console.print(table, justify="center")
    else:
        for num, (title,solved) in sorted(challenges_state.items()):
            state = "Résolu" if solved else "Non Résolu"
            print(f"{num} – {state} : {title}")


def print_result(result):
    """Affiche le résultat d’un challenge, avec ou sans rich"""
    if RICH_AVAILABLE:
        console.print(f"[bold green]Résultat :[/bold green] {result}")
    else:
        print(f"Résultat : {result}")


def print_error(msg: str):
    """Affiche un message d'erreur"""
    if RICH_AVAILABLE:
        console.print(f"[bold red]{msg}[/bold red]")
    else:
        print(f"{msg}")
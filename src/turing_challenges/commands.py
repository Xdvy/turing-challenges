from . import runner
from . import display
from .discovery import discover_challenges
from .registry import get_challenge_title, get_challenge_states
from .loader import get_challenge_readme


def handle_list():
    discovered = discover_challenges()
    states = get_challenge_states(discovered)
    display.print_challenges(states)


def handle_info(n: int):
    discovered = discover_challenges()
    if n not in discovered:
        title = get_challenge_title(n)
        display.print_error(
            f"Le challenge {n} ({title}) n'est pas encore résolu."
        )
        return

    readme = get_challenge_readme(n)
    print(readme)


def handle_solve(n: int, **kwargs):
    discovered = discover_challenges()
    if n not in discovered:
        title = get_challenge_title(n)
        display.print_error(
            f"Le challenge {n} ({title}) n'est pas encore résolu."
        )
        return
    result = runner.solve(n, **kwargs)
    display.print_result(result)

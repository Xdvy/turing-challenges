import pkgutil
import turing_challenges

def discover_challenges() -> list[int]:
    """Découvre dynamiquement tous les challenges présents dans le package."""
    discovered = []

    for _, name, _ in pkgutil.iter_modules(turing_challenges.__path__):
        if name.startswith("challenge_"):
            discovered.append(int(name.split("_")[1]))

    return sorted(discovered)

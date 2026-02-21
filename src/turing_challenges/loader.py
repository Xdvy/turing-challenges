import importlib
from importlib import resources
from .errors import ChallengeNotFoundError


def load_build_parser(n: int):
    """Construit le parser du challenge n si disponible."""

    module_name = f"turing_challenges.challenge_{n:03d}.cli"

    try:
        module = importlib.import_module(module_name)
        return module.build_parser
    except ModuleNotFoundError as e :
        raise ChallengeNotFoundError(n) from e


def get_challenge_readme(n: int) -> str:
    """Renvoie l'énoncé du challenge n si disponible"""

    module_name = f"turing_challenges.challenge_{n:03d}"

    try:
        package = importlib.import_module(module_name)
    except ModuleNotFoundError as e:
        raise ChallengeNotFoundError(n) from e

    try:
        return (
            resources.files(package)
            .joinpath("README.md")
            .read_text(encoding="utf-8")
        )
    except FileNotFoundError:
        return "Aucun README disponible."

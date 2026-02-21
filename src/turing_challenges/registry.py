import json
from pathlib import Path
from .errors import JSONNotFoundError, ChallengeNotInListError


_BASE_PATH = Path(__file__).parent
_TITLES_PATH = _BASE_PATH / "challenge_titles.json"


def get_all_titles() -> dict[str, str]:
    """Récupère les titre des challenges"""
    try :
        with open(_TITLES_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError as e :
        raise JSONNotFoundError(_TITLES_PATH) from e
        


def get_challenge_title(n: int) -> str:
    """Récupère le titre du challenge numéro n si disponible"""
    titles = get_all_titles()
    key = str(n)

    try :
        return titles[key]
    except KeyError as e :
        raise ChallengeNotInListError(n,(min(titles),max(titles))) from e


def get_challenge_states(discovered: list[int]) -> dict[int, tuple[str, bool]]:
    """
    Récupère le numéro,le titre et l'état de chaque challenge (implémenté ou non).
    """
    titles = get_all_titles()

    return {
        int(num): (title, int(num) in discovered)
        for num, title in titles.items()
    }

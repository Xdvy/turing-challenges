class ChallengeNotFoundError(Exception):
    """Erreur lorsque le dossier n'est pas bien nommé."""
    def __init__(self, challenge_number: int):
        self.challenge_number = challenge_number
        super().__init__(self._build_message())

    def _build_message(self) -> str:
        return (
            f"Challenge {self.challenge_number} introuvable "
            f"(nom de dossier attendu: challenge_{self.challenge_number:03d})"
        )

class ChallengeNotInListError(Exception):
    """Erreur lorsque l'indice n'existe pas dans le JSON"""
    def __init__(self, challenge_number: int, challenge_range: tuple[int,int] = None):
        self.challenge_number = challenge_number
        self.challenge_range = challenge_range
        super().__init__(self._build_message())

    def _build_message(self) -> str:
        if self.challenge_range is not None :
            return (
                f"Le challenge {self.challenge_number} n'existe pas dans la base de donnée. "
                f"Challenges valides : {self.challenge_range[0]} à {self.challenge_range[1]}"
            )
        else :
            return (
                f"Le challenge {self.challenge_number} n'existe pas dans la base de donnée. "  
            )

class JSONNotFoundError(Exception):
    """Erreur lorsque le fichier JSON n'est pas trouvé."""
    def __init__(self, _TITLES_PATH: int):
        self._TITLES_PATH = _TITLES_PATH
        super().__init__(self._build_message())

    def _build_message(self) -> str:
        return (
            f"JSON introuvable "
            f"(PATH attendu: {self._TITLES_PATH})"
        )


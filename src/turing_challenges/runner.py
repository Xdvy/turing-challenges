# src/turing_challenges/runner.py
import importlib
from .errors import ChallengeNotFoundError

_cached_challenges = {}

def solve(challenge_number: int, *args, **kwargs):
    """Execute a challenge by its number lazily, with caching."""

    # Return from cache if already imported.
    if challenge_number in _cached_challenges:
        challenge_class = _cached_challenges[challenge_number]
    else:
        module_name = f"turing_challenges.challenge_{challenge_number:03d}.challenge"
        class_name = f"Challenge{challenge_number:03d}"

        try:
            module = importlib.import_module(module_name)
            challenge_class = getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ChallengeNotFoundError(challenge_number) from e

        _cached_challenges[challenge_number] = challenge_class

    return challenge_class().solve(*args, **kwargs)

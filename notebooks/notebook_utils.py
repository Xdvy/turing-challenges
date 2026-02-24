import importlib
import time
from turing_challenges.errors import ChallengeNotFoundError
from turing_challenges.loader import get_challenge_readme
from turing_challenges import solve


def get_kwargs(n) -> dict:
  """Renvoie les valeurs par défaut des arguments du challenge n"""

  module_name = f"turing_challenges.challenge_{n:03d}.cli"

  try:
      package = importlib.import_module(module_name)
  except ModuleNotFoundError as e:
      raise ChallengeNotFoundError(n) from e

  try:
      return vars(package.build_parser().parse_args([]))
  except NameError:
      return "Aucun argument par défaut disponible."
  
  
def solve_challenge(n: int, *args, **kwargs) :
  if not(args or kwargs) :
    kwargs = get_kwargs(n)

  start_time = time.time()
  result = solve(n,*args,**kwargs)
  total_time = time.time() - start_time

  print(get_challenge_readme(n))
  print("-----------")
  print(f"Résultat : {solve(n,*args,**kwargs)}")
  print(f"Temps d'exécution : {round(total_time,3)}s")
  

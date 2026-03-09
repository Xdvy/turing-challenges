# test/challenge_001/test_cli.py

import pytest
from turing_challenges.challenge_001.cli import build_parser, run, main

# -------------------
# Tests erreurs build_parser
# -------------------

@pytest.mark.parametrize("cli_args,res", [
    ([],2013),
    (["--max_value", "100"],100)
])

def test_build_parser_default_and_valid_value(cli_args, res):
    parser = build_parser()
    args = parser.parse_args(cli_args)

    assert args.max_value == res


@pytest.mark.parametrize(
    "args",
    [
        ["--max_value", "abc"],     # string
        ["--max_value", "1.5"],     # float
        ["--max_value"],            # argument manquant
        ["--unknown", "10"]         # argument inconnu
    ],
)
def test_build_parser_invalid_type(args):
    parser = build_parser()

    with pytest.raises(SystemExit) as exc:
        parser.parse_args(args)
    
    assert exc.value.code == 2

# -------------------
# Tests erreurs run - test solve en réalité
# -------------------
max_value,res = (20,51)
def test_run_lower_than_20(max_value=max_value) :
    assert run(max_value) == res

# -------------------
# Tests erreurs main
# -------------------

def test_main_flow(capsys):

    def fake_runner(x):
        return 51

    main(["--max_value", "20"],runner=fake_runner)

    assert capsys.readouterr().out.strip() == "51"
# challenge_001/cli.py
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Trouver la somme de tous les multiples de 5 ou de 7 inférieurs à max_value.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--max_value", type=int, default=2013, help="Valeur maximale")

    return parser

def run(max_value: int) -> int:
    from .challenge import Challenge001
    return Challenge001().solve(max_value)

def main(argv=None, runner=run):
    parser = build_parser()
    args = parser.parse_args(argv)

    result = runner(args.max_value)
    print(result)


if __name__ == "__main__":
    main()
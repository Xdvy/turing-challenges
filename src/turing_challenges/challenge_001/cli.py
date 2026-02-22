# challenge_001/cli.py
import argparse

def build_parser():
    parser = argparse.ArgumentParser(description="Trouver la somme de tous les multiples de 5 ou de 7 inférieurs à max_value.",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--max_value", type=int, default=2013, help="Valeur maximale")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()

    # appel direct à la logique
    from .challenge import Challenge001
    result = Challenge001().solve(args.max_value)
    print(result)


if __name__ == "__main__":
    main()
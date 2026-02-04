#!/usr/bin/env python3

import sys
import argparse

def compute_sum(n: int) -> int:
    '''
    Compute the sum of every digit of n.
    
    :param n: Integer
    :return: Sum of the digits
    '''
    return sum(int(i) for i in str(n))


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the sum of digits of 2**x."
    )

    parser.add_argument(
        "x",
        type=int,
        help="Exponent x",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display the value of 2**x",
    )

    args = parser.parse_args(argv)

    n = pow(2,args.x)

    if args.verbose: 
        if n < 10**10:
            print(n)
        else:
            print(f"n has {len(str(n))} digits - too big to display")

    digit_sum = compute_sum(n)

    print(digit_sum)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import sys
import argparse
from xdvyturing.utils import largest_prime_divisor

#def largest_prime_divisor(n, verbose=False):
#    '''
#    Compute the largest prime divider of a number.
#    
#    :param n: number to divide
#    '''
#    from math import sqrt
#    lprime = [] if verbose else None
#
#    for i in range(2, int(sqrt(n))+1):
#        while n % i == 0:
#            if verbose : lprime.append(i)
#            n //= i
#            if n == 1:
#                return lprime, i
#    if verbose : lprime.append(n)
#    return lprime, n

def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the largest prime divisor of a number."
    )

    parser.add_argument(
        "n",
        type=int,
        help="Integer value (must be >= 2)",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display all prime factors",
    )

    args = parser.parse_args(argv)

    try:
        factors, largest = largest_prime_divisor(args.n, collect=args.verbose)

    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    if factors is not None:
        print(factors)

    print(largest)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
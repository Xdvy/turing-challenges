#!/usr/bin/env python3

import sys
import argparse
from typing import Iterator

from xdvyturing.utils import positive_int

def sum_primes_up_to(n: int) -> int:
    '''
    Sum the prime numbers below or equal to n 
    '''
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))

    return sum(i for i, is_prime in enumerate(sieve) if is_prime)


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the sum of prime numbers below or equal to n."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="Upper bound to sum prime numbers",
    )

    ### Extract parameters
    args = parser.parse_args(argv)

    n = args.n

    print(sum_primes_up_to(n))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
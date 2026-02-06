#!/usr/bin/env python3

import sys
import argparse
from xdvyturing.utils import is_prime, positive_int

def get_nth_prime(n: int) -> int:
    '''
    Compute the nth prime number.
    
    :param n: integer
    '''
    if n < 1:
        raise ValueError("n must be >= 1")

    count = 0
    i = 1
    while count < n:
        i += 1
        if is_prime(i):
            count += 1
    return i


def collect_primes_up_to_nth(n: int) -> list[int]:
    '''
    Collect primes up to the nth prime number.
    
    :param n: index of wanted prime number
    :type n: int
    :return: list of the n first prime numbers 
    :rtype: list[int]
    '''

    if n < 1:
        raise ValueError("n must be >= 1")
    
    primes = []
    i = 1
    while len(primes) < n:
        i += 1
        if is_prime(i):
            primes.append(i)
    return primes


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the nth prime number."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="Integer n",
    )

    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Allow calculation above Python's safe limit (up to 8000). May consume large memory.",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display the first n prime numbers",
    )

    ### Extract parameters
    args = parser.parse_args(argv)

    # Upper bound on n to prevent excessive CPU usage.
    # The current primality test is O(sqrt(p)), so large n may lead to long runtimes.
    ABSOLUTE_MAX_N = 100000
    DEFAULT_MAX_N= 50000

    n = args.n
    
    if n > ABSOLUTE_MAX_N :
        print(
            f"Error: requested computation exceeds hard safety limits.",
            file=sys.stderr
        )
        return 3
    
    if n > DEFAULT_MAX_N and not args.force:
        print(
            f"Error: {n} exceeds the safe limit ({DEFAULT_MAX_N}). Use --force to override.",
            file=sys.stderr
        )
        return 2
    
    if args.force:
        print(f"Warning: The current primality test is O(sqrt(p)), so large n may lead to long runtimes.", file=sys.stderr)

    try :
        primes = collect_primes_up_to_nth(n) if args.verbose else None
        prime = primes[-1] if primes else get_nth_prime(n)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2
    

    if primes :
        n_prime = len(primes)
        if n_prime > 10 : 
            print(f"{n_prime} prime numbers below {prime} - too big to display")
        else :
            print(primes)

    
    print(prime)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
#!/usr/bin/env python3

import sys
import argparse
from typing import Iterator

from xdvyturing.utils import positive_int

def generate_pythagorean_triplet(n: int, err=10e-4) -> Iterator[tuple[int, int, int]] :
    '''
    Yield pythagorician triplets (a, b, c) such that a^2+b^2=c^2 and a + b + c = n. 
    
    :param n: Value of the sum of integers
    :type n: int
    :return: generator
    '''
    if n < 1 :
        raise ValueError("n must be >= 1")
    
    max_value = int(n/2)+1

    for a in range(1, n // 3) :
        for b in range(a+1, (n - a) // 2) :
            c = n - a - b
            if a*a + b*b == c*c:
                yield (a, b, c)


def get_biggest_pythagorean(n: int) -> tuple[int,int]:
    '''
    Compute the biggest phytagorean triplet
    
    :param n: Description
    :type n: int
    '''

    if n < 1 :
        raise ValueError("n must be >= 1")
    
    biggest_triplet = None
    biggest_value = 0

    for (a,b,c) in generate_pythagorean_triplet(n) :
        if biggest_value==0 or biggest_value < a*b*c :
            biggest_triplet = (a,b,c)
            biggest_value = a*b*c

    return biggest_triplet, biggest_value


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the product of the biggest pythagorician triplet with a+b+c=n."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="value of the sum a+b+c",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display the triplet corresponding to the maximum a*b*c value",
    )

    ### Extract parameters
    args = parser.parse_args(argv)

    n = args.n


    biggest_triplet, biggest_value = get_biggest_pythagorean(n)
    
    if args.verbose :
        print(biggest_triplet)

    print(biggest_value)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
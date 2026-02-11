#!/usr/bin/env python3

import sys
import argparse
import math
from typing import Iterator, Tuple

from xdvyturing.utils import positive_int


def get_nth_triangular(n: int) -> int:
    '''
    Compute the value of the nth triangular number
    '''
    return sum(i for i in range(n+1))


def generate_dividers(n: int) -> Iterator[Tuple[int,int]]:
    '''
    Docstring pour get_dividers
    
    :param n: Description
    :type n: int
    :return: Description
    :rtype: Iterator[int]
    '''

    for i in range(1,math.isqrt(n)+1) :
        if n%i==0 :
            yield i, n//i


def get_dividers(n: int) -> list :
    '''
    Docstring pour get_dividers
    
    :param n: Description
    :type n: int
    :return: Description
    :rtype: list
    '''

    dividers_list = [x for y in generate_dividers(n) for x in y]

    if math.sqrt(n) == math.isqrt(n) :
        dividers_list.remove(math.isqrt(n))

    return dividers_list


def get_num_dividers(n: int):
    '''
    Docstring pour get_num_dividers
    
    :param n: Description
    :type n: int
    :param collect: Description
    '''

    n_dividers = sum(2 for _ in generate_dividers(n))

    if math.sqrt(n) == math.isqrt(n) :
        n_dividers -=1

    return n_dividers


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the first triangular number with at least n dividers."
    )

    parser.add_argument(
        "n",
        type=positive_int,
        help="number of dividers to get",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display the dividers",
    )

    ### Extract parameters
    args = parser.parse_args(argv)
    n = args.n

    k = 0
    while get_num_dividers(get_nth_triangular(k)) < n :
        k += 1

    result = get_nth_triangular(k)
    if args.verbose :
        dividers_list = get_dividers(result)
        print(dividers_list)
        print(result)
        return 0
    else :
        print(result)

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
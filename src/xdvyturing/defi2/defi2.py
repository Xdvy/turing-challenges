#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import sys
import argparse

def sum_odd_fibonacci(max_value, verbose=False):
    a, b = 1, 1
    total = 0
    values = [] if verbose else None

    while a < max_value:
        if a % 2 != 0:
            total += a
        if values is not None :
            values.append(a)
        a, b = b, a + b

    return values, total

def main(argv=None) :
    """Main function"""

    parser = argparse.ArgumentParser(
        description="Return the sum of odd numbers below n in Fibonacci sequence ."
    )

    parser.add_argument(
        dest="maxValue",
        type=int,
        help="Maximum value of integers to sum",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="verbose",
        default=False,
        action="store_true",
        help="display list of integers",
    )

    args = parser.parse_args(argv)

    values, fiboOddSum = sum_odd_fibonacci(args.maxValue, args.verbose)
    if values is not None : print(values)
    print(fiboOddSum)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
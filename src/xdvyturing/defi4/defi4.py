#!/usr/bin/env python3

import sys
import argparse

def compute_products(len_x,len_y) :
    '''
    Define the generator to get all combination of numbers with len_x and len_y characters.
    
    :param len_x: length of the first number
    :param len_y: length of the second number
    '''

    lower_x = 10 ** (len_x - 1)
    upper_x = 10 ** len_x

    lower_y = 10 ** (len_y - 1)
    upper_y = 10 ** len_y

    for y in range(upper_y - 1, lower_y - 1, -1):
        for x in range(upper_x - 1, lower_x - 1, -1):
            yield x * y

   
def biggest_palindrome(len_x,len_y, collect=False):
    '''
    Docstring pour biggest_palindrome
    
    :param len_x: length of the first number
    :param len_y: length of the second number
    :param verbose: Get the list of palindromes.
    '''
    max_pal = 0
    palindromes = set() if collect else None

    for n in compute_products(len_x, len_y):
        if n <= max_pal:
            continue

        s = str(n)
        if s == s[::-1]:
            max_pal = n
            if palindromes is not None:
                palindromes.add(n)

    if palindromes is not None:
        palindromes = sorted(palindromes)

    return palindromes, max_pal


def main(argv=None):
    """CLI entry point"""

    parser = argparse.ArgumentParser(
        description="Return the largest palindrome obtained with two numbers of length x and y."
    )

    parser.add_argument(
        "length",
        nargs = '*',
        help="Length of x and y numbers (two values needed, they must be >= 1)",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="display all palindromes",
    )

    args = parser.parse_args(argv)

    if len(args.length) != 2:
        parser.error("Exactly two integer values are required")

    try:
        len_x, len_y = map(int, args.length)
    except ValueError:
        parser.error("Lengths must be integers")

    if len_x < 1 or len_y < 1:
        parser.error("Lengths must be >= 1")

    
    lPalindromes, max_palindrome = biggest_palindrome(len_x,len_y, collect=args.verbose)

    if lPalindromes is not None:
        print(lPalindromes)

    print(max_palindrome)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user", file=sys.stderr)
        sys.exit(130)
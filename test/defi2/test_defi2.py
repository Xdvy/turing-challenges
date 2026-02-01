#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import pytest
from xdvyturing.defi2.defi2 import sum_odd_fibonacci, main

# =========================================================
# Tests unitaires de sum_odd_fibonacci
# =========================================================

def test_sum_odd_fibonacci_basic():
    values, total = sum_odd_fibonacci(10, verbose=False)

    # Fibonacci < 10 : 1, 1, 2, 3, 5, 8
    # Impairs        : 1, 1, 3, 5  → somme = 10
    assert values is None
    assert total == 10


def test_sum_odd_fibonacci_verbose():
    values, total = sum_odd_fibonacci(10, verbose=True)

    assert values == [1, 1, 2, 3, 5, 8]
    assert total == 10


def test_sum_odd_fibonacci_zero():
    values, total = sum_odd_fibonacci(0, verbose=True)

    assert values == []
    assert total == 0


def test_sum_odd_fibonacci_one():
    values, total = sum_odd_fibonacci(1, verbose=True)

    assert values == []
    assert total == 0


def test_sum_odd_fibonacci_two():
    values, total = sum_odd_fibonacci(2, verbose=True)

    assert values == [1, 1]
    assert total == 2


def test_no_list_created_when_not_verbose():
    values, total = sum_odd_fibonacci(100, verbose=False)

    assert values is None
    assert total > 0


# =========================================================
# Tests du CLI (argparse + print)
# =========================================================

def test_cli_without_verbose(capsys):
    main(["10"])

    captured = capsys.readouterr()
    # Une seule ligne : la somme
    assert captured.out.strip() == "10"


def test_cli_with_verbose(capsys):
    main(["10", "--verbose"])

    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines[0] == "[1, 1, 2, 3, 5, 8]"
    assert lines[1] == "10"


def test_cli_zero(capsys):
    main(["0", "--verbose"])

    captured = capsys.readouterr()
    lines = captured.out.strip().splitlines()

    assert lines[0] == "[]"
    assert lines[1] == "0"


# =========================================================
# Tests de robustesse
# =========================================================

def test_large_value_does_not_crash():
    values, total = sum_odd_fibonacci(4_000_000, verbose=False)

    assert values is None
    assert total > 0
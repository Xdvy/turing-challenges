#!/usr/bin/env python3
# -*- coding: iso-8859-1 -*-

import argparse

def positive_int(value: str) -> int:
    ivalue = int(value)
    if ivalue < 1:
        raise argparse.ArgumentTypeError("n must be a positive integer")
    return ivalue
#!/usr/bin/env python -O
# -*- coding: utf-8 -*-
#from __future__ import print_function, unicode_literals, with_statement, division, absolute_import

import sys


def main():
    if sys.stdin.isatty():
        with open(sys.argv[1]) as fin:
            data = fin.read()
    else:
        # pipe
        data = sys.stdin.read()
    return 0


if __name__ == '__main__':
    sys.exit(main())

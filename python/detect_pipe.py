#!/usr/bin/env python -O
# -*- coding: utf-8 -*-
#from __future__ import print_function, unicode_literals, with_statement, division, absolute_import

import sys


def main():
    if sys.stdin.isatty():
        fin = open(sys.argv[1])
    else:
        # pipe
        fin = sys.stdin

    with fin:
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())

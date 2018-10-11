#!/usr/bin/env python -O
# -*- coding: utf-8 -*-
import yaml


def main():
    yaml.dump({}, default_flow_style=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())

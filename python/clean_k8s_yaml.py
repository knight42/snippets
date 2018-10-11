#!/usr/bin/env python -O
# -*- coding: utf-8 -*-

import yaml
import sys


def delete_key(d, *keys):
    for key in keys:
        if d.get(key) is not None:
            del d[key]


def main():
    if sys.stdin.isatty():
        with open(sys.argv[1]) as fin:
            content = fin.read()
    else:
        content = sys.stdin.read()

    data = yaml.load(content)

    delete_key(data, 'status')
    if data.get('metadata'):
        meta = data['metadata']
        delete_key(meta, 'generation', 'resourceVersion', 'uid',
                   'creationTimestamp', 'selfLink')
        if meta.get('annotations'):
            delete_key(meta['annotations'],
                       'kubectl.kubernetes.io/last-applied-configuration')

    yaml.dump(data, sys.stdout, default_flow_style=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/bin/bash

main() {
    echo -e '# snippets\n'

    for d in */; do
        echo "* ${d%/}"
        for f in $(ls -A $d); do
            echo "    * [$f]($d$f)"
        done
    done
}

main > README.md

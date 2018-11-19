#!/bin/bash

set -euo pipefail

if [[ $(id -u) -ne 0 ]]; then
    sudo "$0" "$@"
    exit $?
fi

main() {
    :
}

main "$@"

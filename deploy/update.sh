#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR >/dev/null
git pull --rebase
# this will reload the wsgi daemon
touch ../code.py
popd >/dev/null

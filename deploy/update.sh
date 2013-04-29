#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR >/dev/null
git pull --rebase
# ^ that should do it since the commit we are rebasing changes code.py
# just in case, this will reload the wsgi daemon
touch ../code.py
popd >/dev/null

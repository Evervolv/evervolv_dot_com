#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

pushd $DIR >/dev/null
git am 0001-apache-changes.patch
popd >/dev/null

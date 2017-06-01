#!/usr/bin/env bash
set -e

# Save arguments
SV_NAME=$1
SV_VERSION=$2
SV_RELEASE=$3

BASESPECFILES=/tmp/basespecfiles

#TODO cd to helmod base
module purge
source ./setup.sh

# Restore our original arguments
export NAME=$SV_NAME
export VERSION=$SV_VERSION
export RELEASE=$SV_RELEASE
export TYPE=Core

cd "$FASRCSW_DEV"/rpmbuild/SPECS

cp $BASESPECFILES/$NAME.spec "$NAME-$VERSION-fasrc$RELEASE.spec"

make
make install

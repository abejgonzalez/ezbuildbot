#!/bin/bash
# Snippet sourced in order to set some default variables.
# See README.md for documentation about these variables.

# ${VAR+x} is to detect unset variables.
# See https://stackoverflow.com/a/13864829

if [ -z "${PROJ_PREFIX+x}" ]; then
    export PROJ_PREFIX=myproject
fi

if [ -z "${SQLITE_FILE+x}" ]; then
    export SQLITE_FILE="${PWD}/state.sqlite"
fi

if [ -z "${BUILDBOT_ADMIN_PORT+x}" ]; then
    export BUILDBOT_ADMIN_PORT=8020
fi

if [ -z "${BUILDBOT_COMMS_PORT+x}" ]; then
    export BUILDBOT_COMMS_PORT=9989
fi

if [ -z "${BUILDBOT_HASH+x}" ]; then
    export BUILDBOT_HASH=ec38d8f7bbffa4fc792d5bb6466c336015131197
fi

if [ -z "${BUILDBOT_CONFIG+x}" ]; then
    export BUILDBOT_CONFIG="sample-master.cfg"
fi

if [ -z "${BUILD_TEMPDIR+x}" ]; then
    export BUILD_TEMPDIR=tmp
fi
mkdir -p $BUILD_TEMPDIR

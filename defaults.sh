#!/bin/bash
# Snippet sourced in order to set some default variables.
# See README.md for documentation about these variables.

# Script dir (folder this script resides in)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ${VAR+x} is to detect unset variables.
# See https://stackoverflow.com/a/13864829

if [ -z "${PROJ_PREFIX+x}" ]; then
    export PROJ_PREFIX=chipyard
fi

if [ -z "${EZBB_WORKDIR+x}" ]; then
    # By default this is the script dir (folder this script resides in)
    export EZBB_WORKDIR="$SCRIPT_DIR"
fi
mkdir -p $EZBB_WORKDIR

if [ -z "${SQLITE_FILE+x}" ]; then
    export SQLITE_FILE="${EZBB_WORKDIR}/state.sqlite"
fi

if [ -z "${BB_ADMIN_PORT+x}" ]; then
    export BB_ADMIN_PORT=8020
fi

if [ -z "${BB_COMMS_PORT+x}" ]; then
    export BB_COMMS_PORT=9989
fi

if [ -z "${BB_WORKER_SCRIPTS+x}" ]; then
    export BB_WORKER_SCRIPTS=""
fi

if [ -z "${BB_WORKER_DOCKERFRAG+x}" ]; then
    # Reading from /dev/null is equivalent to reading an empty file
    export BB_WORKER_DOCKERFRAG=/dev/null
fi

if [ -z "${BB_WORKER_LANG+x}" ]; then
    export BB_WORKER_LANG="C.UTF-8"
fi

if [ -z "${BB_HASH+x}" ]; then
    export BB_HASH=ec38d8
fi

if [ -z "${BB_SHARE_LOCAL_DIR+x}" ]; then
    export BB_SHARE_LOCAL_DIR="$SCRIPT_DIR/container-dir"
fi

if [ -z "${BB_SHARE_DOCKER_DIR+x}" ]; then
    export BB_SHARE_DOCKER_DIR="/var/log/container-data"
fi

if [ -z "${BB_SSH_PASSTHROUGH+x}" ]; then
    export BB_SSH_PASSTHROUGH=""
fi

if [ -z "${BUILD_TEMPDIR+x}" ]; then
    export BUILD_TEMPDIR="${SCRIPT_DIR}/tmp"
fi
mkdir -p $BUILD_TEMPDIR

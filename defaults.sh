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

if [ -z "${EZBUILDBOT_WORKDIR+x}" ]; then
    # By default this is the script dir (folder this script resides in)
    export EZBUILDBOT_WORKDIR="$SCRIPT_DIR"
fi
mkdir -p $EZBUILDBOT_WORKDIR

if [ -z "${SQLITE_FILE+x}" ]; then
    export SQLITE_FILE="${EZBUILDBOT_WORKDIR}/state.sqlite"
fi

if [ -z "${BUILDBOT_ADMIN_PORT+x}" ]; then
    export BUILDBOT_ADMIN_PORT=8020
fi

if [ -z "${BUILDBOT_COMMS_PORT+x}" ]; then
    export BUILDBOT_COMMS_PORT=9989
fi

if [ -z "${EZBUILDBOT_CONFIG+x}" ]; then
    export EZBUILDBOT_CONFIG="${SCRIPT_DIR}/chipyard-config.yml"
fi

if [ -z "${BUILDBOT_WORKER_SCRIPTS+x}" ]; then
    export BUILDBOT_WORKER_SCRIPTS=""
fi

if [ -z "${BUILDBOT_WORKER_DOCKERFRAG+x}" ]; then
    # Reading from /dev/null is equivalent to reading an empty file
    export BUILDBOT_WORKER_DOCKERFRAG=/dev/null
fi

if [ -z "${BUILDBOT_WORKER_LANG+x}" ]; then
    export BUILDBOT_WORKER_LANG="C.UTF-8"
fi

if [ -z "${BUILDBOT_HASH+x}" ]; then
    export BUILDBOT_HASH=ec38d8
fi

if [ -z "${BUILDBOT_SSH_PASSTHROUGH+x}" ]; then
    export BUILDBOT_SSH_PASSTHROUGH=""
fi

if [ -z "${BUILDBOT_CONFIG_TEMPLATE+x}" ]; then
    export BUILDBOT_CONFIG_TEMPLATE="${SCRIPT_DIR}/master-template.py"
fi

if [ -z "${BUILD_TEMPDIR+x}" ]; then
    export BUILD_TEMPDIR="${SCRIPT_DIR}/tmp"
fi
mkdir -p $BUILD_TEMPDIR

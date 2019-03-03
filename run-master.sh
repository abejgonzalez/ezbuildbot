#!/bin/bash
# Re-run the master instance from the master image.
set -ex
set -euo pipefail

source defaults.sh

# TODO(edwardw): parametrize this
# Make sure state.sqlite exists.
SQLITE_FILE="${PWD}/state.sqlite"
touch "$SQLITE_FILE"

# Terminate any previous running instance.
docker rm "${PROJ_PREFIX}-master-inst" --force || true

# Usage notes:
# -v a:b = binds host file a to container file b
# -p a:b = bind host port a to container port b
# -d = detach and run in background
docker run --name "${PROJ_PREFIX}-master-inst" -it \
  -v "${SQLITE_FILE}:/var/lib/buildbot/state.sqlite" \
  -p $BUILDBOT_ADMIN_PORT:$BUILDBOT_ADMIN_PORT \
  -p $BUILDBOT_COMMS_PORT:$BUILDBOT_COMMS_PORT \
  -d \
  "${PROJ_PREFIX}-master"

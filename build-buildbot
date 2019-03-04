#!/bin/bash
# Build the buildbot base images.
set -ex
set -euo pipefail

source defaults.sh

# Check out buildbot folder if not present
if [ ! -d "buildbot" ]; then
    git clone https://github.com/buildbot/buildbot.git buildbot
fi

# Check out desired hash
pushd buildbot
git reset --hard $BUILDBOT_HASH
popd

# Apply patches
pushd buildbot
git am -3 ../patches/*.patch
popd

# Build buildbot master image
pushd buildbot/master
docker build -t "${PROJ_PREFIX}-master-base" .
popd

# Build buildbot worker image
pushd buildbot/worker
docker build -t "${PROJ_PREFIX}-worker-base" -f Dockerfile.py3 .
popd

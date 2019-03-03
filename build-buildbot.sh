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

#!/bin/bash
# Rebuild the buildbot master image.
set -ex
set -euo pipefail

source defaults.sh

cp $(readlink -f $BUILDBOT_CONFIG) $BUILD_TEMPDIR/master.cfg
cat > $BUILD_TEMPDIR/Dockerfile.master <<EOF
FROM ${PROJ_PREFIX}-master-base

COPY master.cfg /var/lib/buildbot/master.cfg

# Run image (copied from parent Dockerfile)
WORKDIR /var/lib/buildbot
CMD ["dumb-init", "/usr/src/buildbot/docker/start_buildbot.sh"]

EOF

cd $BUILD_TEMPDIR
docker build -t "${PROJ_PREFIX}-master" -f Dockerfile.master .

#!/bin/bash
# Snippet sourced in order to set some default variables.

if [ -z "$PROJ_PREFIX" ]; then
    export PROJ_PREFIX=myproject
fi

if [ -z "$BUILDBOT_HASH" ]; then
    export BUILDBOT_HASH=ec38d8f7bbffa4fc792d5bb6466c336015131197
fi

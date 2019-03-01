Easy to set up Docker-based buildbot config.

Usage
=====

First ensure the following environment variables are set:
* `PROJ_PREFIX`: this sets the prefix for all the Docker images that are built. For example, if `PROJ_PREFIX` is set to `foobar`, images like `foobar-master-base`, `foobar-master` will be built.
* `BUILDBOT_HASH` (optional): set this to use a custom buildbot revision. Usually the default one is fine.

The following scripts build/set up various images and instances:
* `build-buildbot.sh`: Build the buildbot base images (required for other commands).

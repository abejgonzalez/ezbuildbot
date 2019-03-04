Easy to set up Docker-based buildbot config.

Usage
=====

First ensure the following environment variables are set:
* `PROJ_PREFIX`: this sets the prefix for all the Docker images that are built. For example, if `PROJ_PREFIX` is set to `foobar`, images like `foobar-master-base`, `foobar-master` will be built.
* `SQLITE_FILE`: path to the SQLite databased used to store state. Defauls to `state.sqlite`.
* `BUILDBOT_ADMIN_PORT`: buildbot web admin port. Defaults to 8020.
* `BUILDBOT_COMMS_PORT`: buildbot communication port used for communication between workers and the buildbot master. Defaults to 9989.
* `BUILDBOT_CONFIG`: this points to a `buildbot.cfg`/`master.cfg` file. You can use the `./generate_config` script to do so.
* `BUILDBOT_WORKER_DOCKERFRAG`: Dockerfile fragment that helps set up the worker image. Defaults to a blank file.
* `BUILDBOT_HASH` (optional): set this to use a custom buildbot revision. Usually the default one is fine.
* `BUILD_TEMPDIR` (optional): temporary folder used in the build, defaults to `tmp`.

The following scripts build/set up various images and instances:
* `build-buildbot.sh`: Build the buildbot base images (required for other commands).
* `start-master.sh`: Re-starts the master instance. Usually it is preferred to use this command after changing the configuration since it will rebuild the image (required for changes to take effect) before re-running it.
** `build-master.sh`: Re-builds the master image.
** `run-master.sh`: Re-run the master instance from the master image but does NOT rebuild the image.

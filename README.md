Easy to set up Docker-based buildbot config.

Requirements
============
On Ubuntu:

```
sudo apt-get install -y docker.io python3-pip
sudo -H pip3 install astor==0.7.1
```

Usage
=====

First ensure the following environment variables are set:
* `PROJ_PREFIX`: this sets the prefix for all the Docker images that are built. For example, if `PROJ_PREFIX` is set to `foobar`, images like `foobar-master-base`, `foobar-master` will be built.
* `EZBUILDBOT_WORKDIR`: working directory to put scratch files, clone the buildbot repo, etc. Defaults to the folder where ezbuildbot scripts reside.
* `SQLITE_FILE`: path to the SQLite databased used to store state. Defauls to `$EZBUILDBOT_WORKDIR/state.sqlite`.
* `BUILDBOT_ADMIN_PORT`: buildbot web admin port. Defaults to 8020.
* `BUILDBOT_COMMS_PORT`: buildbot communication port used for communication between workers and the buildbot master. Defaults to 9989.
* `EZBUILDBOT_CONFIG`: ezbuildbot YAML/JSON based configuration for buildbot.
* `BUILDBOT_WORKER_SCRIPTS`: Comma-delimited list of scripts to run when building the worker image. Defaults to blank.
* `BUILDBOT_WORKER_DOCKERFRAG`: Dockerfile fragment that helps set up the worker image. Defaults to a blank file.
* `BUILDBOT_CONFIG_TEMPLATE` (optional): this is a customized `master.cfg` file that will be automatically processed by `./generate_config`. If this needs to be set, it should be a copy of `master-template.py`.
* `BUILDBOT_SSH_PASSTHROUGH` (optional): if present, will bind the given folder to `~/.ssh` on the worker to test private repos.
* `BUILDBOT_WORKER_LANG` (optional): `$LANG` setting to use in the worker container. Required for some applications e.g. JVM to be able to read files properly. Defaults to `C.UTF-8`.
* `BUILDBOT_HASH` (optional): set this to use a custom buildbot revision. Usually the default one is fine.
* `BUILD_TEMPDIR` (optional): temporary folder used in the build, defaults to `$EZBUILDBOT_WORKDIR/tmp`.

The following scripts build/set up various images and instances:
* `build-buildbot`: Build the buildbot base images (required for other commands).
* `start-master`: Re-starts the master instance. Usually it is preferred to use this command after changing the configuration since it will rebuild the image (required for changes to take effect) before re-running it.
  * `build-master`: Re-builds the master image.
  * `run-master`: Re-run the master instance from the master image but does NOT rebuild the image.
* `start-worker`: Re-starts a worker instance. It takes two parameters, a worker name and password.
  * `build-worker`: Re-builds the worker image.
  * `run-worker`: Re-run a worker instance using parameters (see above).

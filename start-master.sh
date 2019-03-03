#!/bin/sh
# Start the master instance: rebuild the master image and run it.
set -ex
./build-master.sh
./run-master.sh

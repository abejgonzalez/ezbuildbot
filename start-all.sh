#!/bin/bash

./build-buildbot
./start-master
./start-worker chipyard-worker-1 password
./start-worker chipyard-worker-2 password
./start-worker chipyard-worker-3 password
./start-worker chipyard-worker-3 password

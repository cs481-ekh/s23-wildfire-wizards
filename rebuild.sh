#!/bin/bash
./clean.sh
git pull
./build.sh
./sample-data-import.sh
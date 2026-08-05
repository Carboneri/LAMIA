#!/bin/bash

# Force plain, sequential build output instead of BuildKit's interactive
# TUI, which corrupts the terminal on Git Bash for Windows
export BUILDKIT_PROGRESS=plain

# Build the base images from which are based the Dockerfiles
# then Startup all the containers at once
docker build --progress=plain -t hadoop-base docker/hadoop/hadoop-base && \
docker build --progress=plain -t hive-base docker/hive/hive-base && \
docker build --progress=plain -t spark-base docker/spark/spark-base && \
docker-compose up -d --build

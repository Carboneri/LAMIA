#!/bin/bash

# Force plain, sequential build output instead of BuildKit's interactive
# TUI, which corrupts the terminal on Git Bash for Windows
export BUILDKIT_PROGRESS=plain

# Startup all the containers at once
docker-compose up -d --build

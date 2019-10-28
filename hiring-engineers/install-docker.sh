#!/usr/bin/env bash

set -x

sudo apt-get update -y

sudo apt install -y docker.io

sudo systemctl start docker

sudo systemctl enable docker

sudo usermod -aG docker $USER

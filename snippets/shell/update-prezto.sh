#!/usr/bin/env bash

set -e

cd ~/.zprezto
git pull && git submodule update --init --recursive

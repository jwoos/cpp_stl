#!/usr/bin/env bash

# TODO allow taking parameters

browser-sync start --files "*.html, css/*.css, js/*.js" --server "." --no-notify

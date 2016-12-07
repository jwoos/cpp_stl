#!/usr/bin/env bash

for file in *.${1}; do
	mv ${file} `basename ${file}`.${2}
done

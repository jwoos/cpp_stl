#!/usr/bin/env sh

if [[ $# -lt 1 ]]; then
	python3 packages/pytest .
else
	python3 test_hash_map.py
fi

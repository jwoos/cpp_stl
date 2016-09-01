#!/usr/bin/env bash

for spec in "${@}"; do
	./${spec}
done

#!/usr/bin/env bash

# reroutes traffic from 80 to given port
# default port will be 8080

if [[ $# -ge 2 ]]; then
	echo 'Only one argument is taken'
	exit 1
elif [[ $# -eq 0 ]]; then
	port=$1
else
	port=8080
fi

sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports ${port}

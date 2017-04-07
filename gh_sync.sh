#!/usr/bin/env bash

END="\033[0m"
BLACK="\033[0;30m"
WHITE="\033[0;37m"
RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"

function printUsage() {
	echo 'USAGE:'
	echo -e "\t./gh_sync.sh <USERNAME> <TOKEN>"
	echo -e "\tUSERNAME: your GitHub username"
	echo -e "\tTOKEN: your token - if you don't have one generate one from https://github.com/settings/tokens"
}

function debug() {
	echo -e "${YELLOW}[DEBUG] $1${END}"
}

if [[ $# -ne 2 ]]; then
	echo -e "${RED}Illegal number of parameters\n${END}"
	printUsage
	exit 1
fi

USERNAME=$1
TOKEN=$2

GITHUB_BASE='https://api.github.com'
GITHUB_PER_PAGE=30

USER_FILE=$(mktemp)
if [[ "$DEBUG" == true ]]; then
	debug "${YELLOW}${USER_FILE}${END}"
fi

curl -s -u $USERNAME:$TOKEN $GITHUB_BASE/user > $USER_FILE

# User has lots of keys, it should be bigger than 8 if successful
if [[ $(less $USER_FILE | jq 'length' 2>/dev/null) -lt 8 ]]; then
	echo -e "${RED}Error fetching user${END}"
	echo 'Response: '
	cat $USER_FILE
	exit 1
fi

# Query user information and get total repository count (private + public) that are owned by $USERNAME
REPO_COUNT=$(less $USER_FILE | jq '.owned_private_repos , .public_repos' | paste -sd+ | bc)
if [[ "$DEBUG" == true ]]; then
	debug $REPO_COUNT
fi

REPO_FILE=$(mktemp)
if [[ "$DEBUG" == true ]]; then
	debug $REPO_FILE
fi

curl -s -H "Authorization: token ${TOKEN}" "${GITHUB_BASE}/user/repos?type=owner" > $REPO_FILE

# Check if in an array and has message
if [[ -z $(less $REPO_FILE | jq '.[] | .message' 2>/dev/null) ]]; then
	echo -e "${RED}Error fetching repositories${END}"
	echo 'Response: '
	cat $REPO_FILE
	exit 1
fi

URLS=$(less $REPO_FILE | jq '.[] | .clone_url')
if [[ "$DEBUG" == true ]]; then
	debug $URLS
fi

PATTERN="s/https:\/\/github.com\/${USERNAME}\/\([a-zA-Z0-9_-]\+\)\.git/\1/"

while read -r GH_URL; do
	if [[ "$DEBUG" == true ]]; then
		debug "Working on: ${GH_URL}"
	fi

	DIRECTORY=$(echo $GH_URL | sed $PATTERN)
	if [[ "$DEBUG" == true ]]; then
		debug "DIRECTORY: ${DIRECTORY}"
	fi

	continue

	if [[ -d ${DIRECTORY} ]]; then
		pushd ${DIRECTORY}

		BRANCH=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)

		git checkout master

		# if checkout errors while switching to master just fetch
		if [[ $? -ne 0 ]]; then
			git fetch
		else
			git pull origin master
			git checkout $BRANCH
		fi

		popd
	else
		git clone $1
	fi
done <<< "$URLS"

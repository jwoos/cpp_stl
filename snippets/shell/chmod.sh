#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo $GREEN
echo '         | owner | group | other'
echo '   none  |   0   |   0   |   0  '
echo '   read  |   4   |   4   |   4  '
echo '  write  |   2   |   2   |   2  '
echo ' execute |   1   |   1   |   1  '
echo $NC

if [ $# -lt 3 ]
then
  echo $RED
  echo 'sh chmod.sh <owner> <group> <other>'
  echo $NC
  exit 1
else
  pwd
fi

owner=$1
group=$2
other=$3

for file in *
do
  if test -f "$file"
  then
    chmod ${1}${2}${3} $file
  else
    echo $RED
    echo 'Error, directory seems to be empty'
    echo $NC
  fi
done

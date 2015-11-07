#!/bin/bash
#set -x
if [ "$#" -ne 1 ];then
    echo "This script takes 1 argument"
    echo "OS"
    echo "./run.sh centos6"
    exit 1
fi
OS=$1
if [ -f "Dockerfile" ]; then
  rm -f Dockerfile
fi
cp ${OS}Dockerfile Dockerfile
docker build -t="rpmbuild:${OS}" .

#!/bin/bash
#set -x
if [ "$#" -ne 2 ];then
    echo "This script takes 2 arguments"
    echo "OS, and then rpm"
    echo "./run.sh centos6 tmux"
    exit 1
fi
OS=$1
RPM=$2
docker run -ti -v ${GOPATH}:/usr/src/go -v $(pwd)/rpmbuild:/root/rpmbuild:z rpmbuild:${OS} ${RPM}

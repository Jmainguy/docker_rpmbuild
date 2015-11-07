#!/bin/bash
#set -x
SPEC=$1
chown -R root:root /root/rpmbuild
chmod -R 777 /root/rpmbuild
/usr/bin/rpmbuild -ba /root/rpmbuild/SPECS/${SPEC}.spec

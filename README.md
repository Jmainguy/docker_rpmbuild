# docker_rpmbuild
A docker setup for building rpms across multiple OS's.
## run.sh
```./run.sh centos6 zookeeper``` to build a zookeeper rpm on centos6
### dockerbuild/build.sh
```./build.sh centos6``` to build a fresh centos6 image.
#### How to
Simply add your rpm.spec to rpmbuild/SPECS and .tar.gz to rpmbuild/SOURCES/
and then use ```./run.sh```

# Centos7 with rpmbuild
FROM centos:centos7
MAINTAINER Jonathan Mainguy jon@soh.re
RUN yum install -y rpm-build make gcc \
    autoconf gettext-devel automake \
    libtool libgcrypt-devel zlib-devel \
    libcurl-devel ncurses-devel cmake \
    libevent-devel tar python2-devel \
    python-setuptools golang && \
    mkdir -p /root/rpmbuild/SPECS
WORKDIR /root/rpmbuild/SPECS
ENTRYPOINT ["/root/rpmbuild/SPECS/spec.sh"]

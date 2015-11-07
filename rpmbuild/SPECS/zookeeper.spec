#
# ZooKeeper
#
Summary: A ZooKeeper to manage solr
Name: zookeeper
Version: 3.4.6
Release: 1%{?dist}
License: GPL
Source: http://mirrors.koehn.com/apache/zookeeper/zookeeper-3.4.6/zookeeper-3.4.6.tar.gz
URL: https://zookeeper.apache.org/
BuildArch:      noarch
Distribution: RHEL 7
Vendor: Apache
Packager: Jonathan Mainguy <jmainguy@redhat.com>

%description
ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them ,which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.

%prep
%setup -q
mkdir -p ${RPM_BUILD_ROOT}/opt/zookeeper
cp -R * ${RPM_BUILD_ROOT}/opt/zookeeper/
%clean
rm -rf $RPM_BUILD_ROOT
%files
/opt/zookeeper

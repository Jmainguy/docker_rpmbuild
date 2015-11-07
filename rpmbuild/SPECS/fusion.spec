#
# Fusion
#
Summary: LucidWorks Fusion 
Name: fusion
Version: 2.1.0
Release: 2
License: GPL
Source: http://download.lucidworks.com/fusion-2.1.0.tar.gz
URL: https://lucidworks.com
BuildArch: x86_64
Vendor: LucidWorks
Packager: Jonathan Mainguy <jmainguy@redhat.com>
AutoReqProv: no

%description
As a standalone search platform or as an extension of your existing Solr implementation, Fusion provides the enterprise-grade capabilities needed to design, develop and deploy intelligent search apps at every level of your organization — at any scale.

%prep
%setup -q -n fusion
mkdir -p ${RPM_BUILD_ROOT}/opt/fusion
cp -R * ${RPM_BUILD_ROOT}/opt/fusion/
%clean
rm -rf $RPM_BUILD_ROOT
%files
/opt/fusion

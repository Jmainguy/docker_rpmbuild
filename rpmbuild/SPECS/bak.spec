#
# bak
#
Summary: bak
Name: bak
Version: 0.1
Release: 1%{?dist}
License: GPL
Source: bak.tar.gz
URL: https://github.com/Jmainguy/bak
BuildArch: x86_64
Vendor: Jmainguy
Packager: Jonathan Mainguy <jon@soh.re>

%description
Backup a file, defaults to same path and .bak

%prep
%setup -q
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
cp bak.py ${RPM_BUILD_ROOT}/usr/bin/bak
%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/bin/bak
%post
chmod 755 /usr/bin/bak

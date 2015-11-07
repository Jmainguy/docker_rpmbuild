# $Id$
# Authority: dag

# ExcludeDist: el3 el4 el5

Summary: Terminal multiplexer program
Name: tmux
Version: 1.9a
Release: 1%{?dist}
License: BSD
Group: Applications/System
URL: http://tmux.sourceforge.net/
Packager: Jonathan Mainguy <jmainguy@redhat.com>

Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or windows)
to be accessed and controlled from a single terminal. It is intended to be
a simple, modern, BSD-licensed alternative to programs such as GNU screen.

%prep
%setup
#patch0 -p1 -b .location
#patch1 -p1 -b .sockethandling
#patch2 -p1 -b .dropprivs
#%patch3 -p1 -b .writehard

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALLBIN="install -p -m0755" INSTALLMAN="install -p -m0644"

# Create the socket dir
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/tmux/

%clean
%{__rm} -rf %{buildroot}

%pre
getent group tmux >/dev/null || groupadd -r tmux

%files
%defattr(-, root, root, 0755)
%doc CHANGES FAQ TODO examples/
%doc %{_mandir}/man1/tmux.1.*
%attr(2755, root, tmux) %{_bindir}/tmux
%attr(0775, root, tmux) %{_localstatedir}/run/tmux/

%changelog
* Wed Apr 17 2013 David Hrbáč <david@hrbac.cz> - 1.8-1
- new upstream release

* Thu Oct 25 2012 Dag Wieers <dag@wieers.com> - 1.7-1
- Updated to release 1.7.

* Mon Jan 23 2012 David Hrbáč <david@hrbac.cz> - 1.6-1
- new upstream release

* Tue Jul 19 2011 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Mon Apr 11 2011 David Hrbáč <david@hrbac.cz> - 1.4-2
- CVE-2011-1496 fix
- imported Fedora patches
- added examples

* Mon Apr 11 2011 David Hrbáč <david@hrbac.cz> - 1.4-1
- new upstream release

* Tue Jul 20 2010 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Fri Nov 13 2009 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Thu Sep 24 2009 Dag Wieers <dag@wieers.com> - 1.0-1
- Updated to release 1.0.

* Fri Jul 10 2009 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Mon Apr 27 2009 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sun Feb 08 2009 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Mon Jan 19 2009 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Mon Nov 17 2008 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Fri Jul 04 2008 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Thu Jun 19 2008 Dag Wieers <dag@wieers.com> - 0.3-1
- Updated to release 0.3.

* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 0.2-1
- Initial package. (using DAR)

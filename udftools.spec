Summary: Linux UDF Filesystem userspace utilities
Name: udftools
Version: 1.0.0b3
Release: 26%{?dist}
License: GPLv2+
Group: Applications/Archiving
URL: http://sourceforge.net/projects/linux-udf/
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source2: wrudf.1
Patch0: udftools-1.0.0b3-pktsetup-chardev.patch
Patch1: udftools-1.0.0b3-mkudffs-bigendian.patch
Patch2: udftools-1.0.0b3-wrudf-gcc4.patch
Patch3: udftools-1.0.0b3-warningfixes.patch
Patch4: udftools-1.0.0b3-fixcompile.patch
Patch5: udftools-1.0.0b3-warningfixes2.patch
Patch6: udftools-1.0.0b3-extsize.patch
Patch7: udftools-1.0.0b3-staticanal.patch
Patch8: udftools-1.0.0b3-wrudf_help.patch
Patch9: udftools-1.0.0b3-man-missing-options.patch
BuildRequires: readline-devel, ncurses-devel
BuildRequires: autoconf, automake, libtool, perl-Carp

%description
Linux UDF Filesystem userspace utilities.


%prep
%setup
%patch0 -p1 -b .pktsetup-chardev
%patch1 -p1 -b .mkudffs-bigendian
%patch2 -p1 -b .wrudf-gcc4
%patch3 -p1 -b .warningfixes
%patch4 -p1 -b .fixcompile
%patch5 -p1 -b .warningfixes2
%patch6 -p1 -b .extsize
%patch7 -p1 -b .staticanal
%patch8 -p1 -b .wrudfhelp
%patch9 -p1 -b .man


%build
./bootstrap
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall
./libtool --finish %{buildroot}%{_libdir}
install -m 644 %{SOURCE2} %buildroot%{_mandir}/man1/

%files
%doc AUTHORS ChangeLog COPYING
%{_bindir}/*
#udffsck does nothing (in version 1.0.0b3), do not package
%exclude %{_bindir}/udffsck
%exclude %{_libdir}/libudffs.a
%exclude %{_libdir}/libudffs.la
%{_mandir}/man?/*


%changelog
* Wed Jan 29 2014 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.0.0b3-26
- added missing options to manual pages
  Resolves: #948506

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.0.0b3-25
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.0b3-24
- Mass rebuild 2013-12-27

* Tue Apr 16 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.0.0b3-23
- Build dependency on txt2man unacceptable. Included final man page wrudf.1 instead of source.

* Tue Apr 16 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.0.0b3-22
- added man page for wrudf

* Mon Apr 15 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.0.0b3-21
- added "--help"/"-h" with basic info to wrudf

* Fri Apr 05 2013 Frantisek Kluknavsky <fkluknav@redhat.com> - 1.0.0b3-20
- udffsck is an empty placeholder, erased

* Mon Mar 25 2013 Harald Hoyer <harald@redhat.com> 1.0.0b3-19
- run autoreconf to support aarch64 architecture
Resolves: rhbz#926671

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Honza Horak <hhorak@redhat.com> - 1.0.0b3-17
- Minor spec file fixes

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 26 2012 Honza Horak <hhorak@redhat.com> - 1.0.0b3-15
- fixed segmentation fault
  Resolves: #685005
- fixed some most obvious issues from static analysis

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 23 2010 Roman Rakus <rrakus@redhat.com> - 1.0.0b3-12
- Build with -fno-strict-aliasing CFLAG

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0b3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.0b3-9
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Harald Hoyer <harald@redhat.com> - 1.0.0b3-8
- fixed compile issues
- added more bigendian patches
- changed license tag

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-7
- FC6 rebuild.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-6
- Add ncurses-devel build requirement, since it's not pulled in anymore.
- Add patch to fix as many trivial warnings as possible. Some stuff seems to
  still not be 64bit clean, though.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-5
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 1.0.0b3-4
- Rebuild for new gcc/glibc.
- Exclude the static library... there isn't even a header file.

* Tue May  3 2005 Matthias Saou <http://freshrpms.net/> 1.0.0b3-3
- Include patches to fix big endian issue and gcc4 compile.

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.0.0b3-1
- Initial RPM release, based on spec file from John Treacy.
- Exclude .la file.
- Remove unneeded /sbin/ldconfig calls (only a static lib for now).


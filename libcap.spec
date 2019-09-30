Name:     libcap
Version:  2.25
Release:  14
Summary:  A library for getting and setting POSIX.1e draft 15 capabilities        
License:  GPLv2
URL:      https://sites.google.com/site/fullycapable
Source0:  https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/%{name}-%{version}.tar.gz

Patch1: %{name}-2.25-buildflags.patch

BuildRequires: libattr-devel pam-devel perl-interpreter gcc

%description
This is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

%package devel
Summary: Development headers and libraries for %{name}
Requires:%{name} = %{version}-%{release}

%description devel
Development headers and libraries for %{name}

%package_help

%prep
%autosetup -n %{name}-%{version} -p1  

%build
make prefix=%{_prefix} lib=%{_lib} LIBDIR=%{_libdir} SBINDIR=%{_sbindir} \
     INCDIR=%{_includedir} MANDIR=%{_mandir} PKGCONFIGDIR=%{_libdir}/pkgconfig/

%install
make install RAISE_SETFCAP=no DESTDIR=%{buildroot} LIBDIR=%{_libdir} SBINDIR=%{_sbindir} PKGCONFIGDIR=%{_libdir}/pkgconfig/

mkdir -p %{buildroot}/%{_mandir}/man{2,3,8}
mv -f doc/*.3 %{buildroot}/%{_mandir}/man3/
chmod +x %{buildroot}/%{_libdir}/*.so.*

%pre

%preun

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license License
%doc doc/capability.notes
%{_libdir}/*.so.*
%{_sbindir}/*
%{_libdir}/security/pam_cap.so

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.a

%files help
%defattr(-,root,root)
%{_mandir}/man3/*.gz
%{_mandir}/man1/*.gz
%{_mandir}/man8/*.gz

%changelog
* Sun Sep 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.25-14
- Fix bugfix of missing pam_cap.so

* Wed Aug 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.25-13
- Package init

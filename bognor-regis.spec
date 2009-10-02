%define major           0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname %{name} -d

%define version 0.4.10
%define rel 2
%define snapshot git20091001
%define release %mkrel 0.%{snapshot}.%{rel}

%define sversion %{version}%{snapshot}

Name: bognor-regis
Summary: Media daemon and play queue manager
Group: Graphical desktop/Other
Version: %{version}
License: LGPLv2.1
URL: http://www.moblin.org
Release: %{release}
Source0: %{name}-%{sversion}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: glib2-devel
BuildRequires: libgtk+2.0-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libgstreamer-devel
BuildRequires: libGConf2-devel
BuildRequires: intltool

%description
Media daemon and play queue manager

%package -n %{libname}
Group: System/Libraries
Summary: Media daemon and play queue manager
Requires: %{name}

%description -n %{libname}
Bognor Regis library

%package -n %{develname}
Summary: Bognor Regis development environment
Group: Development/C

Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel

%description -n %{develname}
Bognor Regis development environment

%prep
%setup -q -n %{name}-%{sversion}
perl -pi -e 's,^./configure.*,,' ./autogen.sh

%build
./autogen.sh
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README NEWS AUTHORS ChangeLog
%{_libexecdir}/bognor-regis-daemon
%{_datadir}/dbus-1/services/org.moblin.BognorRegis.service
%{_datadir}/locale/*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/%{name}*
%{_libdir}/libbognor-regis-*.la
%{_libdir}/libbognor-regis-*.a
%{_libdir}/lib*.so
%{_libdir}/pkgconfig

%files -n %{libname}
%{_libdir}/libbognor-regis-*.so.*

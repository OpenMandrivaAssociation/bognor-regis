%define major           0
%define libname         %mklibname %{name} %{major}
%define develname       %mklibname %{name} -d

Name: bognor-regis
Summary: Media daemon and play queue manager
Group: Applications/Multimedia
Version: 0.4.10git20091001
License: LGPLv2.1
URL: http://www.moblin.org
Release: %mkrel 1
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: glib2-devel
BuildRequires: libdbus-glib-devel
BuildRequires: libgstreamer-devel

%description
Media daemon and play queue manager

%package -n %{libname}
Group: System/Libraries
Summary: Media daemon and play queue manager

%description -n %{libname}
Bognor Regis library

%package -n %{develname}
Summary: Bognor Regis development environment
Group: Development/Libraries

Requires: %{libname} = %{version}-%{release}
Requires: pkgconfig
Requires: %{libname} >= %{version}

%description -n %{develname}
Bognor Regis development environment

%prep
%setup -q

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

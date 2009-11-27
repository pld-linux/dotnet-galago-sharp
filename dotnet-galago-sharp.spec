#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET language bindings for Galago
Summary(pl.UTF-8):	Wiązania Galago dla .NET
Name:		dotnet-galago-sharp
Version:	0.5.0
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://www.galago-project.org/files/releases/source/galago-sharp/galago-sharp-%{version}.tar.gz
# Source0-md5:	87fb532cfe2085f81fe824c17f8836eb
Source1:	galago-api.xml
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-pkgconfig.patch
Patch2:		%{name}-destdir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	libgalago-devel >= 0.5.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Galago libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do bibliotek z Galago.

%package devel
Summary:	Development part of galago-sharp
Summary(pl.UTF-8):	Programistyczna część galago-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgalago-devel >= 0.5.0

%description devel
Tools for developing applications using galago-sharp.

%description devel -l pl.UTF-8
Narzędzia potrzebne przy tworzeniu aplikacji korzystających z
galago-sharp.

%prep
%setup -qn galago-sharp-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

cp %{SOURCE1} galago

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/mono/gac/galago-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/galago-sharp
%{_datadir}/gapi-2.0/*
%{_pkgconfigdir}/*.pc

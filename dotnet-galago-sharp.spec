%include	/usr/lib/rpm/macros.mono
Summary:	.NET language bindings for Galago
Summary(pl):	Wi±zania Galago dla .NET
Name:		dotnet-galago-sharp
Version:	0.3.2
Release:	4
License:	GPL
Group:		Development/Libraries
Source0:	http://www.galago-project.org/files/releases/source/galago-sharp/galago-sharp-%{version}.tar.gz
# Source0-md5:	90824eaf08bfbbbc0155ab08b623bced
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-pkgconfig.patch
Patch2:		%{name}-destdir.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel
BuildRequires:	libgalago-devel >= 0.3.2
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Galago libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Galago.

%package devel
Summary:	Development part of galago-sharp
Summary(pl):	Programistyczna czê¶æ galago-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgalago-devel >= 0.3.2

%description devel
Tools for developing applications using galago-sharp.

%description devel -l pl
Narzêdzia potrzebne przy tworzeniu aplikacji korzystaj±cych z
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
%{__make} \
	gapidir='%{_datadir}/gapi-2.0'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gapidir='%{_datadir}/gapi-2.0'

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

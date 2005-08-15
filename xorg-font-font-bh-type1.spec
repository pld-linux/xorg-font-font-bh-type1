# $Rev: 3200 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	font-bh-type1
Summary(pl):	font-bh-type1
Name:		xorg-font-font-bh-type1
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bh-type1-%{version}.tar.bz2
# Source0-md5:	be1242ee102d2b61ab802c16bcd68c92
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/font-bh-type1-%{version}-root-%(id -u -n)

%description
font-bh-type1

%description -l pl
font-bh-type1


%prep
%setup -q -n font-bh-type1-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/Type1/*

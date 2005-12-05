Summary:	bh-type1 font
Summary(pl):	Font bh-type1
Name:		xorg-font-font-bh-type1
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/font/font-bh-type1-%{version}.tar.bz2
# Source0-md5:	867ff907066a1e57031e7c11034f95e3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	t1utils
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bh-type1 font.

%description -l pl
Font bh-type1.

%prep
%setup -q -n font-bh-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm, convert *.pfa to .pfb
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
mv -f *.afm afm
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
sed -i -e 's/\.pfa /.pfb /' fonts.scale
mv -f fonts.scale fonts.scale.bh

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/Type1/*.pfb
%{_fontsdir}/Type1/afm/*.afm
%{_fontsdir}/Type1/fonts.scale.bh

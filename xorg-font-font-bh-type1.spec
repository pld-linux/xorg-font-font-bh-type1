Summary:	Bigelow & Holmes Luxi fonts in Type1 format
Summary(pl.UTF-8):	Fonty Bigelow & Holmes Luxi w formacie Type1
Name:		xorg-font-font-bh-type1
Version:	1.0.4
Release:	1
License:	distributable if unmodified
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-bh-type1-%{version}.tar.xz
# Source0-md5:	51a17c981275439b85e15430a3d711ee
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	fontconfig
BuildRequires:	t1utils
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.2
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/Type1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bigelow & Holmes Luxi fonts in Type1 format.

%description -l pl.UTF-8
Fonty Bigelow & Holmes Luxi w formacie Type1.

%prep
%setup -q -n font-bh-type1-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/Type1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate *.afm, convert *.pfa to .pfb
cd $RPM_BUILD_ROOT%{_fontsdir}/Type1
install -d afm
%{__mv} *.afm afm
for f in *.pfa ; do
	t1binary $f `basename $f .pfa`.pfb
	rm -f $f
done
sed -e '1d;s/\.pfa /.pfb /' fonts.scale > fonts.scale.bh
%{__rm} fonts.scale fonts.dir

cat > Fontmap.bh <<EOF
/LuxiMono                                (l047013t.pfb) ;
/LuxiMono-Bold                           (l047016t.pfb) ;
/LuxiMono-Oblique                        (l047033t.pfb) ;
/LuxiMono-BoldOblique                    (l047036t.pfb) ;
/LuxiSans                                (l048013t.pfb) ;
/LuxiSans-Bold                           (l048016t.pfb) ;
/LuxiSans-Oblique                        (l048033t.pfb) ;
/LuxiSans-BoldOblique                    (l048036t.pfb) ;
/LuxiSerif                               (l049013t.pfb) ;
/LuxiSerif-Bold                          (l049016t.pfb) ;
/LuxiSerif-Oblique                       (l049033t.pfb) ;
/LuxiSerif-BoldOblique                   (l049036t.pfb) ;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst Type1

%postun
fontpostinst Type1

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/Type1/l04*.pfb
%{_fontsdir}/Type1/afm/l04*.afm
%{_fontsdir}/Type1/fonts.scale.bh
%{_fontsdir}/Type1/Fontmap.bh

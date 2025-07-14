Summary:	A Sinclair ZX Spectrum Emulator
Summary(pl.UTF-8):	Emulator Sinclair ZX Spectrum
Name:		fbzx
Version:	2.5.0
Release:	1
License:	GPL v3+
Group:		Applications/Emulators
Source0:	http://www.rastersoft.com/descargas/%{name}-%{version}.tar.bz2
# Source0-md5:	c3abdfe41a9d6829c50ea62d25c4526e
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-install.patch
Patch2:		%{name}-desktop.patch
URL:		http://www.rastersoft.com/programas/fbzxesp.html
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	sed >= 4.0
BuildRequires:	svg2png
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Sinclair ZX Spectrum Emulator, designed to work both in framebuffer
and X.

%description -l pl.UTF-8
Emulator Sinclair ZX Spectrum, działający zarówno z buforem ramki
(framebuffer) jak i z systemem X-Window.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%{__sed} -i 's,spectrum-roms,%{_datadir}/%{name}/spectrum-roms,' emulator.c

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `pkg-config --cflags sdl libpulse-simple alsa` -D D_SOUND_PULSE -D D_SOUND_ALSA -D D_SOUND_OSS" \
	LDFLAGS="%{rpmldflags}" \
	LIBS="`pkg-config --libs sdl libpulse-simple alsa`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

svg2png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.svg $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# useless (svg converted to png)
%{__rm} $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.svg

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AMSTRAD CAPABILITIES README* TODO VERSIONS
%attr(755,root,root) %{_bindir}/fbzx
%{_datadir}/%{name}
%{_desktopdir}/fbzx.desktop
%{_pixmapsdir}/fbzx.png

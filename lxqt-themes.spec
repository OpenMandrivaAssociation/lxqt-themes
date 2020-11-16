%define git 0
Name: lxqt-themes
Version:	0.16.0
%if %git
Release:	1
Source0: %{name}-%{git}.tar.xz
%else
Release:	1
Source0:	https://github.com/lxqt/lxqt-themes/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz
%endif
Summary: Themes for the LXQt desktop
URL: http://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: ninja
BuildRequires: lxqt-build-tools
BuildArch: noarch
Conflicts: lxqt-common < 0.12.0

%description
Themes for the LXQt desktop.

%prep
%if %git
%setup -qn %{name}-%{git}
%else
%setup -q
%endif
%autopatch -p1
%cmake_qt5 -DPULL_TRANSLATIONS=NO -G Ninja

%build
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja -C build

%install
# Need to be in a UTF-8 locale so grep (used by the desktop file
# translation generator) doesn't scream about translations containing
# "binary" (non-ascii) characters
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8
%ninja_install -C build

# (tpg) openmandriva icons
for i in `ls -1 %{buildroot}%{_datadir}/lxqt/themes`; do
    ln -sf %{_iconsdir}/openmandriva.svg %{buildroot}%{_datadir}/lxqt/themes/$i/openmandriva.svg
    sed -i -e "s/mainmenu.svg/openmandriva.svg/g" %{buildroot}%{_datadir}/lxqt/themes/$i/lxqt-panel.qss
    sed -i 's|file=.*$|file=default.png|' %{buildroot}%{_datadir}/lxqt/themes/$i/wallpaper.cfg ||:
    ln -sf %{_datadir}/mdk/backgrounds/default.png %{buildroot}%{_datadir}/lxqt/themes/$i/default.png
done

%files
%{_datadir}/icons/*/*/*/*
%{_datadir}/lxqt/graphics
%{_datadir}/lxqt/themes/*

#define git 0
Name: lxqt-themes
Version: 2.4.0
%if 0%{?git:1}
Source0: %{name}-%{git}.tar.xz
%else
Source0: https://github.com/lxqt/lxqt-themes/releases/download/%{version}/lxqt-themes-%{version}.tar.xz
%endif
Release: %{?git:0.%{git}.}2
Summary: Themes for the LXQt desktop
URL: https://lxqt.org/
License: GPL
Group: Graphical desktop/KDE
BuildSystem: cmake
BuildOption: -DPULL_TRANSLATIONS=NO
BuildRequires: lxqt-build-tools
BuildArch: noarch
Conflicts: lxqt-common < 0.12.0

%description
Themes for the LXQt desktop.

%build -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -p
export LANG=en_US.utf-8
export LC_ALL=en_US.utf-8

%install -a
# (tpg) openmandriva icons
for i in $(ls -1 %{buildroot}%{_datadir}/lxqt/themes); do
	ln -sf %{_iconsdir}/openmandriva.svg %{buildroot}%{_datadir}/lxqt/themes/$i/openmandriva.svg
	sed -i -e "s/mainmenu.svg/openmandriva.svg/g" %{buildroot}%{_datadir}/lxqt/themes/$i/lxqt-panel.qss
	sed -i 's|file=.*$|file=default.png|' %{buildroot}%{_datadir}/lxqt/themes/$i/wallpaper.cfg ||:
	ln -sf %{_datadir}/mdk/backgrounds/default.png %{buildroot}%{_datadir}/lxqt/themes/$i/default.png
done

%files
%{_datadir}/icons/*/*/*/*
%{_datadir}/lxqt/graphics
%{_datadir}/lxqt/themes/*
%{_datadir}/lxqt/palettes
%{_datadir}/lxqt/wallpapers

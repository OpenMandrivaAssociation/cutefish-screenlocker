%define oname screenlocker

Name:           cutefish-screenlocker
Version:        0.5
Release:        1
Summary:        System screen locker
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://github.com/cutefishos/screenlocker
Source:         https://github.com/cutefishos/screenlocker/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(x11)

%description
Third Party Code - kcheckpass.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/ccheckpass

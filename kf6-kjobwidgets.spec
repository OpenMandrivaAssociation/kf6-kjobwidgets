%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6JobWidgets
%define devname %mklibname KF6JobWidgets -d
#define git 20240217

Name: kf6-kjobwidgets
Version: 6.12.0
Release: %{?git:0.%{git}.}2
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kjobwidgets/-/archive/master/kjobwidgets-master.tar.bz2#/kjobwidgets-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/kjobwidgets-%{version}.tar.xz
%endif
Summary: Widgets for showing progress of asynchronous jobs
URL: https://invent.kde.org/frameworks/kjobwidgets
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6Notifications)
Requires: %{libname} = %{EVRD}

%description
Widgets for showing progress of asynchronous jobs

%package -n %{libname}
Summary: Widgets for showing progress of asynchronous jobs
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Widgets for showing progress of asynchronous jobs

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Widgets for showing progress of asynchronous jobs

%prep
%autosetup -p1 -n kjobwidgets-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kjobwidgets.*
%{_datadir}/dbus-1/interfaces/*Job*.xml

%files -n %{devname}
%{_includedir}/KF6/KJobWidgets
%{_libdir}/cmake/KF6JobWidgets
%{_qtdir}/doc/KF6JobWidgets.*

%files -n %{libname}
%{_libdir}/libKF6JobWidgets.so*

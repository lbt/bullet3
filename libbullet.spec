#
# spec file for package libbullet
#

Name:           libbullet
%define lname   libbullet2_82
Version: 2.82
Release: 2
Summary:        Bullet Continuous Collision Detection and Physics Library
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://bulletphysics.org/
BuildRequires:  cmake
#BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libxml2-devel
Source:         libbullet-%{version}.tar.gz
Patch1:	0001-Add-missing-UseBullet.cmake.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bullet is a Collision Detection and Rigid Body Dynamics Library. The
Library is Open Source and free for commercial use, under the ZLib
license. This means you can use it in commercial games, even on
next-generation consoles like Sony Playstation 3.

%package -n %lname
Summary:        Bullet Continuous Collision Detection and Physics Library
Group:          System/Libraries
Obsoletes:      libbullet < %{version}-%{release}
Provides:       libbullet = %{version}-%{release}

%description -n %lname
Bullet is a Collision Detection and Rigid Body Dynamics Library. The
Library is Open Source and free for commercial use, under the ZLib
license. This means you can use it in commercial games, even on
next-generation consoles like Sony Playstation 3.

%package devel
Summary:        Development package for bullet library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
This package contain all that is needed to developer or compile
appliancation with the Bullet library.

%prep
%setup -q -n src
%patch1 -p1

%build
LIB_DIR=%{_lib}
cmake . -DMAKE_SKIP_RPATH=ON \
 -DBUILD_SHARED_LIBS=ON \
 -DCMAKE_BUILD_TYPE=RelWithDebInfo \
 -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
 -DLIB_SUFFIX=${LIB_DIR#lib} \
 -DBUILD_EXTRAS=OFF \
 -DBUILD_DEMOS=OFF \
 -DUSE_GLUT=OFF \
 -DUSE_NEON=ON

make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libB*.so.2.82
%{_libdir}/libLinearMath*.so.2.82

%files devel
%defattr(-,root,root)
%{_includedir}/bullet/
%{_libdir}/pkgconfig/bullet.pc
%{_libdir}/libB*.so
%{_libdir}/libLinearMath*.so

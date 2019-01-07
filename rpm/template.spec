Name:           ros-melodic-jskeus
Version:        1.2.1
Release:        0%{?dist}
Summary:        ROS jskeus package

Group:          Development/Libraries
License:        BSD
URL:            http://euslisp.github.io/jskeus/manual.html
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-euslisp
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-euslisp

%description
EusLisp software developed and used by JSK at The University of Tokyo

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Jan 07 2019 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.1-0
- Autogenerated by Bloom

* Thu Jul 19 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-3
- Autogenerated by Bloom

* Thu Jul 19 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-2
- Autogenerated by Bloom

* Thu Jul 19 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-1
- Autogenerated by Bloom

* Thu Jul 19 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.2.0-0
- Autogenerated by Bloom


#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reportlab
Version  : 3.5.68
Release  : 70
URL      : https://files.pythonhosted.org/packages/f8/3b/3684a3414cde1626be5245af21ace0629ceb1e38ff745a84e07349505827/reportlab-3.5.68.tar.gz
Source0  : https://files.pythonhosted.org/packages/f8/3b/3684a3414cde1626be5245af21ace0629ceb1e38ff745a84e07349505827/reportlab-3.5.68.tar.gz
Summary  : The Reportlab Toolkit
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0 OFL-1.0
Requires: reportlab-license = %{version}-%{release}
Requires: reportlab-python = %{version}-%{release}
Requires: reportlab-python3 = %{version}-%{release}
Requires: Pillow
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
This directory is the home of various ReportLab tools.
They are packaged such that they can be used more easily.

%package license
Summary: license components for the reportlab package.
Group: Default

%description license
license components for the reportlab package.


%package python
Summary: python components for the reportlab package.
Group: Default
Requires: reportlab-python3 = %{version}-%{release}

%description python
python components for the reportlab package.


%package python3
Summary: python3 components for the reportlab package.
Group: Default
Requires: python3-core
Provides: pypi(reportlab)
Requires: pypi(pillow)

%description python3
python3 components for the reportlab package.


%prep
%setup -q -n reportlab-3.5.68
cd %{_builddir}/reportlab-3.5.68

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1624893938
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/reportlab
cp %{_builddir}/reportlab-3.5.68/LICENSE.txt %{buildroot}/usr/share/package-licenses/reportlab/638e7067709f6721a407b256bd4ed84cb1737106
cp %{_builddir}/reportlab-3.5.68/src/reportlab/fonts/bitstream-vera-license.txt %{buildroot}/usr/share/package-licenses/reportlab/b3245f6ac784e19a10843831b45b5944c62e3ccc
cp %{_builddir}/reportlab-3.5.68/src/reportlab/license.txt %{buildroot}/usr/share/package-licenses/reportlab/638e7067709f6721a407b256bd4ed84cb1737106
cp %{_builddir}/reportlab-3.5.68/src/rl_addons/renderPM/libart_lgpl/COPYING %{buildroot}/usr/share/package-licenses/reportlab/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/reportlab/638e7067709f6721a407b256bd4ed84cb1737106
/usr/share/package-licenses/reportlab/b3245f6ac784e19a10843831b45b5944c62e3ccc
/usr/share/package-licenses/reportlab/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

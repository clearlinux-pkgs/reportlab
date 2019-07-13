#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reportlab
Version  : 3.5.23
Release  : 29
URL      : https://files.pythonhosted.org/packages/41/93/c57ed3f33daabaad2146504d888ea77c44d35fa57bf844342a70f4593007/reportlab-3.5.23.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/93/c57ed3f33daabaad2146504d888ea77c44d35fa57bf844342a70f4593007/reportlab-3.5.23.tar.gz
Summary  : The Reportlab Toolkit
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0
Requires: reportlab-license = %{version}-%{release}
Requires: reportlab-python = %{version}-%{release}
Requires: reportlab-python3 = %{version}-%{release}
Requires: Pillow
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
# rlzope : an external Zope method to show people how to use
# the ReportLab toolkit from within Zope.
# this method searches an image named 'logo' in the
# ZODB then prints it at the top of a simple PDF
# document made with ReportLab
# the resulting PDF document is returned to the
# user's web browser and, if possible, it is
# simultaneously saved into the ZODB.
# this method illustrates how to use both the platypus
# and canvas frameworks.
# License : The ReportLab Toolkit's license (similar to BSD)
# Author : Jerome Alet - alet@librelogiciel.com

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

%description python3
python3 components for the reportlab package.


%prep
%setup -q -n reportlab-3.5.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559319903
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/reportlab
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/reportlab/LICENSE.txt
cp src/reportlab/license.txt %{buildroot}/usr/share/package-licenses/reportlab/src_reportlab_license.txt
cp src/rl_addons/renderPM/libart_lgpl/COPYING %{buildroot}/usr/share/package-licenses/reportlab/src_rl_addons_renderPM_libart_lgpl_COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/reportlab/LICENSE.txt
/usr/share/package-licenses/reportlab/src_reportlab_license.txt
/usr/share/package-licenses/reportlab/src_rl_addons_renderPM_libart_lgpl_COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

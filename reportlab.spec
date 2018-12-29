#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : reportlab
Version  : 3.5.12
Release  : 19
URL      : https://files.pythonhosted.org/packages/5b/85/0242a416eb5e50815216ac548129cdc9bbcc8a4b12a2f93cc19ead9ae0d9/reportlab-3.5.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/5b/85/0242a416eb5e50815216ac548129cdc9bbcc8a4b12a2f93cc19ead9ae0d9/reportlab-3.5.12.tar.gz
Summary  : The Reportlab Toolkit
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.0
Requires: reportlab-license = %{version}-%{release}
Requires: reportlab-python = %{version}-%{release}
Requires: reportlab-python3 = %{version}-%{release}
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

%description python3
python3 components for the reportlab package.


%prep
%setup -q -n reportlab-3.5.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543752189
python3 setup.py build

%install
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

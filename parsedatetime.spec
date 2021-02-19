#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : parsedatetime
Version  : 2.5
Release  : 32
URL      : https://files.pythonhosted.org/packages/5f/19/43357ced106dd1ab6bceb1decb866e8619172fc271991a54eb2f680a2e9b/parsedatetime-2.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/19/43357ced106dd1ab6bceb1decb866e8619172fc271991a54eb2f680a2e9b/parsedatetime-2.5.tar.gz
Summary  : Parse human-readable date/time text.
Group    : Development/Tools
License  : Apache-2.0
Requires: parsedatetime-license = %{version}-%{release}
Requires: parsedatetime-python = %{version}-%{release}
Requires: parsedatetime-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest
BuildRequires : pytest-python
BuildRequires : python-future

%description
Parse human-readable date/time strings.
        
        Python 2.6 or greater is required for parsedatetime version 1.0 or greater.
        
        While we still test with Python 2.6 we cannot guarantee that future changes will not break under 2.6

%package license
Summary: license components for the parsedatetime package.
Group: Default

%description license
license components for the parsedatetime package.


%package python
Summary: python components for the parsedatetime package.
Group: Default
Requires: parsedatetime-python3 = %{version}-%{release}

%description python
python components for the parsedatetime package.


%package python3
Summary: python3 components for the parsedatetime package.
Group: Default
Requires: python3-core
Provides: pypi(parsedatetime)

%description python3
python3 components for the parsedatetime package.


%prep
%setup -q -n parsedatetime-2.5
cd %{_builddir}/parsedatetime-2.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603397676
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/parsedatetime
cp %{_builddir}/parsedatetime-2.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/parsedatetime/76d24cdbc1fa8ba89cee3fd79e9841cdb21f9fbe
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/parsedatetime/76d24cdbc1fa8ba89cee3fd79e9841cdb21f9fbe

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : parsedatetime
Version  : 2.4
Release  : 13
URL      : http://pypi.debian.net/parsedatetime/parsedatetime-2.4.tar.gz
Source0  : http://pypi.debian.net/parsedatetime/parsedatetime-2.4.tar.gz
Summary  : Parse human-readable date/time text.
Group    : Development/Tools
License  : Apache-2.0
Requires: parsedatetime-python3
Requires: parsedatetime-python
BuildRequires : attrs-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy-python
BuildRequires : py-python
BuildRequires : pytest-python

BuildRequires : python-future
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python

%description
Parse human-readable date/time strings.
        
        Python 2.6 or greater is required for parsedatetime version 1.0 or greater.
        
        While we still test with Python 2.6 we cannot guarantee that future changes will not break under 2.6

%package python
Summary: python components for the parsedatetime package.
Group: Default
Requires: parsedatetime-python3

%description python
python components for the parsedatetime package.


%package python3
Summary: python3 components for the parsedatetime package.
Group: Default
Requires: python3-core

%description python3
python3 components for the parsedatetime package.


%prep
%setup -q -n parsedatetime-2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519051103
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

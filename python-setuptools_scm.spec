#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Python 2 package to manager versions by scm tags
Summary(pl.UTF-8):	Pakiet Pythona 2 do zarządzania wersjami poprzez etykiety systemu kontroli wersji
Name:		python-setuptools_scm
Version:	1.2.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/setuptools_scm
Source0:	https://pypi.python.org/packages/source/s/setuptools_scm/setuptools-scm-%{version}.tar.gz
# Source0-md5:	251730e2ca3ff05e6e1fcd4ba368e6a8
URL:		https://bitbucket.org/pypa/setuptools_scm/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
BuildRequires:	python3-modules >= 1:3.2
%endif
Requires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

%description -l pl.UTF-8
setuptools_scm to proste narzędzie dla funkcji setup_requires modułu
setuptools przeznaczone do stosowania w projektach opatych na
systemach kontroli wersji Mercurial i Git.

%package -n python3-setuptools_scm
Summary:	Python 3 package to manager versions by scm tags
Summary(pl.UTF-8):	Pakiet Pythona 3 do zarządzania wersjami poprzez etykiety systemu kontroli wersji
Group:		Libraries/Python
Requires:	python3-setuptools

%description -n python3-setuptools_scm
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

%description -n python3-setuptools_scm -l pl.UTF-8
setuptools_scm to proste narzędzie dla funkcji setup_requires modułu
setuptools przeznaczone do stosowania w projektach opatych na
systemach kontroli wersji Mercurial i Git.

%prep
%setup -q -n setuptools-scm-%{version}

%build
%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py_sitescriptdir}/setuptools_scm
%{py_sitescriptdir}/setuptools_scm-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-setuptools_scm
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/setuptools_scm
%{py3_sitescriptdir}/setuptools_scm-%{version}-py*.egg-info
%endif

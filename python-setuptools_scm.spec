#
# Conditional build:
%bcond_without	tests		# py.test tests
%bcond_with	tests_scm	# py.test tests using SCM programs (git, hg)
%bcond_without	python2		# CPython 2.x module
%bcond_without	python3		# CPython 3.x module

Summary:	Python 2 package to manager versions by scm tags
Summary(pl.UTF-8):	Pakiet Pythona 2 do zarządzania wersjami poprzez etykiety systemu kontroli wersji
Name:		python-setuptools_scm
Version:	2.1.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools_scm/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
# Source0-md5:	cfec5d2dbbd0a85c40066f79035b5878
URL:		https://github.com/pypa/setuptools_scm
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-py >= 1.4.26
BuildRequires:	python-pytest >= 3.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
BuildRequires:	python3-modules >= 1:3.4
%if %{with tests}
BuildRequires:	python3-py >= 1.4.26
BuildRequires:	python3-pytest >= 3.1.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests_scm}
BuildRequires:	git-core
BuildRequires:	mercurial
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
%setup -q -n setuptools_scm-%{version}

%if %{without tests_scm}
%{__rm} testing/test_{file_finder,git,mercurial,regressions}.py
%endif

# tries to install using pip
%{__rm} testing/test_setuptools_support.py

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python} -m pytest
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
%{__python3} -m pytest
%endif
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

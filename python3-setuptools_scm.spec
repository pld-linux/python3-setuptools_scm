#
# Conditional build:
%bcond_with	tests		# py.test tests
%bcond_with	tests_scm	# py.test tests using SCM programs (git, hg)

Summary:	Python 3 package to manager versions by scm tags
Summary(pl.UTF-8):	Pakiet Pythona 3 do zarządzania wersjami poprzez etykiety systemu kontroli wersji
Name:		python3-setuptools_scm
Version:	6.4.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools_scm/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
# Source0-md5:	b4e02bf8e62ed49142ea7b42a68671d7
URL:		https://github.com/pypa/setuptools_scm
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-packaging >= 20.0
BuildRequires:	python3-setuptools >= 1:45
BuildRequires:	python3-tomli >= 1.0.0
%if %{with tests}
BuildRequires:	python3-pytest >= 3.1.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with tests_scm}
BuildRequires:	git-core
BuildRequires:	mercurial
%endif
Requires:	python3-setuptools >= 1:45
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
setuptools_scm is a simple utility for the setup_requires feature of
setuptools for use in Mercurial and Git based projects.

%description -l pl.UTF-8
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
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest testing
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst LICENSE README.rst
%{py3_sitescriptdir}/setuptools_scm
%{py3_sitescriptdir}/setuptools_scm-%{version}-py*.egg-info

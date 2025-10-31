# TODO: docs (BR: mkdocs + extensions)
#
# Conditional build:
%bcond_with	tests		# pytest tests
%bcond_with	tests_scm	# pytest tests using SCM programs (git, hg)

Summary:	Python 3 package to manager versions by scm tags
Summary(pl.UTF-8):	Pakiet Pythona 3 do zarządzania wersjami poprzez etykiety systemu kontroli wersji
Name:		python3-setuptools_scm
Version:	9.2.2
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/setuptools_scm/
Source0:	https://files.pythonhosted.org/packages/source/s/setuptools_scm/setuptools_scm-%{version}.tar.gz
# Source0-md5:	72975fc3ec40a1ae06bb2d86ca8ac48d
URL:		https://github.com/pypa/setuptools_scm
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-packaging >= 20.0
BuildRequires:	python3-setuptools >= 1:61
%if "%{_ver_lt %{py3_ver} 3.11}" == "1"
BuildRequires:	python3-tomli >= 1.0.0
%endif
%if %{with tests}
BuildRequires:	python3-build
BuildRequires:	python3-pytest >= 3.1.0
BuildRequires:	python3-pytest-timeout
BuildRequires:	python3-rich
%if "%{_ver_lt %{py3_ver} 3.11}" == "1"
BuildRequires:	python3-typing_extensions
%endif
BuildRequires:	python3-wheel
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.750
%if %{with tests_scm}
BuildRequires:	git-core
BuildRequires:	mercurial
%endif
Requires:	python3-modules >= 1:3.8
Requires:	python3-setuptools >= 1:61
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
%{__rm} testing/test_{cli,file_finder,git,mercurial,regressions}.py
%endif

cat > setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
export PYTHONPATH=$(pwd):$(pwd)/src
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_timeout \
%{__python3} -m pytest testing
%endif

%install
rm -rf $RPM_BUILD_ROOT

export PYTHONPATH=$(pwd):$(pwd)/src
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%attr(755,root,root) %{_bindir}/setuptools-scm
%{py3_sitescriptdir}/setuptools_scm
%{py3_sitescriptdir}/setuptools_scm-%{version}-py*.egg-info

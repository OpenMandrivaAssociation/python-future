%global pypi_name future

Name:           python-future
Version:	1.0.0
Release:	1
Group:          Development/Python
Summary:        Clean single-source support for Python 3 and 2

License:        MIT
Source0:	https://files.pythonhosted.org/packages/source/f/future/future-%{version}.tar.gz
BuildArch:      noarch
 
BuildSystem:	python

%description
Easy, safe support for Python 3/2 compatibility

%files
%doc README.rst docs/_themes/LICENSE LICENSE.txt
%{_bindir}/futurize
%{_bindir}/pasteurize
%{python_sitelib}/%{pypi_name}-%{version}-py*.*.egg-info
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/past
%{python_sitelib}/libfuturize
%{python_sitelib}/libpasteurize

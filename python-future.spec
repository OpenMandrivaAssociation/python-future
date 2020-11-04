%global pypi_name future

Name:           python-future
Version:	0.18.2
Release:	3
Group:          Development/Python
Summary:        Clean single-source support for Python 3 and 2

License:        MIT
Source0:	https://files.pythonhosted.org/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python-setuptools


%description
Easy, safe support for Python 3/2 compatibility

%package -n     python2-%{pypi_name}
Summary:        Clean single-source support for Python 3 and 2

%description -n python2-%{pypi_name}
Easy, safe support for Python 3/2 compatibility


%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'

%build
# Do the build in the install stage.
# The build system wipes the build directory at the start of the 
# build


%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
pushd %{py2dir}
%{__python2} setup.py install --root %{buildroot}
mv %{buildroot}%{_bindir}/futurize %{buildroot}/%{_bindir}/python2-futurize
mv %{buildroot}%{_bindir}/pasteurize %{buildroot}/%{_bindir}/python2-pasteurize
popd

%{__python} setup.py install --root %{buildroot}


%files
%doc README.rst docs/_themes/LICENSE LICENSE.txt
%{_bindir}/futurize
%{_bindir}/pasteurize
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/past
%{python_sitelib}/libfuturize
%{python_sitelib}/libpasteurize

%files -n python2-%{pypi_name}
%{_bindir}/python2-futurize
%{_bindir}/python2-pasteurize
%doc README.rst docs/_themes/LICENSE LICENSE.txt
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/past
%{python2_sitelib}/libfuturize
%{python2_sitelib}/libpasteurize
%{python2_sitelib}/builtins
%{python2_sitelib}/copyreg
%{python2_sitelib}/html
%{python2_sitelib}/http
%{python2_sitelib}/queue
%{python2_sitelib}/reprlib
%{python2_sitelib}/socketserver
%{python2_sitelib}/tkinter
%{python2_sitelib}/_dummy_thread
%{python2_sitelib}/_markupbase
%{python2_sitelib}/_thread
%{python2_sitelib}/winreg
%{python2_sitelib}/xmlrpc


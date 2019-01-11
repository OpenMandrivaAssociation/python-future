%global pypi_name future

Name:           python-future
Version:        0.17.1
Release:        1
Group:          Development/Python
Summary:        Clean single-source support for Python 3 and 2

License:        MIT
Source0:        https://pypi.python.org/packages/source/f/future/future-%{version}.tar.gz
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
python setup.py install --root %{buildroot}
mv %{buildroot}%{_bindir}/futurize %{buildroot}/%{_bindir}/python2-futurize
mv %{buildroot}%{_bindir}/pasteurize %{buildroot}/%{_bindir}/python2-pasteurize
popd

python setup.py install --root %{buildroot}


%files
%doc README.rst docs/_themes/LICENSE LICENSE.txt
%{_bindir}/futurize
%{_bindir}/pasteurize
%{py_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info
%{py_puresitedir}/%{pypi_name}
%{py_puresitedir}/past
%{py_puresitedir}/libfuturize
%{py_puresitedir}/libpasteurize

%files -n python2-%{pypi_name}
%{_bindir}/python2-futurize
%{_bindir}/python2-pasteurize
%doc README.rst docs/_themes/LICENSE LICENSE.txt
%{py_puresitedir}/%{pypi_name}-%{version}-py?.?.egg-info
%{py_puresitedir}/%{pypi_name}
%{py_puresitedir}/past
%{py_puresitedir}/libfuturize
%{py_puresitedir}/libpasteurize
%{py_puresitedir}/builtins
%{py_puresitedir}/configparser
%{py_puresitedir}/copyreg
%{py_puresitedir}/html
%{py_puresitedir}/http
%{py_puresitedir}/queue
%{py_puresitedir}/reprlib
%{py_puresitedir}/socketserver
%{py_puresitedir}/tkinter
%{py_puresitedir}/_dummy_thread
%{py_puresitedir}/_markupbase
%{py_puresitedir}/_thread
%{py_puresitedir}/winreg
%{py_puresitedir}/xmlrpc

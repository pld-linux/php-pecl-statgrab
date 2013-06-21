%define		php_name	php%{?php_suffix}
%define		modname	statgrab
%define		status		stable
Summary:	%{modname} - libstatgrab bindings
Summary(pl.UTF-8):	%{modname} - dowiązania biblioteki libstatgrab
Name:		%{php_name}-pecl-%{modname}
Version:	0.6.0
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	5e8e659e28d95da57c3d5a694cfb5af4
URL:		http://pecl.php.net/package/statgrab/
BuildRequires:	libstatgrab-devel >= 0.10
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libstatgrab is a library that provides a common interface for
retrieving a variety of system statistics on a number of *NIX like
systems.

This extension allows you to call the functions made available by
libstatgrab library.

In PECL status of this package is: %{status}.

%description -l pl.UTF-8
libstatgrab to biblioteka dostarczająca wspólny interfejs do
odczytywania różnych statystyk systemowych na wielu systemach
uniksowych.

To rozszerzenie pozwala wywoływać funkcje udostępniane przez
bibliotekę libstatgrab.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv Statgrab-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so

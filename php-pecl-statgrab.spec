%define		_modname	statgrab
%define		_smodname	Statgrab
%define		_status		beta

Summary:	%{_modname} - libstatgrab bindings
Summary(pl):	%{_modname} - dowi±zania biblioteki libstatgrab
Name:		php-pecl-%{_modname}
Version:	0.3
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	c2dd8a7f74de55ef273f96fc9e271512
URL:		http://pecl.php.net/package/statgrab/
BuildRequires:	libtool
BuildRequires:	libstatgrab-devel >= 0.10
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
libstatgrab is a library that provides a common interface for
retrieving a variety of system statistics on a number of *NIX like
systems.

This extension allows you to call the functions made available by
libstatgrab library. 

In PECL status of this package is: %{_status}.

%description -l pl
libstatgrab to biblioteka dostarczaj±ca wspólny interfejs do
odczytywania ró¿nych statystyk systemowych na wielu systemach
uniksowych.

To rozszerzenie pozwala wywo³ywaæ funkcje udostêpniane przez
bibliotekê libstatgrab.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_smodname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_smodname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_smodname}-%{version}/CREDITS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so

%define		ocaml_ver	1:3.10.0
Summary:	OCaml bindings for the libssl
Summary(pl.UTF-8):	Wiązania OpenSSL do OCamla
Name:		ocaml-ssl
Version:	0.4.5
Release:	5
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	http://dl.sourceforge.net/savonet/%{name}-%{version}.tar.gz
# Source0-md5:	a75899dabd555b7196bef9124385e65e
URL:		http://savonet.sourceforge.net/
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
BuildRequires:	openssl-devel
BuildRequires:	which
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OCaml bindings for the libssl.

%description -l pl.UTF-8
Wiązania OpenSSL do OCamla.

%package devel
Summary:	OCaml bindings for the libssl
Summary(pl.UTF-8):	Wiązania OpenSSL do OCamla
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
OCaml bindings for the libssl.

%description devel -l pl.UTF-8
Wiązania OpenSSL do OCamla.

%prep
%setup -q

%build
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{ssl,stublibs}

install src/*.cm[ixa]* src/*.a $RPM_BUILD_ROOT%{_libdir}/ocaml/ssl
install src/*.so $RPM_BUILD_ROOT%{_libdir}/ocaml/stublibs

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# META for findlib
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ssl
install src/META $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ssl
echo 'directory = "+ssl"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/ssl/META

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%dir %{_libdir}/ocaml/ssl
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc doc/html src/*.mli
%{_libdir}/ocaml/ssl/*.cm[ixa]*
%{_libdir}/ocaml/ssl/*.a
%{_libdir}/ocaml/site-lib/ssl
%{_examplesdir}/%{name}-%{version}

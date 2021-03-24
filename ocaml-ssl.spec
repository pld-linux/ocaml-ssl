%define		ocaml_ver	1:3.10.0
Summary:	OCaml bindings for the libssl
Summary(pl.UTF-8):	Wiązania OpenSSL do OCamla
Name:		ocaml-ssl
Version:	0.5.10
Release:	1
License:	LGPL + OCaml linking exception
Group:		Libraries
Source0:	https://github.com/savonet/ocaml-ssl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	afebbdc3130c1addf1da31e3b92c1dcd
URL:		https://github.com/savonet/ocaml-ssl
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-dune
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
%requires_eq ocaml

%description devel
OCaml bindings for the libssl.

%description devel -l pl.UTF-8
Wiązania OpenSSL do OCamla.

%prep
%setup -q

%build
dune build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{ssl,stublibs}

dune install  --destdir $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README.md
%dir %{_libdir}/ocaml/ssl
%{_libdir}/ocaml/ssl/META
%{_libdir}/ocaml/ssl/dune-package
%{_libdir}/ocaml/ssl/opam
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc src/*.mli
%{_libdir}/ocaml/ssl/*.cm[ixa]*
%{_libdir}/ocaml/ssl/*.a
%{_libdir}/ocaml/ssl/ssl.cmt
%{_libdir}/ocaml/ssl/ssl.cmti
%{_libdir}/ocaml/ssl/ssl.mli
%{_libdir}/ocaml/ssl/ssl_threads.cmt
%{_libdir}/ocaml/ssl/ssl_threads.cmti
%{_libdir}/ocaml/ssl/ssl_threads.mli
%{_examplesdir}/%{name}-%{version}

#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	OCaml bindings for the libssl
Summary(pl.UTF-8):	Wiązania OpenSSL do OCamla
Name:		ocaml-ssl
Version:	0.5.10
Release:	3
License:	LGPL v2.1 + OCaml linking exception
Group:		Libraries
#Source0Download: https://github.com/savonet/ocaml-ssl/releases
Source0:	https://github.com/savonet/ocaml-ssl/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	afebbdc3130c1addf1da31e3b92c1dcd
URL:		https://github.com/savonet/ocaml-ssl
BuildRequires:	ocaml >= 1:4.02.0
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	openssl-devel
BuildRequires:	which
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OCaml bindings for the libssl.

%description -l pl.UTF-8
Wiązania OpenSSL do OCamla.

%package devel
Summary:	OCaml bindings for the libssl - development part
Summary(pl.UTF-8):	Wiązania OpenSSL do OCamla - część programistyczna
Group:		Development/Libraries
%requires_eq ocaml

%description devel
OCaml bindings for the libssl - development part.

%description devel -l pl.UTF-8
Wiązania OpenSSL do OCamla - część programistyczna.

%prep
%setup -q

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/{ssl,stublibs}

dune install --destdir $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ssl/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ssl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md COPYING README.md
%dir %{_libdir}/ocaml/ssl
%{_libdir}/ocaml/ssl/META
%{_libdir}/ocaml/ssl/dune-package
%{_libdir}/ocaml/ssl/opam
%attr(755,root,root) %{_libdir}/ocaml/stublibs/dllssl_stubs.so
%{_libdir}/ocaml/ssl/*.cma
%if %{with ocaml_opt}
%{_libdir}/ocaml/ssl/ssl.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ssl/*.cmi
%{_libdir}/ocaml/ssl/ssl.cmt
%{_libdir}/ocaml/ssl/ssl.cmti
%{_libdir}/ocaml/ssl/ssl.mli
%{_libdir}/ocaml/ssl/ssl_threads.cmt
%{_libdir}/ocaml/ssl/ssl_threads.cmti
%{_libdir}/ocaml/ssl/ssl_threads.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/ssl/*.a
%{_libdir}/ocaml/ssl/*.cmx
%{_libdir}/ocaml/ssl/*.cmxa
%endif
%{_examplesdir}/%{name}-%{version}

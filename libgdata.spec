Summary:	GData access library
Name:		libgdata
Version:	0.4.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgdata/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	06b14f1cd96432b0717ed03fe013ca4d
URL:		http://www.gnumeric.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7.1
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-common
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libsoup-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgdata is a GLib-based library for accessing online service APIs using the
GData protocol - most notably, Google's services. It provides APIs to access
the common Google services, and has full asynchronous support.

%package devel
Summary:	Support files necessary to compile applications with libgdata
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libsoup-devel
Requires:	libxml2-devel >= 1:2.6.26

%description devel
Headers, and support files necessary to compile applications using
libgdata.

%package static
Summary:	libgdata static libraries
Summary(pl.UTF-8):	Statyczne biblioteki libgsf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Package contains static libraries.

%package apidocs
Summary:	libgdata API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libgdata API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gdata

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f gdata.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%attr(755,root,root) %{_libdir}/libgdata.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgdata.so.5

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdata.so
%{_libdir}/libgdata.la
%{_includedir}/libgdata
%{_pkgconfigdir}/libgdata.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdata.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdata

Summary:	Utility to convert an Alcohol 120% bin images to ISO-9660 format
Summary(pl):	Narz�dzie do konwertowania obraz�w wykonanych przez program Alcohol 120% na format ISO-9660
Name:		mdf2iso
Version:	0.3.0
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://download.berlios.de/mdf2iso/%{name}-%{version}-src.tar.bz2
# Source0-md5:	a190625318476a196930ac66acd8fd07
URL:		http://mdf2iso.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to convert an Alcohol 120% bin images to ISO-9660 format.

%description -l pl
Narz�dzie do konwertowania obraz�w wykonanych przez program Alcohol
120% na format ISO-9660.

%prep
%setup -q -n %{name}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
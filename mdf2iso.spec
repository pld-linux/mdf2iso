Summary:	Utility to convert an Alcohol 120% bin image to ISO-9660 format
Summary(pl):	Narzêdzie do konwertowania obrazu wykonanego przez program Alcohol 120% na format ISO-9660
Name:		mdf2iso
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://download.berlios.de/mdf2iso/%{name}-%{version}-src.tar.bz2
# Source0-md5:	2996ad87d45916a5e4998bb42e512139
URL:		http://mdf2iso.berlios.de/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to convert an Alcohol 120% bin image to ISO-9660 format.

%description -l pl
Narzêdzie do konwertowania obrazu wykonanego przez program Alcohol
120% na format ISO-9660.

%prep
%setup -q -n %{name}-%{version}-src

%build
%{__cc} %{rpmcflags} src/mdf2iso.c -o mdf2iso

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mdf2iso $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/*

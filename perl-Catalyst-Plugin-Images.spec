%define module Catalyst-Plugin-Images
%define name	perl-%{module}
%define version	0.02
%define release	%mkrel 1

Summary:	Generate image tags for static files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Catalyst/%{module}-%{version}.tar.gz
BuildRequires:	perl(Catalyst) >= 5.50
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(Image::Size)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Test::use::ok)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This plugin aims to assist you in generating image tags that contain
alt text, a properly escaped src attribute, height and width info,
without worrying too much.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

%clean
rm -rf %{buildroot}


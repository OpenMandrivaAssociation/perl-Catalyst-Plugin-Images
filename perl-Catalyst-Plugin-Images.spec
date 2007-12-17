%define realname Catalyst-Plugin-Images
%define name	perl-%{realname}
%define version	0.01
%define release	%mkrel 3

Summary:	Generate image tags for static files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Catalyst/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%else
BuildRequires:	perl >= 5.8.1
%endif
BuildRequires:	perl(Catalyst) >= 5.50
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(Image::Size)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Test::use::ok)
Requires:	perl >= 5.8.1
BuildArch:	noarch

%description
This plugin aims to assist you in generating image tags that contain
alt text, a properly escaped src attribute, height and width info,
without worrying too much.


%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

%clean
rm -rf %{buildroot}


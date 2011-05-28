%define upstream_name    Catalyst-Plugin-Images
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Generate image tags for static files
License:	Artistic/GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst) >= 5.50
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(Image::Size)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:  perl(Test::use::ok)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This plugin aims to assist you in generating image tags that contain
alt text, a properly escaped src attribute, height and width info,
without worrying too much.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst

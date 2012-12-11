%define upstream_name    Catalyst-Plugin-Images
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Generate image tags for static files
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst) >= 5.50
BuildRequires:	perl(HTML::Entities)
BuildRequires:	perl(Image::Size)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl(Test::use::ok)
BuildArch:	noarch

%description
This plugin aims to assist you in generating image tags that contain
alt text, a properly escaped src attribute, height and width info,
without worrying too much.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 680749
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 406264
- rebuild using %%perl_convert_version

* Sun Jan 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.1
+ Revision: 333423
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.01-5mdv2009.0
+ Revision: 241161
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdv2008.0
+ Revision: 86057
- rebuild


* Tue May 09 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-2mdk
- Add BuildRequires

* Mon May 08 2006 Scott Karns <scottk@mandriva.org> 0.01-1mdk
- First Mandriva release


%define upstream_name Shell-Config-Generate
%define upstream_version 0.33

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    Portably generate config for any shell
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Shell/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Shell::Guess) >= 0.20.0
BuildRequires: perl(Test2::API) >= 1.302.15
#BuildRequires: perl(Test2::Mock) >= 0.0.60
#BuildRequires: perl(Test2::V0) >= 0.0.60
BuildRequires: perl(base)
BuildArch:  noarch

%description
This module provides an interface for specifying shell configurations
for different shell environments without having to worry about the
arcane differences between shells such as csh, sh, cmd.exe and
command.com.

It does not modify the current environment, but it can be used to
create shell configurations which do modify the environment.

%prep
%autosetup -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make_build

%install
%make_install

%files
%doc Changes INSTALL LICENSE META.json META.yml MYMETA.yml README example
%{_mandir}/man3/*
%{perl_vendorlib}/*

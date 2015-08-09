#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Changes
%include	/usr/lib/rpm/macros.perl
Summary:	Test::CPAN::Changes - Validation of the Changes file in a CPAN distribution
Summary(pl.UTF-8):	Test::CPAN::Changes - sprawdzanie poprawności pliku Changes w dystrybucji CPAN
Name:		perl-CPAN-Changes
Version:	0.400002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5773d51abaafd37c6bcdde3827873075
URL:		http://search.cpan.org/dist/CPAN-Changes/
BuildRequires:	perl-devel >= 1:5.10.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.59
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-version >= 0.79
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows CPAN authors to write automated tests to ensure
their changelogs match the specification.

%description -l pl.UTF-8
Ten moduł pozwala autorom CPAN tworzyć automatyczne testy sprawdzające
zgodność plików logów zmian ze specyfikacją.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/tidy_changelog
%{perl_vendorlib}/CPAN/Changes.pm
%{perl_vendorlib}/CPAN/Changes
%dir %{perl_vendorlib}/Test/CPAN
%{perl_vendorlib}/Test/CPAN/Changes.pm
%{_mandir}/man1/tidy_changelog.1p*
%{_mandir}/man3/CPAN::Changes*.3pm*
%{_mandir}/man3/Test::CPAN::Changes.3pm*

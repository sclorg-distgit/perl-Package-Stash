%{?scl:%scl_package perl-Package-Stash}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_Package_Stash_enables_optional_test
%else
%bcond_with perl_Package_Stash_enables_optional_test
%endif

Name:		%{?scl_prefix}perl-Package-Stash
Version:	0.38
Release:	5%{?dist}
Summary:	Routines for manipulating stashes
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Package-Stash
Source0:	https://cpan.metacpan.org/modules/by-module/Package/Package-Stash-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl-interpreter
BuildRequires:	%{?scl_prefix}perl(Config)
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(File::Spec)
BuildRequires:	%{?scl_prefix}perl(Text::ParseWords)
# Module Runtime
BuildRequires:	%{?scl_prefix}perl(B)
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(constant)
BuildRequires:	%{?scl_prefix}perl(Dist::CheckConflicts) >= 0.02
BuildRequires:	%{?scl_prefix}perl(Getopt::Long)
BuildRequires:	%{?scl_prefix}perl(Module::Implementation) >= 0.06
BuildRequires:	%{?scl_prefix}perl(Package::Stash::XS) >= 0.26
BuildRequires:	%{?scl_prefix}perl(Scalar::Util)
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(Symbol)
BuildRequires:	%{?scl_prefix}perl(warnings)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(base)
BuildRequires:	%{?scl_prefix}perl(IO::Handle)
BuildRequires:	%{?scl_prefix}perl(IPC::Open3)
BuildRequires:	%{?scl_prefix}perl(lib)
BuildRequires:	%{?scl_prefix}perl(Test::Fatal)
BuildRequires:	%{?scl_prefix}perl(Test::More) >= 0.88
BuildRequires:	%{?scl_prefix}perl(Test::Requires)
%if %{with perl_Package_Stash_enables_optional_test}
# Optional Tests
BuildRequires:	%{?scl_prefix}perl(CPAN::Meta) >= 2.120900
BuildRequires:	%{?scl_prefix}perl(Package::Anon)
BuildRequires:	%{?scl_prefix}perl(Variable::Magic)
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
# For performance and consistency
Requires:	%{?scl_prefix}perl(Package::Stash::XS) >= 0.26
# Not found by rpm auto-provides
Provides:	%{?scl_prefix}perl(Package::Stash::Conflicts) = 0

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that behind
a simple API.

%prep
%setup -q -n Package-Stash-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%if 0%{?_licensedir:1}
%doc LICENSE
%else
%doc LICENSE
%endif
%doc Changes CONTRIBUTING README
%{_bindir}/package-stash-conflicts
%{perl_vendorlib}/Package/
%{_mandir}/man1/package-stash-conflicts.1*
%{_mandir}/man3/Package::Stash.3*
%{_mandir}/man3/Package::Stash::PP.3*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-5
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-3
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan  2 2019 Paul Howarth <paul@city-fan.org> - 0.38-1
- Update to 0.38
  - Avoid new warning in 5.21.x regarding too many arguments for printf/sprintf
  - Canonical repository moved to https://github.com/moose/Package-Stash
- Package new CONTRIBUTING file
- Specify all build dependencies
- Don't bother running the extra tests
- Simplify find command using -delete
- Drop EL-5 support
  - Drop legacy Group: tag
  - Drop explicit buildroot cleaning in %%install section
  - Drop workaround for building with Test::More < 0.88

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-10
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-7
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-5
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-2
- Perl 5.22 rebuild

* Tue Sep 23 2014 Paul Howarth <paul@city-fan.org> - 0.37-1
- Update to 0.37
  - Fix spurious warning in taint mode (GH#12)
- Update patch for building with old Test::More versions
- No documentation for Package::Stash::Conflicts in this release
- Classify buildreqs by usage
- Use %%doc where possible
- Don't try to run the extra tests for EL builds as we won't have the
  dependencies

* Fri Aug 29 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.36-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep  4 2013 Paul Howarth <paul@city-fan.org> - 0.36-1
- Update to 0.36
  - Support building with PUREPERL_ONLY
- BR: perl(Config), perl(Text::ParseWords) and perl(Variable::Magic)
- Update patch for building with old Test::More version in EPEL-5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Pisar <ppisar@redhat.com> - 0.35-2
- Perl 5.18 rebuild

* Wed Jul 10 2013 Paul Howarth <paul@city-fan.org> - 0.35-1
- Update to 0.35
  - Remove old, deprecated API
- BR: perl(Getopt::Long)
- perl(Package::DeprecationManager) is no longer needed

* Thu Jan 24 2013 Paul Howarth <paul@city-fan.org> - 0.34-2
- BR: perl(Package::Anon) if we have Perl ≥ 5.14

* Sun Jan  6 2013 Paul Howarth <paul@city-fan.org> - 0.34-1
- Update to 0.34
  - Support anonymous stashes on newer perl versions
  - Prevent harmful effects from invalid settings for
    $ENV{PACKAGE_STASH_IMPLEMENTATION}
  - Switch to Module::Implementation
- BR: perl(Module::Implementation) ≥ 0.06
- BR: perl(base) for test suite
- Bump Package::Stash::XS version requirement to 0.26
- Explicitly run extra tests (except on RHEL ≥ 7, where the necessary
  build dependencies may not be available)
- Update patch for building with old Test::More version in EPEL-5

* Mon Aug 27 2012 Petr Pisar <ppisar@redhat.com> - 0.33-7
- Disable author tests on RHEL >= 7

* Fri Aug 24 2012 Paul Howarth <paul@city-fan.org> - 0.33-6
- Drop EPEL-4 support
  - Drop %%defattr, redundant since rpm 4.4
  - Test::LeakTrace, Test::Requires and Test::Script are now universally available
  - A suitably recent version of ExtUtils::MakeMaker is now universally available
- Don't need to remove empty directories from the buildroot

* Tue Aug 14 2012 Petr Pisar <ppisar@redhat.com> - 0.33-5
- Specify all dependendencies

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Petr Pisar <ppisar@redhat.com> - 0.33-3
- Perl 5.16 rebuild

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 0.33-2
- Fedora 17 mass rebuild

* Thu Sep 29 2011 Paul Howarth <paul@city-fan.org> - 0.33-1
- Update to 0.33
  - Add conflict on MooseX::Method::Signatures 0.36
- BR: perl(Carp)

* Tue Sep  6 2011 Paul Howarth <paul@city-fan.org> - 0.32-1
- Update to 0.32
  - Bring the behavior of has_symbol for nonexistant scalars into line with the
    XS version
  - Invalid package names (for instance, Foo:Bar) are not allowed
  - Invalid stash entry names (anything containing ::) are not allowed
- Update patches to apply cleanly
- Bump perl(Package::Stash::XS) version requirement to 0.24

* Tue Aug  9 2011 Paul Howarth <paul@city-fan.org> - 0.31-1
- Update to 0.31
  - Fix ->add_symbol('$foo', qr/sdlfk/) on 5.12+
  - Fix ->add_symbol('$foo', \v1.2.3) on 5.10+
- Update patch for old Test::More versions
- Update patch for no Test::Requires

* Thu Jul 21 2011 Paul Howarth <paul@city-fan.org> - 0.30-2
- Perl mass rebuild

* Thu Jul 21 2011 Paul Howarth <paul@city-fan.org> - 0.30-1
- Update to 0.30
  - Fix compiler detection in Makefile.PL
- Update patch for old ExtUtils::MakeMaker versions
- Drop usage of macros for commands
- Drop redundant %%{?perl_default_filter}
- perl(Pod::Coverage::TrustPod) now available everywhere

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.29-2
- Perl mass rebuild

* Wed Apr  6 2011 Paul Howarth <paul@city-fan.org> - 0.29-1
- Update to 0.29
  - Really skip the package-stash-conflict script in the compile test

* Wed Mar 30 2011 Paul Howarth <paul@city-fan.org> - 0.28-1
- Update to 0.28
  - META.json fixes
- Update patch for old ExtUtils::MakeMaker versions to apply cleanly

* Mon Mar 28 2011 Paul Howarth <paul@city-fan.org> - 0.27-1
- Update to 0.27
  - Skip the package-stash-conflicts script in the compile test

* Sat Mar  5 2011 Paul Howarth <paul@city-fan.org> - 0.26-1
- Update to 0.26
  - Make the namespace cache lazy and weak, in case the stash is deleted
  - However, this doesn't work on 5.8, so disable the namespace caching
    entirely there
- Update patches to apply cleanly
- Bump perl(Package::Stash::XS) version requirement to 0.22
- Bump perl(Dist::CheckConflicts) version requirement to 0.02

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 25 2011 Paul Howarth <paul@city-fan.org> - 0.25-1
- Update to 0.25 (make the leak tests author-only, since some smokers run
  release tests)
- Update patches to apply cleanly
- Bump perl(Package::Stash::XS) version requirement to 0.21
- Drop buildreq perl(Test::Exception), no longer needed

* Tue Jan 18 2011 Paul Howarth <paul@city-fan.org> - 0.24-1
- Update to 0.24 (reinstate Test::Requires dependency)

* Wed Jan 12 2011 Paul Howarth <paul@city-fan.org> - 0.23-1
- Update to 0.23
  - Lower perl prereq to 5.8.1
  - Make the leak tests release-only
- Update patches to apply cleanly
- Add patch to skip memory leak tests if we don't have Test::LeakTrace

* Thu Jan  6 2011 Paul Howarth <paul@city-fan.org> - 0.22-1
- Update to 0.22 (bump Package::Stash::XS version requirement since a bug was
  fixed there)
- Update patches for old ExtUtils::MakeMaker and Test::More versions
- BR/R perl(Package::Stash::XS) >= 0.19
- Content-free manpages for package-stash-conflicts and
  Package::Stash::Conflicts dropped upstream

* Tue Jan  4 2011 Paul Howarth <paul@city-fan.org> - 0.20-1
- Update to 0.20
  - Methods were renamed for brevity: s/_package//
  - Convert Package::Stash into a module which loads either the XS or pure perl
    implementation, depending on what's available
  - Use Test::Fatal instead of Test::Exception
  - Use Dist::CheckConflicts
  - Silence deprecation warnings for the method renaming for now
- New script and manpage: package-stash-conflicts
- New modules and manpages: Package::Stash::Conflicts and Package::Stash::PP
- New build requirements:
  - perl(Dist::CheckConflicts)
  - perl(Package::DeprecationManager)
  - perl(Package::Stash::XS)
  - perl(Test::LeakTrace)
  - perl(Test::Requires)
  - perl(Test::Script)
- Update patches for old ExtUtils::MakeMaker and Test::More versions
- Add new patch to work around absence of Test::Requires in EPEL-4
- Require perl(Package::Stash::XS) for performance and consistency
- Manually provide perl(Package::Stash::Conflicts), hidden from auto-provides

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.08-2
- Rebuild to fix problems with vendorarch/lib (#661697)

* Mon Sep 20 2010 Paul Howarth <paul@city-fan.org> - 0.08-1
- Update to 0.08 (re-enable the caching of the stash)
- Update patch for old ExtUtils::MakeMaker and Test::More versions

* Wed Jun 16 2010 Paul Howarth <paul@city-fan.org> - 0.05-1
- Update to 0.05
  - Bump Test::More requirement for done_testing
  - Update packaging stuff
- BR: perl(Test::EOL) and perl(Test::NoTabs)
- Unify spec for all active branches, adding patches for back-compatibility

* Mon Jun 14 2010 Paul Howarth <paul@city-fan.org> - 0.04-1
- Update to 0.04 (get_package_symbol now doesn't autovivify stash entries; a
  new method get_or_add_package_symbol can now be used for that behavior)

* Mon Jun 14 2010 Paul Howarth <paul@city-fan.org> - 0.03-2
- Incorporate package review suggestions (#602597)
  - Use %%{?perl_default_filter}
  - Use DESTDIR instead of PERL_INSTALL_ROOT

* Mon Jun  7 2010 Paul Howarth <paul@city-fan.org> - 0.03-1
- Initial RPM version

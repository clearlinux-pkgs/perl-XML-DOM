#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-DOM
Version  : 1.46
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-DOM-1.46.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-DOM-1.46.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-DOM-perl = %{version}-%{release}
Requires: perl(XML::RegExp)
BuildRequires : buildreq-cpan
BuildRequires : perl(LWP::UserAgent)
BuildRequires : perl(XML::Parser)
BuildRequires : perl(XML::Parser::PerlSAX)
BuildRequires : perl(XML::RegExp)

%description
Perl module: XML-DOM
All rights reserved.
This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-XML-DOM package.
Group: Development
Provides: perl-XML-DOM-devel = %{version}-%{release}
Requires: perl-XML-DOM = %{version}-%{release}

%description dev
dev components for the perl-XML-DOM package.


%package perl
Summary: perl components for the perl-XML-DOM package.
Group: Default
Requires: perl-XML-DOM = %{version}-%{release}

%description perl
perl components for the perl-XML-DOM package.


%prep
%setup -q -n XML-DOM-1.46
cd %{_builddir}/XML-DOM-1.46

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::DOM.3
/usr/share/man/man3/XML::DOM::AttDef.3
/usr/share/man/man3/XML::DOM::AttlistDecl.3
/usr/share/man/man3/XML::DOM::Attr.3
/usr/share/man/man3/XML::DOM::CDATASection.3
/usr/share/man/man3/XML::DOM::CharacterData.3
/usr/share/man/man3/XML::DOM::Comment.3
/usr/share/man/man3/XML::DOM::DOMImplementation.3
/usr/share/man/man3/XML::DOM::Document.3
/usr/share/man/man3/XML::DOM::DocumentFragment.3
/usr/share/man/man3/XML::DOM::DocumentType.3
/usr/share/man/man3/XML::DOM::Element.3
/usr/share/man/man3/XML::DOM::ElementDecl.3
/usr/share/man/man3/XML::DOM::Entity.3
/usr/share/man/man3/XML::DOM::EntityReference.3
/usr/share/man/man3/XML::DOM::NamedNodeMap.3
/usr/share/man/man3/XML::DOM::Node.3
/usr/share/man/man3/XML::DOM::NodeList.3
/usr/share/man/man3/XML::DOM::Notation.3
/usr/share/man/man3/XML::DOM::Parser.3
/usr/share/man/man3/XML::DOM::PerlSAX.3
/usr/share/man/man3/XML::DOM::ProcessingInstruction.3
/usr/share/man/man3/XML::DOM::Text.3
/usr/share/man/man3/XML::DOM::XMLDecl.3
/usr/share/man/man3/XML::Handler::BuildDOM.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM.pm
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/AttDef.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/AttlistDecl.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Attr.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/CDATASection.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/CharacterData.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Comment.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/DOMException.pm
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/DOMImplementation.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Document.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/DocumentFragment.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/DocumentType.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Element.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/ElementDecl.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Entity.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/EntityReference.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/NamedNodeMap.pm
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/NamedNodeMap.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Node.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/NodeList.pm
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/NodeList.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Notation.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Parser.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/PerlSAX.pm
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/ProcessingInstruction.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/Text.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/DOM/XMLDecl.pod
/usr/lib/perl5/vendor_perl/5.30.2/XML/Handler/BuildDOM.pm

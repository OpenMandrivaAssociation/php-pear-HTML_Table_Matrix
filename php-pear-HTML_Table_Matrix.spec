%define		_class		HTML
%define		_subclass	Table
%define		upstream_name	%{_class}_%{_subclass}_Matrix

Name:		php-pear-%{upstream_name}
Version:	1.0.10
Release:	6
Summary:	Autofill a table with data
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Table_Matrix/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
HTML_Table_Matrix is an extension to HTML_Table which allows you to
easily fill up a table with data. Features:
- It uses Filler classes to determine how the data gets filled in the
  table. With a custom Filler, you can fill data in up, down,
  forwards, backwards, diagonally, randomly or any other way you like.
- Comes with Fillers to fill left-to-right-top-to-bottom and
  right-to-left-top-to-bottom.
- Abstract Filler methods keep the code clean & easy to understand.
- Table height or width may be omitted, and it will figure out the
  correct table size based on the data you provide.
- It integrates handily with Pager to create pleasant pageable table
  layouts, such as for an image gallery. Just specify a height or
  width, Filler, and feed it the data returned from Pager.
- Table may be constrained to a specific height or width, and excess
  data will be ignored.
- Fill offset may be specified, to leave room for a table header, or
  other elements in the table.
- Fully documented with PHPDoc.
- Includes fully functional example code.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/examples

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-5mdv2012.0
+ Revision: 742004
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-4
+ Revision: 679355
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.10-3mdv2011.0
+ Revision: 613681
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-2mdv2010.1
+ Revision: 477885
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sat Sep 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.10-1mdv2010.0
+ Revision: 449321
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.0.9-5mdv2010.0
+ Revision: 441180
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-4mdv2009.1
+ Revision: 322122
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-3mdv2009.0
+ Revision: 236881
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.0.9-2mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Nov 12 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-2mdv2007.0
+ Revision: 83325
- rebuild

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-1mdv2007.1
+ Revision: 81686
- Import php-pear-HTML_Table_Matrix

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.9-1mdk
- 1.0.9
- new group (Development/PHP)

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.8-1mdk
- 1.0.8

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-1mdk
- 1.0.7

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.6-1mdk
- initial Mandriva package (PLD import)


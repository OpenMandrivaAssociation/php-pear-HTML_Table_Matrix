%define		_class		HTML
%define		_subclass	Table
%define		upstream_name	%{_class}_%{_subclass}_Matrix

Name:		php-pear-%{upstream_name}
Version:	1.0.10
Release:	%mkrel 5
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
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/examples

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{upstream_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml

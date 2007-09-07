%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	LV
%define		_status		stable
%define		_pearname	Validate_LV

Summary:	%{_pearname} - Validation class for Latvia
Summary(pl.UTF-8):	%{_pearname} - klasa sprawdzająca poprawność dla Łotwy
Name:		php-pear-%{_pearname}
Version:	1.0.0
Release:	1
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8b4e87ea5fab464bcbc3bef51999aa55
URL:		http://pear.php.net/package/Validate_LV/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-PEAR >= 1.4.0b1
Requires:	php-pear-Validate >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data validation class for Latvia. Provides methods to validate:
 - VAT number
 - Registration number
 - Swift code
 - Telephone number
 - Person ID
 - IBAN Bank account number for Latvian Banks
 - Postal code
 - Passport
 - Person name

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności dla Łotwy danych takich jak:
 - numer VAT,
 - numer rejestracyjny,
 - kod swift,
 - numer telefonu,
 - osobisty numer identyfikacyjny,
 - numer IBAN konta bankowego dla banków łotewskich,
 - kod pocztowy,
 - paszport,
 - imię

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/LV.php

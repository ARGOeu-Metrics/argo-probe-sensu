%define underscore() %(echo %1 | sed 's/-/_/g')

Summary:       ARGO probe that generates list of hostnames with a given service in status OK
Name:          argo-probe-sensu
Version:       0.3.0
Release:       1%{?dist}
Source0:       %{name}-%{version}.tar.gz
License:       ASL 2.0
Group:         Development/System
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix:        %{_prefix}
BuildArch:     noarch

BuildRequires: python3-devel
Requires: python3-requests


%description
ARGO probe that generates list of hostnames with a given service in status OK

%prep
%setup -q


%build
%{py3_build}


%install
%{py3_install "--record=INSTALLED_FILES" }


%clean
rm -rf $RPM_BUILD_ROOT


%files -f INSTALLED_FILES
%defattr(-,root,root)
%dir %{python3_sitelib}/%{underscore %{name}}/
%{python3_sitelib}/%{underscore %{name}}/*.py


%changelog
* Thu Jun 27 2024 Katarina Zailac <kzailac@srce.hr> - 0.2.0-1%{?dist}
- AO-982 Create el9 rpm for argo-probe-sensu
* Thu Feb 1 2024 Katarina Zailac <kzailac@srce.hr> - 0.1.0-1%{?dist}
- ARGO-4462 Hostnames saved into file without newline
- ARGO-4461 Create probe to replace argo-probe-nagios

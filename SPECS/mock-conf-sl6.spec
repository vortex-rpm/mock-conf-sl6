%define debug_package %{nil}

Summary:	Mock configs for SL6
Name:		mock-conf-sl6
Version:	4
Release:	1.vortex%{?dist}
Vendor:		Vortex RPM
License:	GPLv3
Group:		Development/Tools
URL:		http://vortex-rpm.org/
Source0:	sl-6-x86_64.cfg
Source1:	sl-6-i386.cfg
Requires:	mock
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This package contains Scientific Linux 6 configuration files for mock.

The additional repositories are:
- EPEL
- IUS
- Vortex
- Vortex (noarch)

%prep
%setup -q -c -T

%build

%install
rm -rf %{buildroot}
install -D -p -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/mock/sl-6-x86_64.cfg
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/sl-6-i386.cfg

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,mock,-)
%config(noreplace) %{_sysconfdir}/mock/sl-6-x86_64.cfg
%config(noreplace) %{_sysconfdir}/mock/sl-6-i386.cfg

%changelog
* Fri Apr  4 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 4-1.vortex
- Add vortex-noarch repo.

* Tue Apr  1 2014 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 3-1.vortex
- Switch to more convenient mirrors on sl and sl-security.

* Sun Mar  3 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 2-1.vortex
- Add IUS and Vortex.

* Thu Nov 17 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1-2.vortex
- Fix files ownership.
- Move from custom mirrorlist to official baseurl.

* Tue Sep 09 2011 Ilya A. Otyutskiy <sharp@thesharp.ru> - 1-1.vortex
- Initial packaging for Enterprise Linux.

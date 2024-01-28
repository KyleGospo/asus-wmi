%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     asus-wmi
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Asus PC WMI hotkey driver
License:  GPLv2
URL:      https://github.com/KyleGospo/asus-wmi

Source:   %{url}/archive/refs/heads/main.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}

BuildRequires: systemd-rpm-macros

%description
Asus PC WMI hotkey driver

%prep
%setup -q -c %{name}-main

%files
%doc %{name}-main/README.md
%license %{name}-main/LICENSE

%changelog
{{{ git_dir_changelog }}}

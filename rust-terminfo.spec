# Generated by rust2rpm
# https://github.com/meh/rust-terminfo/issues/10
%bcond_with check
%global debug_package %{nil}

%global crate terminfo

Name:           rust-%{crate}
Version:        0.6.1
Release:        3%{?dist}
Summary:        Terminal information

# https://github.com/meh/rust-terminfo/issues/9
License:        WTFPL
URL:            https://crates.io/crates/terminfo
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(fnv/default) >= 1.0.0 with crate(fnv/default) < 2.0.0)
BuildRequires:  (crate(nom/default) >= 4.0.0 with crate(nom/default) < 5.0.0)
BuildRequires:  (crate(phf/default) >= 0.7.0 with crate(phf/default) < 0.8.0)
BuildRequires:  (crate(phf_codegen/default) >= 0.7.0 with crate(phf_codegen/default) < 0.8.0)

%global _description \
Terminal information.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 17:11:32 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.1-1
- Initial package

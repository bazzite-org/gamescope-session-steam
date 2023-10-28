Name:           gamescope-session-steam
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Steam Big Picture session

License:        MIT
URL:            https://github.com/KyleGospo/gamescope-session-steam

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}
BuildArch:      noarch

Requires:       gamescope-session-plus

BuildRequires:  systemd-rpm-macros

%description
Steam Big Picture session

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build

%install
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/
cp -rv usr/bin/* %{buildroot}%{_bindir}
cp -rv usr/share/* %{buildroot}%{_datadir}
rm -rf %{buildroot}%{_bindir}/steamos-polkit-helpers
rm %{buildroot}%{_bindir}/jupiter-biosupdate
rm %{buildroot}%{_bindir}/steamos-session-select
rm %{buildroot}%{_bindir}/steamos-update

# Do post-installation
%post

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%{_bindir}/steam-http-loader
%{_bindir}/steamos-select-branch
%{_datadir}/applications/gamescope-mimeapps.list
%{_datadir}/applications/steam_http_loader.desktop
%{_datadir}/gamescope-session-plus/sessions.d/steam
%{_datadir}/polkit-1/actions/org.chimeraos.update.policy
%{_datadir}/wayland-sessions/gamescope-session-steam.desktop
%{_datadir}/wayland-sessions/gamescope-session.desktop

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}

Name: smorg-nagios-plugins
Version: 1.4.16
Release: 1
Summary: Host/service/network monitoring program plugins for Nagios

Group: Applications/System
License: GPL
URL: http://nagiosplug.sourceforge.net/
Source0: http://dl.sf.net/sourceforge/nagiosplug/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Prefix: %{_prefix}/lib64/nagios/plugins
Packager: Mark Clarkson <mark.clarkson@smorg.co.uk>
Vendor: Smorg
Summary: Nagios Plugins for x86_64 Linux Servers

Provides: smorg-nagios-plugins
Conflicts: nagios-plugins
%{!?custom:%global custom 0}
Obsoletes: nagios-plugins-custom nagios-plugins-extras
AutoReq: no
Requires: perl, perl(Net::SNMP), net-snmp

BuildRequires: gcc-c++, gettext, radiusclient-devel, python
BuildRequires: bind-utils, ntp, samba-client, openssh-clients
BuildRequires: openldap-devel, mysql-devel, postgresql-devel
BuildRequires: perl(Net::SNMP)


# Requires


%description

This package contains the basic plugins necessary for use with the
Nagios package. This package should install cleanly on almost any
RPM-based system.

But you may need additional packages. Depending on what plugins you
use, the following packages may be required:

    bind-utils, mysql, net-snmp-utils, ntp, openldap,
    openssh-clients, openssl, postgresql-libs
    qstat, radiusclient, samba-client, sendmail


Nagios is a program that will monitor hosts and services on your
network, and to email or page you when a problem arises or is
resolved. Nagios runs on a unix server as a background or daemon
process, intermittently running checks on various services that you
specify. The actual service checks are performed by separate "plugin"
programs which return the status of the checks to Nagios. This package
contains those plugins.


%prep
%setup -q


%build
./configure \
--prefix=%{_prefix} \
--exec-prefix=%{_exec_prefix} \
--libexecdir=%{_exec_prefix}/lib64/nagios/plugins \
--sysconfdir=%{_sysconfdir}/nagios \
--datadir=%{_datadir} \
--with-cgiurl=/nagios/cgi-bin \
--enable-extra-opts \
--with-snmpget-command=/usr/bin/snmpget \
--with-snmpgetnext-command=/usr/bin/snmpgetnext \
--with-qstat-command=/usr/bin/qstat \
--with-fping-command=/usr/sbin/fping 
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make AM_INSTALL_PROGRAM_FLAGS="" DESTDIR=${RPM_BUILD_ROOT} install
install -d ${RPM_BUILD_ROOT}/etc/nagios
install -m 664 command.cfg ${RPM_BUILD_ROOT}/etc/nagios
#%find_lang %{name}
%find_lang nagios-plugins


%clean
rm -rf $RPM_BUILD_ROOT


%files -f nagios-plugins.lang
%defattr(-,root,root)
%config(missingok,noreplace) /etc/nagios/command.cfg
%doc CODING COPYING FAQ INSTALL LEGAL README REQUIREMENTS SUPPORT THANKS
%doc ChangeLog command.cfg
%defattr(775,root,root)
%dir %{_exec_prefix}/lib64/nagios/plugins
%{_datadir}/locale/de/LC_MESSAGES/nagios-plugins.mo
%{_datadir}/locale/fr/LC_MESSAGES/nagios-plugins.mo
%{_exec_prefix}/lib64/nagios/plugins

%changelog
* Wed Oct 17 2012 Mark Clarkson <mark.clarkson@smorg.co.uk>
- Updated from upstream.
* Mon May 23 2005 Sean Finney <seanius@seanius.net> - cvs head
- just include the nagios plugins directory, which will automatically include
  all generated plugins (which keeps the build from failing on systems that
  don't have all build-dependencies for every plugin)
* Tue Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs
* Tue Mar 04 2004 Karl DeBisschop <karl[AT]debisschop.net> - 1.4.0alpha1
- extensive rewrite to facilitate processing into various distro-compatible specs

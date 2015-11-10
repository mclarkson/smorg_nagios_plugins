smorg_nagios_plugins
====================

Build files for nagios-plugins version 2.1.1.

Build:
```
# Install RPMs needed for build

sudo yum install @development yum-utils
sudo yum-builddep rpmbuild/SPECS/smorg-nagios-plugins.spec

# Build. Use sudo since root is needed for setuid bits on
# check_dhcp and check_icmp

sudo ./jenkins_build.sh
```


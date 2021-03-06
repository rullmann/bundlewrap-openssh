# openssh

`openssh` configures the openssh server daemon.
It will setup security measures, a banner and integrate with firewalld.

## Integrations

* Bundles:
  * [firewalld](https://github.com/rullmann/bundlewrap-firewalld)
    * Zone settings from firewalld bundle will be used
  * [users](https://github.com/rullmann/bundlewrap-users)
    * Ability to add ssh keys for users
  * [monit](https://github.com/rullmann/bundlewrap-monit)

## Metadata

OpenSSH requires an IP(v6) address and a `main_interface`. Currently no additional listen interfaces are supported.

    'metadata': {
        'interfaces': {
            'eth0': {
                'ip_address': '192.168.1.2',
                'ipv6_address': '2001:xxxx:xxxx::1', # optional
            },
        },
        'main_interface': 'eth0',
        'openssh': {
            'listen_ipv4': True, # Optional, True by default
            'listen_ipv6': False, # Optional, False by default
            'enable_systemd_service': True, # Optional, True by default. Might be used on laptops etc. where openssh should be configured, but not enabled
            'listen_all': False, # Optional, False by default. May break in combination with listen_ipv* options. Enable only if you know what you're doing!
        },
    }

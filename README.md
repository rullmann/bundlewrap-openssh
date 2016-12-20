# openssh

`openssh` configures the openssh server daemon.
It will setup security measures, a banner and integrate with firewalld.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 24   | `[x]` |
| Fedberry 24 | `[x]` |

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
            'listen_ipv6': True, # Optional, True by default
            'listen_ipv6': False, # Optional, False by default
        },
    }

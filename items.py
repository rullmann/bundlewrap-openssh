pkg_dnf = {
    'openssh-server': {},
}

svc_systemd = {
    'sshd': {},
}

files = {
    '/etc/ssh/sshd_config': {
        'source': 'sshd_config',
        'mode': '0600',
        'content_type': 'mako',
        'triggers': ['svc_systemd:sshd:restart'],
    },
    '/etc/ssh/sshd_banner': {
        'source': 'sshd_banner',
        'mode': '0600',
        'content_type': 'mako',
    },
    '/etc/ssh/ssh_config': {
        'source': 'ssh_config',
        'mode': '0600',
    },
}

actions = {}

if node.os == 'fedora' and node.os_version >= (27):
    files['/etc/sysconfig/sshd'] = {
        'source': 'sysconfig_sshd',
        'mode': '0640',
        'triggers': ['svc_systemd:sshd:restart'],
    }

if node.has_bundle('firewalld'):
    if node.metadata.get('firewalld', {}).get('default_zone'):
        default_zone = node.metadata.get('firewalld', {}).get('default_zone')
        actions['firewalld_add_ssh_zone_{}'.format(default_zone)] = {
            'command': 'firewall-cmd --permanent --zone={} --add-service=ssh'.format(default_zone),
            'unless': 'firewall-cmd --zone={} --list-services | grep ssh'.format(default_zone),
            'cascade_skip': False,
            'needs': ['pkg_dnf:firewalld'],
            'triggers': ['action:firewalld_reload'],
        }
    elif node.metadata.get('firewalld', {}).get('custom_zones', False):
        for interface in node.metadata['interfaces']:
            custom_zone = node.metadata.get('interfaces', {}).get(interface).get('firewalld_zone')
            actions['firewalld_add_ssh_zone_{}'.format(custom_zone)] = {
                'command': 'firewall-cmd --permanent --zone={} --add-service=ssh'.format(custom_zone),
                'unless': 'firewall-cmd --zone={} --list-services | grep ssh'.format(custom_zone),
                'cascade_skip': False,
                'needs': ['pkg_dnf:firewalld'],
                'triggers': ['action:firewalld_reload'],
            }
    else:
        actions['firewalld_add_ssh'] = {
            'command': 'firewall-cmd --permanent --add-service=ssh',
            'unless': 'firewall-cmd --list-services | grep ssh',
            'cascade_skip': False,
            'needs': ['pkg_dnf:firewalld'],
            'triggers': ['action:firewalld_reload'],
        }

if node.has_bundle('monit'):
    files['/etc/monit.d/openssh'] = {
        'source': 'monit',
        'mode': '0640',
        'content_type': 'mako',
        'triggers': ['svc_systemd:monit:restart'],
    }

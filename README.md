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

## Metadata

* none so far

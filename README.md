# Ansible Role: Stepmania

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-stepmania.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-stepmania)

An Ansible Role that installs [Stepmania](https://github.com/stepmania/stepmania) on Ubuntu 18.04.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
stepmania_install_path: /opt/stepmania
stepmania_version: master
```

# Dependencies

None.

# Example Playbook

```yaml
- name: Install Stepmania
  hosts: all
  roles:
    - hadrienpatte.stepmania
```

## License

MIT

## Author

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)

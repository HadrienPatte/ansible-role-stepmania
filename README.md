# Ansible Role: Stepmania

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

import os

import testinfra.utils.ansible_runner

import pytest

import yaml

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

with open('../../defaults/main.yml') as vars_yml:
    vars = yaml.load(vars_yml)

with open('playbook.yml') as playbook_yml:
    playbook = yaml.load(playbook_yml)

vars.update(playbook[0]['vars'])


@pytest.mark.parametrize('name', [
    ('build-essential'),
    ('cmake'),
    ('mesa-common-dev'),
    ('libglu1-mesa-dev'),
    ('libglew-dev'),
    ('libxtst-dev'),
    ('libxrandr-dev'),
    ('libpng-dev'),
    ('libjpeg-dev'),
    ('zlib1g-dev'),
    ('libbz2-dev'),
    ('libogg-dev'),
    ('libvorbis-dev'),
    ('libc6-dev'),
    ('yasm'),
    ('libasound2-dev'),
    ('libpulse-dev'),
    ('binutils-dev'),
    ('libgtk2.0-dev'),
    ('libmad0-dev'),
    ('libudev-dev'),
    ('libva-dev'),
    ('nasm'),
    ('git')
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


def test_stepmania_directory_ownership(host):
    directory = host.file(vars['stepmania_install_path'])
    assert directory.exists
    assert directory.is_directory
    assert directory.user == vars['ansible_env']['USER']
    assert directory.group == vars['ansible_env']['USER']


def test_stepmania_is_installed(host):
    assert host.exists('stepmania')


def test_stepmania_desktop_entry_exists(host):
    stepmania_desktop = host.file('/usr/share/applications/stepmania.desktop')
    assert stepmania_desktop.exists
    assert stepmania_desktop.is_file

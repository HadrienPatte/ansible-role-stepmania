import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


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


def test_stepmania_is_installed(host):
    assert host.exists('stepmania')


def test_stepmania_desktop_entry_exists(host):
    stepmania_desktop = host.file('/usr/share/applications/stepmania.desktop')
    assert stepmania_desktop.exists
    assert stepmania_desktop.is_file

# Missing tests on stepmania directory ownership

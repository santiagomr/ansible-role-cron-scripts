import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_scripts_files(host):
    f = host.file('/var/scripts/example.sh')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    f = host.file('/var/scripts/daemon.sh')

    assert f.exists
    assert f.user == 'daemon'
    assert f.group == 'daemon'


def test_crontab_files(host):
    f = host.file('/var/spool/cron/crontabs/root')
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'crontab'

    f = host.file('/var/spool/cron/crontabs/daemon')
    assert f.exists
    assert f.user == 'daemon'
    assert f.group == 'crontab'

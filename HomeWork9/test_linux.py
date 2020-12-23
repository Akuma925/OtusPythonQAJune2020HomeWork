import pytest
import os
import shutil
import subprocess
import time


@pytest.mark.parametrize("host", ["google.com",
                                  "otus.ru",
                                  "linux.org.ru", ])
def test_ping(host):
    assert os.system("ping -c 4 " + host) == 0


@pytest.mark.parametrize("ip", ["192.168.1.94",
                                "127.0.0.1",
                                " fe80::d19a:9232:f8a2:2758", ])
def test_ip(ip):
    assert os.system("ip a | grep -F " + ip) == 0


def test_run():
    infi = subprocess.Popen(["cat", "/dev/random"])
    assert not infi.poll()
    time.sleep(2)
    assert not infi.poll()
    infi.terminate()
    assert infi.wait(2)


@pytest.mark.parametrize("name", ["Temp-976444f7-4a9f-482e-802b-87a2aac6b4b5",
                                  "Temp-c207831f-06f0-40f7-812d-c8498e7183a2"
                                  ])
def test_filesystem(name):
    dirname="/tmp/" + name
    shutil.rmtree(dirname, ignore_errors=True)
    os.makedirs(dirname)
    os.chdir(dirname)
    assert os.getcwd() == dirname
    shutil.copy("/etc/passwd", dirname)
    assert os.listdir(dirname) == ["passwd"]
    os.chdir("/home")
    shutil.rmtree(dirname)

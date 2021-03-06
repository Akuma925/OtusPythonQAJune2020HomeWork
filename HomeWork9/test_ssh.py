from ssh import SSH
import requests
import pytest

url="http://localhost"
username="ubuntu"
host="localhost"


@pytest.mark.parametrize("service", ["apache2", "mariadb"])
def test_services(service):
    ssh = SSH(host, username)
    ssh.sudo(f"systemctl restart {service}")
    is_active = ssh.sudo(f"systemctl is-active {service}")
    assert is_active["out"].rstrip() == "active"
    assert requests.get(url).status_code == 200

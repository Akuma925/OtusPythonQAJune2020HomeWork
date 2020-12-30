import paramiko


class SSH:
    def __init__(self, host, username):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, port=22)
        self.ssh = ssh

    def sudo(self, command):
        stdin, stdout, stderr = self.ssh.exec_command("sudo " + command)
        return {
            "out": stdout.read().decode("utf-8"),
            "err": stderr.read().decode("utf-8"), }
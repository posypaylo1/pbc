import paramiko
from paramiko import client


class Ssh:
    client = None
    def __init__(self):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy)
        self.client.connect('192.168.33.10', username='vagrant', password='vagrant')

    # def start(self):
    #     try:
    #         self.client.connect('192.168.33.10', username='vagrant', password='vagrant', timeout=15)
    #         return self.client
    #     except Exception as e:
    #         print(e)
    #         self.client.close()
    #         return False

    def send_command(self, command):
        if self.client:
            result = []
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                for row in stdout:
                    result.append(str(row))
                return result
        else:
            print("Connection not opened.")


    def close(self):
        self.client.close()
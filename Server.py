#
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='34.212.34.156', username='ubuntu', key_filename=r"C:\Users\russi\Downloads\ssh-rsa.ppk")

stdin, stdout, stderr = ssh.exec_command('sudo apt update')

for line in stdout.read().splitlines():
    print(line)

ssh.close()



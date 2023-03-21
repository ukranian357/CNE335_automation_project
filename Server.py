class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        return

    # This is the template code for the CNE335 Final Project
    # Akex Nikolaev
    # CNE 335 Fall
    import os

    def print_program_info():
        # TODO - Change your name
        print("Server Automator v0.1 by Alex Nikolaev")

    # This is the entry point to our program
    if __name__ == '__main__':
        print_program_info()

        # TODO - Create a Server object

    class MyServer:
        def __init__(self, host):
            self.host = host

    $

    def myping(host):
        response = os.system("ping -n 1 " + host)

        if response == 0:
            return True
        else:
            return False

     print(myping("34.212.34.156"))


    # print(myping("34.212.34.156"))

    import paramiko

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='34.212.34.156', username='ubuntu', key_filename=r"C:\Users\russi\Downloads\ssh-rsa.ppk")

    stdin, stdout, stderr = ssh.exec_command('sudo apt update')

    for line in stdout.read().splitlines():
        print(line)

    ssh.close()



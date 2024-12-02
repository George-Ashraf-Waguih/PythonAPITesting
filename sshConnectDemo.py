import paramiko as paramiko
from utilities.configurations import *

user = getConfig()['Server']['username']
password = getConfig()['Server']['password']
host = getConfig()['Server']['host']
port = getConfig()['SQL']['port']
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Start connection
ssh.connect(host, port, username=user, password=password)

# Run commands
# stdin, stdout, stderr = ssh.exec_command('ls -a')   # list all files including hidden files
# print(stdout.readlines())  # stdout is storing the output from the command

stdin, stdout, stderr = ssh.exec_command('cat demofile')  # open this demo file
# print(stdout.readlines())
lines = stdout.readlines()
print(lines[0])


# Tp upload/download files to server
sftp = ssh.open_sftp()
destinationPath = "script.py"  # Path to where file will be created
localPath = "demofile"   # Path to source of file
sftp.put(localPath, destinationPath)



sftp.close()
ssh.close()

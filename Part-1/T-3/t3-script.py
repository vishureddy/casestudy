import paramiko

# Import the library
import argparse
# Create the parser
parser = argparse.ArgumentParser()


# Add an argument
parser.add_argument('--hostname', type=str, required=True)
parser.add_argument('--username', type=str, required=True)

#nargs='+' will allow the argument to take in any number of values. 
parser.add_argument('--commands', type=str, nargs='+')


# Parse the argument
args = parser.parse_args()

# initialize the SSH client
client = paramiko.SSHClient()
# add to known hosts
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pkey = paramiko.RSAKey.from_private_key_file("/Users/ganganakunta.reddy/.ssh/id_rsa")

try:
    client.connect(hostname=args.hostname, username=args.username, pkey=pkey)
except:
    print("[!] Cannot connect to the Remote SSH Server")
    exit()

# execute the commands
for command in args.commands:
    print("*"*50, command, "*"*50)
    stdin, stdout, stderr = client.exec_command(command)
    print(stdout.read().decode())
    err = stderr.read().decode()
    stdin.close()
    if err:
        print(err)
    

client.close()
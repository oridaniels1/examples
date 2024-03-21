import re
import sys

# Check if the file path argument is provided
if len(sys.argv) < 2:
    print("Please provide the path of the input file as an argument.")
    sys.exit(1)

# Get the file path from the command-line argument
file_path = sys.argv[1]

# Open the text file
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)

# Function to mask a string with asterisks
def mask_string(string):
    return re.sub(r'[0-9a-z]', '*', string)

# Create a list to store the host entries
hosts = []

# Process each line from the file
for line in lines:
    # Extract the hostname, username, and IP address using regular expressions
    match = re.search(r'(\S+)\s+(?:NO|Installed)\s+ssh (\S+)@(\d+\.\d+\.\d+\.\d+)', line)
    if match:
        hostname = match.group(1)
        username = match.group(2)
        ip_address = match.group(3)
        ansible_host = ip_address
        ansible_port = '39'
        ansible_user = username
        ansible_password = 'Orca123'
        ansible_sudo_pass = 'Orca123'

        host_entry = {
            'hostname': hostname,
            'ansible_host': ansible_host,
            'ansible_port': ansible_port,
            'ansible_user': ansible_user,
            'ansible_password': ansible_password,
            'ansible_sudo_pass': ansible_sudo_pass
        }

        hosts.append(host_entry)

# Generate the Ansible hosts file
output = ""
for host in hosts:
    output += f"{host['ansible_host']}\t{host['hostname']}\n"
    output += f"{host['hostname']} ansible_host={host['ansible_host']} ansible_port={host['ansible_port']} "
    output += f"ansible_user={host['ansible_user']} ansible_password={host['ansible_password']} "
    output += f"ansible_sudo_pass={host['ansible_sudo_pass']}\n"

# Print the Ansible hosts file
print(output)

# Additional print statement for the desired format
print(f"{hosts[0]['ansible_host']}\t{hosts[0]['hostname']}")

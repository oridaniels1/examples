import os
import glob
import re

def replace_credentials(playbook_pattern, new_username, new_password):
    playbook_files = glob.glob(playbook_pattern)

    for playbook_file in playbook_files:
        with open(playbook_file, 'r') as file:
            playbook_content = file.read()

        # Replace username
        playbook_content = re.sub(r'^( *)- name: Set username.*$', rf'\1- name: Set username to {new_username}', playbook_content, flags=re.MULTILINE)
        playbook_content = re.sub(r'^( *)username: .+$', rf'\1username: {new_username}', playbook_content, flags=re.MULTILINE)

        # Replace password
        playbook_content = re.sub(r'^( *)- name: Set password.*$', rf'\1- name: Set password to {new_password}', playbook_content, flags=re.MULTILINE)
        playbook_content = re.sub(r'^( *)password: .+$', rf'\1password: {new_password}', playbook_content, flags=re.MULTILINE)

        with open(playbook_file, 'w') as file:
            file.write(playbook_content)

if __name__ == '__main__':
    playbook_pattern = '/etc/ansible/playbooks/*.yml'
    new_username = 'techops@orca-ai.io'
    new_password = 'kianjnebnygzopob'

    replace_credentials(playbook_pattern, new_username, new_password)
    print('Credentials replaced successfully.')


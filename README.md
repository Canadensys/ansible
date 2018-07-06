# ansible
Ansible playbooks and roles used by canadensys to :
- add a bit more secure server
- install wordpress, media wiki

## dependencies:
use: ansible 2.2.0.0 or more
use: python 2.7.x or more

## How to use
### Install security playbook
$ ansible-playbook -i hosts -l vm_local_102 security_playbook.yml --user user_with_root_access --ask-pass --ask-sudo-pass

### Install security playbook
$ ansible-playbook -i hosts -l vm_local_102 wordpress_playbook.yml --user user_with_root_access  --private-key ~/.ssh/your_private_key.rsa --ask-sudo-pass

### Install Vascan and Tools playbook
Install community roles:
```
ansible-galaxy install -r roles/roles_requirements.yml
```

Run playbook (note that the database dump will be restored on all run)
```
$ ansible-playbook -i hosts -l vm_vascan_prod vascan_and_tools_playbook.yml --user user_with_root_access  --private-key ~/.ssh/your_private_key.rsa --become
```
*vm_vascan_prod shall be declared in your host file, the matching group_vars will be used for the nginx setup. 

Files not provided with the roles:
 - MySQL dumps (see `vascan_db.src`  and `vascan_editor_db.src`) 
 - Vascan Editor war file (see `vascan_editor_war`)

 Variables to overwrite:
 - `vascan_db.user` and `vascan_db.password`
 - `vascan_editor_db.user`and `vascan_editor_db.password` (shall match the value in the config of the provided Vascan Editor war file)
 - `google_analytics.site_verification` and `google_analytics.account`

## Usable CL:
to create a password:
$ mkpasswd --method=sha-512
to create ssh key:
$ ssh-keygen -f irbv_wordpress.rsa

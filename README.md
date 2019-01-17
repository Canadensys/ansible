# Canadensys Installation Scripts
This project contains [Ansible](http://www.ansible.com/) playbooks for setting up Canadensys components on local server or on cloud.

## Ansible

### Ansible version

The current supported version is: **2.7.1**

The playbooks and roles in this repository have been developed and tested against the above version.

NOTE: many linux packages have an older version of Ansible (1.7 or even 1.5). You will need to update your packages and upgrade ansible first.

For APT:

```
$ sudo apt-get install software-properties-common python-dev git python-pip
$ sudo pip install setuptools
$ sudo pip install -I ansible==[version]
# or 
$ sudo -H pip install ansible==[version]
```

where ```[version]``` is the supported version listed above.

If you see this error:
```
ERROR: apache2_module is not a legal parameter in an Ansible task or handler.
```
then you have an older version of Ansible.

### Ansible playbooks Family

There are two types of playbooks, one local (local_playbook_name) and one for the cloud (cloud_playbook_name).

### Choose your own inventories directory
In ansible playbook, change:

```
  vars_files:
    - './inventories/common.yml'
```
for
```
  vars_files:
    - '../canadensys-inventories/common.yml'
```
Where ../canadensys-inventories/ contains all your secret inventories.

### Examples

Install wordpress playbook: \
`[...]/canadensys-ansible$ ansible-playbook -i ./inventories/wordpress wordpress-db_local-nginx.yml --user user_with_root_access --ask-pass --ask-sudo-pass` \
or \
`[...]/canadensys-ansible$ ansible-playbook -i ./inventories/wordpress wordpress-db_local-nginx.yml --user user_with_root_access  --private-key ~/.ssh/your_private_key.rsa` \

### Install Vascan and Tools playbook
Install community roles:
`[...]/canadensys-ansible$ ansible-galaxy install -r ./roles/roles_requirements.yml`

Run playbook (note that the database dump will be restored on all run) \
`[...]/canadensys-ansible$ ansible-playbook -i ./inventories/vascan vascan-tools.yml --user user_with_root_access  --private-key ~/.ssh/your_private_key.rsa` \
[//]: # (*vm_vascan_prod* shall be declared in your host file, the matching group_vars will be used for the nginx setup.)

Files not provided with the roles:
 - MySQL dumps (see variables `vascan_db_src`  and `vascan_editor_db_src`) 
 - Vascan Editor war file (see variable `vascan_editor_war`)

 Variables to overwrite:
 - `vascan_db_user` and `vascan_db_password`
 - `vascan_editor_db_user`and `vascan_editor_db_password` (shall match the value in the config of the provided Vascan Editor war file)
 - `google_analytics_site_verification` and `google_analytics_account`

## Usable CL:
Create a password:
$ mkpasswd --method=sha-512
Create ssh key:
$ ssh-keygen -f wordpress.rsa

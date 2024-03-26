Role Name
=========

Role to update LDAP DN for imported AWX LDAP users.

Requirements
------------

Role Variables
--------------

**Ansible Automation Platform Database Name**

```
_ansible_automation_platform_awx_import_aap_database_name_
```

**Ansible Automation Platform Database Username**

```
_ansible_automation_platform_awx_import_aap_database_user_
```

**Ansible Automation Platform Database Password**

```
_ansible_automation_platform_awx_import_aap_database_password_
```

**Path where the exported object files are stored**

```
_awx_export_export_path:_
```


Dependencies
------------


**Collections:**

- community.postgresql

Example Playbook
----------------

```
- name: AWX LDAP DN Update
  hosts: aap_database
  gather_facts: false
  become: false
  roles:
    - ansible_automation_platform_awx_import_ldap_table
```



Author Information
------------------

Bernd Zehrfuchs <bzehrfuc@redhat.com>

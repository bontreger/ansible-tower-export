Role Name
=========

Role to import AWX object from files into Ansible Automation Platform.

Requirements
------------

Role Variables
--------------

**List of AWX Objects which should get imported**

```
ansible_automation_platform_awx_import_object_list:
  - organizations
  - credential_types
  - credentials
  - projects
  - job_templates
  - inventory
  - inventory_sources
  - workflow_job_templates
  - notification_templates
  - users
  - teams
```

**Ansible Automation Platform Controller Username (this user requires superuser privileges)**

```
controller_username
```

**Ansible Automation Platform Controller Password**

```
controller_password
```

**Validate SSL Certificates on the Ansible Automation Platform Controller**

```
controller_validate_certs: true
```

**Path where the exported object files are stored**

```
awx_export_export_path:
```

**Password which is used to decrypt the exported credentials.**

```
awx_export_vault_pass
```

**Import single objects for better error handling instead of importing all object of one kind at once.**

**This creates more detailed logs which contain the type, objectname and the error message of each object.**

```
ansible_automation_platform_awx_import_debug: false
```

**Ignore all errors which are returned by the API. **

**They will get collected and written to the logfile at the end of the import.**

```
ansible_automation_platform_awx_import_ignore_all_errors: false
```

**List of errors which will get collected and stored in the logfile but will not cause the playbook to fail.**

```
ansible_automation_platform_awx_import_ignoreable_errors:
```

**Example:**

```
ansible_automation_platform_awx_import_ignoreable_errors:
  - "Object import failed: Bad Request (400) received - {'playbook': ['Playbook not found for project.']}.\n"
```


Dependencies
------------

**Collections:**

- ansible.controller
- community.postgresql

Example Playbook
----------------

```
- name: AWX Object Collector
  hosts: aap_controller
  gather_facts: false
  become: false
  roles:
    - ansible_automation_platform_awx_import
```

Author Information
------------------

Bernd Zehrfuchs <bzehrfuc@redhat.com>
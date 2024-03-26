# ansible_automation_platform_installation

A Role to install Ansible Automation Platform 2.1.

# Requirements

Ansible Automation Platform Setup Bundle

# Role Variables


## Ansible Automation Platform Database Server Variables:

**Specify the Database Server Hostname:**

`ansible_automation_platform_installation_database_host:`

**Specify the Database Server Port (default: 5432)**

`ansible_automation_platform_installation_database_port:`

**Specify the Database Name:**

`ansible_automation_platform_installation_database_name:`

**Specify the Database Username:**

`ansible_automation_platform_installation_database_username:`

**Specify the Database Password:**

`ansible_automation_platform_installation_database_password:`

**Specify Database SSL Enabled:**

`ansible_automation_platform_installation_postgres_ssl_enabled:`

**Specify Database SSL Cert (only required if SSL is enabled):**

`ansible_automation_platform_installation_postgres_ssl_cert:`

**Specify Database SSL Key (only required if SSL is enabled):**

`ansible_automation_platform_installation_postgres_ssl_key:`

**Ansible Automation Platform Private AutomationHub Variables:**

**Specify Private AutomationHub Host:**

`ansible_automation_platform_installation_automationhub_host:`

**Specify Private AutomationHub Admin Password:**

This password is used for the admin user after the initial installation.
The variable can't be used to reset a forgotten password.

`ansible_automation_platform_installation_automationhub_admin_password:`

**Specify Private Automation Hub Username:**

This can be used to connect to the private AutomationHub if it already exists and the user is already created.
Use the value "admin" on new installations.

`ansible_automation_platform_installation_automationhub_username:`

**Specify Private Automation Hub Password:**

This can be used to connect to the private AutomationHub if it already exists and the user is already created.
Use the same password as for ansible_automation_platform_installation_automationhub_admin_password on new installations.

**Specify Private AutomationHub Database Details:**

The database name, username and password can only get changed on initial installations, do not change it on update/upgrade deployments.

```
ansible_automation_platform_installation_automationhub_database_name:
ansible_automation_platform_installation_automationhub_database_username:
ansible_automation_platform_installation_automationhub_database_password:
```


## Ansible Automation Platform Controller Settings:

**Specify Ansible Automation Platform Controller nodes:**

This variable contains a list of all controller nodes.

`ansible_automation_platform_installation_controller_hosts:`

**Speficy Automation Platform Controller SSL Settings:**

```
ansible_automation_platform_installation_controller_ssl_cert:
ansible_automation_platform_installation_controller_ssl_key: 
```
## Ansible Automation Platform Global Parameters:

Add Custom CA Certificate to the Deployment:

`ansible_automation_platform_installation_ssl_ca_cert:`


# Example Playbook


    - hosts: bastionhost
      gather_facts: false
      become: false
      roles:
         - ansible_automation_platform_installation


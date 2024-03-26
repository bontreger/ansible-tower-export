# Tower to AAP migration

## Use
Update vault.yml and inventory to match your environment details.

Run this command:
`ANSIBLE_VAULT_PASSWORD=<password to the vault.yml file in this repo> ansible-navigator run awx_secrets.yml --eei registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel9:latest -m stdout -i inventory`


## Disclaimer

Listen, this is a terrible idea and an ugly workaround to try to bring objects out of an Ansible Tower database into a configuration as code snippet so that they can be imported into an Ansible Automation Platform instance where the database can't be updated with a lift and replace (i.e. in an AAP managed service).

But it did work for me once, so there's that.

## Issue reporting
Feel free to, just don't expect a response.

## Pull requests
Sure! Why not?

## Support
None. Maybe a moral support giphy in chat but that's probably the limit.
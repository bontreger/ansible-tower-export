# Tower to AAP migration

## Use
Update vault.yml and inventory to match your environment details.

Run this command:
`ANSIBLE_VAULT_PASSWORD=<password to the vault.yml file in this repo> ansible-navigator run awx_secrets.yml --eei registry.redhat.io/ansible-automation-platform-24/ee-supported-rhel9:latest -m stdout -i inventory`

## Importing
Throw all those json files into tower-credential-export/vars/ and run the awx_import.yml playbook. This does require the infra.controller_configuration collection, so build an EE with it or install it and run it locally.


## Disclaimer

Listen, this is a terrible idea and an ugly workaround to try to bring objects out of an Ansible Tower database into a configuration as code snippet so that they can be imported into an Ansible Automation Platform instance where the database can't be updated with a lift and replace (i.e. in an AAP managed service).

But it did work for me once, so there's that.

## Things I've seen happen
We're doing funny things with delegation and remote execution. You might need to add additional environment variables to your psql commands. It's a mess. But it did work... just with some extra effort.


## Issue reporting
Feel free to, just don't expect a response.

## Pull requests
Sure! Why not?

## Support
None. Maybe a moral support giphy in chat but that's probably the limit.
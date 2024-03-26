#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# pylint: disable=wrong-import-order,wrong-import-position,unused-import

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '0.1',
                    'status': ['preview'],
                    'supported_by': 'core'}

DOCUMENTATION = '''
---
module: awxsecret
version_added: "2.9"
short_description: processes AWX secrets
description:
  - Processes and stores AWX secrets.
options:
  kid:
    description:
    - Private KeyID
    required: true
    type: int
    default:
  data:
    description: Credential Extra Data
    required: true
    default:
    type: dict
  credential:
    description: Credential Export Data
    required: true
    default:
    type: dict
'''

EXAMPLES = '''
# Process Credential Object
- name: Process Credential
  awxsecret:
    kid: 1
    data: "{{ extra_credential_info }}"
    credential: "{{ export_credential_data }}"
# Results:
# credentials: "{{ credential_data }}"

'''

import json   # noqa: F401
import re  # noqa: F401
import time # noqa: F401
import base64 # noqa: F401
import hashlib # noqa: F401A
import ast  # noqa: F401

from cryptography.fernet import Fernet, InvalidToken # noqa: F401
from cryptography.hazmat.backends import default_backend # noqa: F401

from ansible.module_utils.basic import AnsibleModule

class FNet256(Fernet):
    def __init__(self, key, backend=None):
        if backend is None:
            backend = default_backend()

        key = base64.urlsafe_b64decode(key)
        if len(key) != 64:
            raise ValueError(
                "Fernet key must be 64 url-safe base64-encoded bytes."
            )

        self._signing_key = key[:32]
        self._encryption_key = key[32:]
        self._backend = backend


class AWXsecretException(Exception):
    ''' Exception class for AWXsecret '''
    pass


# pylint: disable=too-many-public-methods,too-many-instance-attributes
class AWXsecret(object):

    # pylint: disable=too-many-arguments
    def __init__(self,
                 filename=None,
                 content=None,
                 content_type='yaml',
                 separator='.',
                 backup_ext=".{0}".format(time.strftime("%Y%m%dT%H%M%S")),
                 backup=False):
        self.content = content
        self._separator = separator
        self.filename = filename
        self.__yaml_dict = content
        self.content_type = content_type
        self.backup = backup
        self.backup_ext = backup_ext
        self.load(content_type=self.content_type)
        if self.__yaml_dict is None:
            self.__yaml_dict = {}

    @staticmethod
    def run_ansible(params):
        kid = params['kid']
        data=params['data']
        testres = list()
        data = re.sub('\\\\','', data)
        data = data[1:-1]

        credential_object = params['credential'][1:-1]
        credential_object = ast.literal_eval(credential_object)

        if "encrypted" in data:
            data = json.loads(str(data))
            secret = params['secret']
            secret = secret.encode('utf-8')
            for x in data:
                if not(isinstance(data[x], (bool))):
                    if "encrypted" in data[x]:
                        index_name = x
                        key = get_encryption_key(index_name, secret, kid)
                        credential_object['inputs'][index_name] = (decrypt_value(key, data[index_name]))

        return credential_object


def get_encryption_key(field_name, secret, kid=None):
    hlib = hashlib.sha512()
    hlib.update(secret)
    if kid is not None:
        hlib.update(str(kid).encode('utf-8'))
    hlib.update(field_name.encode('utf-8'))
    return base64.urlsafe_b64encode(hlib.digest())

def decrypt_value(encryption_key, value):
    raw_data = value[len('$encrypted$'):]
    utf8 = raw_data.startswith('UTF8$')
    if utf8:
        raw_data = raw_data[len('UTF8$'):]
    algo, b64data = raw_data.split('$', 1)
    if algo != 'AESCBC':
        raise ValueError('unsupported algorithm: %s' % algo)
    encrypted = base64.b64decode(b64data)
    f = FNet256(encryption_key)
    value = f.decrypt(encrypted)
    # If the encrypted string contained a UTF8 marker, decode the data
    if utf8:
        value = value.decode('utf-8')
    return value


def decrypt_key(data):

    return {'changed': True, 'result': data }

def main():
    ''' ansible awx module for decrypting secrets '''

    module = AnsibleModule(
        argument_spec=dict(
        kid=dict(default=None, type='str', required=True),
        data=dict(default=None, type='str', required=True),
        credential=dict(default=None, type='str', required=True),
        secret=dict(default=None, type='str', required=True),
        ),
        required_together=[["kid", "data"]],
    )

    if module.params['kid'] is not None:
        pk_error = False
        data_error = False

        if module.params['data'] in [None, []]:
            data_error = True

        if pk_error and data_error:
            return module.fail_json(failed=True, msg='Empty value for parameter key not allowed.')

    rval = decrypt_key(AWXsecret.run_ansible(module.params))
    if 'failed' in rval and rval['failed']:
        return module.fail_json(**rval)

    return module.exit_json(**rval)


if __name__ == '__main__':
    main()

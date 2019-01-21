#!/usr/bin/python

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'version': '0.1'}

DOCUMENTATION = '''
---
module: azion_cdn
short_description: Manage Azion Content Delivery Distribution
description:
    - Manage Azion Content Delivery Distribution
requirements: ['azion-sdk']
author: "Raphael Pereira Ribeiro (@raphapr)"
options:
  name:
    description:
      - The name of the content delivery configuration
    required: true
  state:
    description:
      - Attribute that specifies if the configuration has to be created, deleted or disabled
    required: false
    default: present
    choices: ['present', 'absent', 'disable']
  origin_address:
    description:
      - Origin address of configuration. It can be ip address or hostname (FQDN)
    required: true
  origin_host_header:
    description:
      - Host header that will be sent for origin
    required: true
  cname:
    description:
      - The domain list of site
    required: no
  cname_access_only:
    description:
      - Defines if content delivery will only use cname domains or not
    required: no
    default: no
    choices: ['yes', 'no']
  delivery_protocol:
    description:
      - Defines content delivery protocol
    required: no
    default: http
    choices: ['http', 'https']
  digital_certificate:
    description:
      - SSL certificte ID
    required: no
  origin_protocol_policy:
    description:
      - Defines to force protocol to origin
    choices: ['http', 'https', 'preserve']
    default: preserve
    required: no
  browser_cache_settings:
    description:
      - Defines browser user cache settings
    required: no
    default: honor
    choices: ['honor', 'override']
  browser_cache_settings_maximum_ttl:
    description:
      - Defines TTL (time-to-live) in seconds for objects into browser cache
    required: no
  cdn_cache_settings:
    description:
      - Defines CDN cache settings.
    required: no
    default: honor
    choices: ['honor', 'override']
  cdn_cache_settings_maximum_ttl:
    description:
      - Defines TTL (time-to-live) in seconds for objects into CDN cache. Default is `null`
    required: no
'''

EXAMPLES = '''
---
- name: Create Azion content delivery configuration
  azion_cdn:
    name: mysite.com
    state: present
    origin_address: 291.190.96.92
    origin_host_header: mysite.com
    cname:
        - mysite.com
        - website.com
    cname_access_only: yes
    delivery_protocol: https
    digital_certificate: 81918
    origin_protocol_policy: preserve
    browser_cache_settings: honor
    cdn_cache_settings: honor
'''

RETURN = '''
'''

import azion

from ansible.module_utils.basic import *


# class AzionContentDelivery:

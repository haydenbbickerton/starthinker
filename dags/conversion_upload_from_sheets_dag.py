###########################################################################
# 
#  Copyright 2019 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

'''
--------------------------------------------------------------

Before running this Airflow module...

  Install StarThinker in cloud composer from open source: 

    pip install git+https://github.com/google/starthinker

  Or push local code to the cloud composer plugins directory:

    source install/deploy.sh
    4) Composer Menu	   
    l) Install All

--------------------------------------------------------------

Conversion Upload Sheets

Move form Sheets to CM.

Specify a CM Account ID, Floodligh Activity ID and Conversion Type.
Include Sheets url, tab, and range, omit headers in range.
Columns: Ordinal, timestampMicros, encryptedUserId | encryptedUserIdCandidates | gclid | mobileDeviceId
Include encryption information if using encryptedUserId or encryptedUserIdCandidates.

'''

from starthinker_airflow.factory import DAG_Factory
 
# Add the following credentials to your Airflow configuration.
USER_CONN_ID = "starthinker_user" # The connection to use for user authentication.
GCP_CONN_ID = "starthinker_service" # The connection to use for service authentication.

INPUTS = {
  'dcm_account': '',
  'auth_read': 'user',  # Credentials used for reading data.
  'floodlight_activity_id': '',
  'floodlight_conversion_type': 'encryptedUserId',
  'encryption_entity_id': '',
  'encryption_entity_type': 'DCM_ACCOUNT',
  'encryption_entity_source': 'DATA_TRANSFER',
  'sheet_url': '',
  'sheet_tab': '',
  'sheet_range': '',
}

TASKS = [
  {
    'conversion_upload': {
      'auth': {
        'field': {
          'name': 'auth_read',
          'kind': 'authentication',
          'order': 1,
          'default': 'user',
          'description': 'Credentials used for reading data.'
        }
      },
      'account_id': {
        'field': {
          'name': 'dcm_account',
          'kind': 'string',
          'order': 0,
          'default': ''
        }
      },
      'activity_id': {
        'field': {
          'name': 'floodlight_activity_id',
          'kind': 'integer',
          'order': 1,
          'default': ''
        }
      },
      'conversion_type': {
        'field': {
          'name': 'floodlight_conversion_type',
          'kind': 'choice',
          'order': 2,
          'choices': [
            'encryptedUserId',
            'encryptedUserIdCandidates',
            'gclid',
            'mobileDeviceId'
          ],
          'default': 'encryptedUserId'
        }
      },
      'encryptionInfo': {
        'encryptionEntityId': {
          'field': {
            'name': 'encryption_entity_id',
            'kind': 'integer',
            'order': 3,
            'default': ''
          }
        },
        'encryptionEntityType': {
          'field': {
            'name': 'encryption_entity_type',
            'kind': 'choice',
            'order': 4,
            'choices': [
              'ADWORDS_CUSTOMER',
              'DBM_ADVERTISER',
              'DBM_PARTNER',
              'DCM_ACCOUNT',
              'DCM_ADVERTISER',
              'ENCRYPTION_ENTITY_TYPE_UNKNOWN'
            ],
            'default': 'DCM_ACCOUNT'
          }
        },
        'encryptionSource': {
          'field': {
            'name': 'encryption_entity_source',
            'kind': 'choice',
            'order': 5,
            'choices': [
              'AD_SERVING',
              'DATA_TRANSFER',
              'ENCRYPTION_SCOPE_UNKNOWN'
            ],
            'default': 'DATA_TRANSFER'
          }
        }
      },
      'sheets': {
        'url': {
          'field': {
            'name': 'sheet_url',
            'kind': 'string',
            'order': 9,
            'default': ''
          }
        },
        'tab': {
          'field': {
            'name': 'sheet_tab',
            'kind': 'string',
            'order': 10,
            'default': ''
          }
        },
        'range': {
          'field': {
            'name': 'sheet_range',
            'kind': 'string',
            'order': 11,
            'default': ''
          }
        }
      }
    }
  }
]

DAG_FACTORY = DAG_Factory('conversion_upload_from_sheets', { 'tasks':TASKS }, INPUTS)
DAG_FACTORY.apply_credentails(USER_CONN_ID, GCP_CONN_ID)
DAG = DAG_FACTORY.execute()

if __name__ == "__main__":
  DAG_FACTORY.print_commandline()

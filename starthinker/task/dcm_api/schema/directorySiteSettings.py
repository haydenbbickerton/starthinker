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

directorySiteSettings_Schema = [
  {
    "name": "activeViewOptOut",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  [
    {
      "description": "",
      "name": "dfpNetworkCode",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "description": "",
      "name": "dfpNetworkName",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "programmaticPlacementAccepted",
      "type": "BOOLEAN",
      "mode": "NULLABLE"
    },
    {
      "name": "pubPaidPlacementAccepted",
      "type": "BOOLEAN",
      "mode": "NULLABLE"
    },
    {
      "name": "publisherPortalOnly",
      "type": "BOOLEAN",
      "mode": "NULLABLE"
    }
  ],
  {
    "name": "instreamVideoPlacementAccepted",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "interstitialPlacementAccepted",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  }
]

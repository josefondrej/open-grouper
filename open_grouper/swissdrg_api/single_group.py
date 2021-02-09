import json
from typing import Dict, Union

import requests

from open_grouper.models.patient_case import PatientCase


def single_group(patient_case: PatientCase, version: str, locale: str) -> Union[Dict, int]:
    request = {
        "single_group": {
            "version": version,
            "locale": locale,
            "patient_case": patient_case.to_dict()
        }
    }

    endpoint = "https://grouper.swissdrg.org/api/group"

    headers = {
        'Content-Type': 'application/json',
    }

    try:
        grouper_result = requests.post(endpoint, headers=headers, data=json.dumps(request))
        if grouper_result.status_code == 200:
            return json.loads(grouper_result.content)
        else:
            return json.status_code

    except Exception as exception:
        print(f"[ERROR] Getting response from {endpoint}:\n "
              f"{exception}")

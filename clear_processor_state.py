import requests
import json

from get_processor import get_processor


def clear_processor_state(processor_id: str, token, url_nifi_api):
    
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(token),
    }
    response = requests.post(
        url_nifi_api + f"processors/{processor_id}/state/clear-requests",
        headers=header,
        verify=False
    )
    
    return response
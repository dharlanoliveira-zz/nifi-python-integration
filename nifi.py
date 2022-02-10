from get_token import get_token
from update_processor_status import update_processor_status
from clear_processor_state import clear_processor_state
from get_processor_state import get_processor_state

def start():
    url_nifi_api = "https://nifi.cpic.tcu.gov.br/nifi-api/"
    processor_id = (
        "10e11831-1298-1428-9aa5-e21c053fc61a"
    )
    access_payload = {
        "username": "",
        "password": "",
    }
    token = get_token(url_nifi_api, access_payload)
    update_processor_status(processor_id, "STOPPED", token, url_nifi_api)
    clear_processor_state(processor_id,token, url_nifi_api)
    update_processor_status(processor_id, "RUNNING", token, url_nifi_api)   
    
if __name__ == "__main__":
    start()
import requests
import config

def create_journal(webhook_data):
    event = webhook_data.get("event")
    device_data = webhook_data.get("data", {})
    device_id = device_data.get("id")
    device_name = device_data.get("name", "Unknown Device")

    if not device_id:
        return False, "Error: device_id is missing!"

    headers = {
        "Authorization": f"Token {config.TOKEN_NETBOX}",
        "Content-Type": "application/json"
    }
    body = {
        "assigned_object_type": "dcim.device",
        "assigned_object_id": device_id,
        "kind": "info",
        "comments": f"{event}-{device_name}"
    }

    response = requests.post(f"{config.URL_NETBOX}/api/extras/journal-entries/", json=body, headers=headers,verify=False)

    if response.status_code == 201:
        return True, "Journal entry created successfully!"
    else:
        return False, f"Error {response.status_code}: {response.text}"

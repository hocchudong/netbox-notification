import config
import asyncio
from telegrams import send_telegram_alert
from journal import create_journal
from message.device import updated_event,created_event,deleted_event
from message.vm import updated_event_vm,created_event_vm,deleted_event_vm
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/webhooks', methods=['POST'])
def webhook():
    # Get data
    data = request.get_json()
    event = data.get("event", {})
    object_type = data.get("model", {})
    if object_type == "devcice":
        # Process data
        messenger = f"*Warning!!!* \n"
        if event == "updated":
            info = updated_event(data)
            messenger+=info
            create_journal(data)
        elif event == "created":
            info = created_event(data)
            messenger+=info
            create_journal(data)
        elif event == "deleted":
            info = deleted_event(data)
            messenger+=info
        else:
            messenger+="No Info! Error while get data from NetBox!"
    elif object_type == "virtualmachine":
        messenger = f"*Warning!!!* \n"
        if event == "created":
            info = created_event_vm(data)
            messenger+=info
            create_journal(data)
            created_event_vm
        elif event == "updated":
            info = updated_event_vm(data)
            messenger+=info
            create_journal(data)
        elif event == "deleted":
            info = deleted_event_vm(data)
            messenger+=info
        else:
            messenger+="No Info! Error while get data from NetBox!"
    # Send messenger
    asyncio.run(send_telegram_alert(messenger))
    return jsonify({"status": "success"}), 200
# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.WEBHOOKS_PORTS, debug=True)

import logging
import pynetbox
import urllib3

TELEGRAM_BOT_TOKEN = "8132391475:AAHpdLS6HQ7m2LJ5t8_NYptdhiapQXHmiqY"
TELEGRAM_CHAT_ID = "6012746677"  
WEBHOOKS_PORTS = "5000"
URL_NETBOX = "https://www.netboxlab.local"
TOKEN_NETBOX = "aa8f29998abd6a63f476a2328ce2a629a506b579"

# Logging bassic config
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Netbox config
nb = pynetbox.api(URL_NETBOX,token=TOKEN_NETBOX)
nb.http_session.verify = False   
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
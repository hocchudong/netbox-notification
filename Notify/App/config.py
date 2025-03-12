import logging
import pynetbox
import urllib3

TELEGRAM_BOT_TOKEN = "Enter your Bot Token here!"
TELEGRAM_CHAT_ID = "Enter your Chat ID here!"  
WEBHOOKS_PORTS = "Enter Port run app here!"
URL_NETBOX = "Enter your NetBox URL here!"
TOKEN_NETBOX = "Enter your NetBox Token here!"

# Logging bassic config
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Netbox config(No SSL Check!)
nb = pynetbox.api(URL_NETBOX,token=TOKEN_NETBOX)
nb.http_session.verify = False   
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
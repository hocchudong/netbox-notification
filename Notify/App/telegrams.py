import config
from telegram import Bot
import logging
async def send_telegram_alert(message):
    bot = Bot(token=config.TELEGRAM_BOT_TOKEN)
    try:
        message = message.replace("_", "-")
        await bot.send_message(chat_id=config.TELEGRAM_CHAT_ID, text=message, parse_mode="Markdown")
        logging.info("Send successed!")
    except Exception as e:
        logging.error(f"Error while trying to send messenger: {e}")
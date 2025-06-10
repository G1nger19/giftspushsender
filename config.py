import os
import logging
from dotenv import load_dotenv
import constants

load_dotenv()

SESSION_NAME = os.getenv("SESSION_NAME")

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

BOT_TOKENS = os.getenv("BOT_TOKENS").split(',')

CHECK_INTERVAL = float(os.getenv("CHECK_INTERVAL"))
DATA_FILEPATH = constants.WORK_DIRPATH / "star_gifts.json"
DATA_SAVER_DELAY = float(os.getenv("DATA_SAVER_DELAY"))
NOTIFY_CHAT_ID = int(os.getenv("NOTIFY_CHAT_ID"))
NOTIFY_AFTER_STICKER_DELAY = float(os.getenv("NOTIFY_AFTER_STICKER_DELAY"))
NOTIFY_AFTER_TEXT_DELAY = float(os.getenv("NOTIFY_AFTER_TEXT_DELAY"))
TIMEZONE = os.getenv("TIMEZONE")
CONSOLE_LOG_LEVEL = getattr(logging, os.getenv("CONSOLE_LOG_LEVEL", "DEBUG"))
FILE_LOG_LEVEL = getattr(logging, os.getenv("FILE_LOG_LEVEL", "INFO"))
HTTP_REQUEST_TIMEOUT = int(os.getenv("HTTP_REQUEST_TIMEOUT"))

NOTIFY_TEXT = """\
{title}

№ {number} (<code>{id}</code>)
{total_amount}{available_amount}
💎 Price: {price} ⭐️
♻️ Convert price: {convert_price} ⭐️
"""

NOTIFY_TEXT_TITLES = {
    True: "🔥 A new limited gift has appeared",
    False: "❄️ A new gift has appeared"
}

NOTIFY_TEXT_TOTAL_AMOUNT = "\n🎯 Total amount: {total_amount}"
NOTIFY_TEXT_AVAILABLE_AMOUNT = "\n❓ Available amount: {available_amount} ({same_str}{available_percentage}%, updated at {updated_datetime} UTC)\n"

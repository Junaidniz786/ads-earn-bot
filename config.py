import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "Y8398491491:AAFKnww5QjxKCgJ3DissBWT5IzHNdvpqYtM")
# ADMIN_IDS as comma separated "12345,67890"
ADMIN_IDS = [int(x) for x in os.environ.get("ADMIN_IDS","").split(",") if x.strip().isdigit()]
CHANNEL_OR_GROUP = os.environ.get(CHANNEL_OR_GROUP = os.environ.get("CHANNEL_OR_GROUP", "@Junaidniz786")

DB_PATH = os.environ.get("DB_PATH","ads_earn.db")
DATABASE_URL = os.environ.get("DATABASE_URL")  # Railway Postgres will set this if added

# Business settings
REWARD_PER_VIEW = float(os.environ.get("REWARD_PER_VIEW", "1"))
COIN_NAME = os.environ.get("COIN_NAME", "Coin")
MIN_WITHDRAW_USDT = float(os.environ.get("MIN_WITHDRAW_USDT", "5.0"))
WITHDRAW_CURRENCY = os.environ.get("WITHDRAW_CURRENCY", "USDT")

# Admin panel key
ADMIN_KEY = os.environ.get("ADMIN_KEY", "set-your-secret-key")

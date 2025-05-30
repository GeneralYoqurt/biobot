import os
from utils.load_dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
# ______________________________________________________________________________________________________________________
DB_DRIVER = os.getenv('DB_DRIVER')
DB_SERVER = os.getenv('DB_SERVER')
DB_DATABASE = os.getenv('DB_DATABASE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
# ______________________________________________________________________________________________________________________
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
YOUTUBE_NOTIFY_CHANNEL_ID = os.getenv("YOUTUBE_NOTIFY_CHANNEL_ID")
YOUTUBE_POLL_INTERVAL = int(os.getenv("YOUTUBE_POLL_INTERVAL"))
LAST_VIDEO_FILE = os.path.join("data", "last_video.txt")
ROLE_ID_PING_NEW_VIDEO = os.getenv("ROLE_ID_PING_NEW_VIDEO")
# ______________________________________________________________________________________________________________________
DEFAULT_ENABLED_GUILD_ID = int(os.getenv("DEFAULT_ENABLED_GUILD_ID"))
# ______________________________________________________________________________________________________________________
CHANNEL_INTRODUCE_ID = int(os.getenv("CHANNEL_INTRODUCE_ID"))
# ______________________________________________________________________________________________________________________
LOGGING_VERIFICATION_CHANNEL_ID = int(os.getenv("LOGGING_VERIFICATION_CHANNEL_ID"))
# ______________________________________________________________________________________________________________________
ROLE_VERIFIED_USER = int(os.getenv("ROLE_VERIFIED_USER"))
# ____________________________________________________________________________________________________________________
MODERATOR_ROLE_ID = int(os.getenv("MODERATOR_ROLE_ID"))
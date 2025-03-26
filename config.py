import os
from utils.load_dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
# ______________________________________________________________________________________________________________________
DB_DRIVER = os.getenv('DRIVER')
DB_SERVER = os.getenv('SERVER')
DB_DATABASE = os.getenv('DATABASE')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_PORT = os.getenv('PORT')
# ______________________________________________________________________________________________________________________
YOUTUBE_CHANNEL_ID = os.getenv("YOUTUBE_CHANNEL_ID")
YOUTUBE_NOTIFY_CHANNEL_ID = os.getenv("YOUTUBE_NOTIFY_CHANNEL_ID")
YOUTUBE_POLL_INTERVAL = int(os.getenv("YOUTUBE_POLL_INTERVAL", "30"))
LAST_VIDEO_FILE = os.path.join("data", "last_video.txt")
# ______________________________________________________________________________________________________________________
ROLE_ID_PING_NEW_VIDEO = os.getenv("ROLE_ID_PING_NEW_VIDEO")
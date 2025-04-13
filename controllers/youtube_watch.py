import os
import asyncio
import aiohttp
import xml.etree.ElementTree as ET
from config import *

async def fetch_latest_video_id():
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={YOUTUBE_CHANNEL_ID}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.text()
            root = ET.fromstring(content)
            namespaces = {'atom': 'http://www.w3.org/2005/Atom', 
                          'yt': 'http://www.youtube.com/xml/schemas/2015'}
            entry = root.find('atom:entry', namespaces)
            if entry is not None:
                video_id_tag = entry.find('yt:videoId', namespaces)
                if video_id_tag is not None:
                    return video_id_tag.text
    return None

def read_last_video():
    try:
        with open(LAST_VIDEO_FILE, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def write_last_video(video_id):
    os.makedirs(os.path.dirname(LAST_VIDEO_FILE), exist_ok=True)
    with open(LAST_VIDEO_FILE, 'w', encoding='utf-8') as f:
        f.write(video_id)

async def youtube_listener(bot):
    # Stan inicjalny tylko z pliku
    last_video = read_last_video()
    while True:
        try:
            video_id = await fetch_latest_video_id()
            if video_id and video_id != last_video:
                # Dodatkowy check – np. logika opóźnienia lub ignorowanie krótkotrwałych zmian
                last_video = video_id
                write_last_video(last_video)
                message = f"<@&{ROLE_ID_PING_NEW_VIDEO}> **na kanale Ani!\nhttps://www.youtube.com/watch?v={video_id}**"
                if YOUTUBE_NOTIFY_CHANNEL_ID:
                    await bot.rest.create_message(int(YOUTUBE_NOTIFY_CHANNEL_ID), message, role_mentions=True)
                    print("Wysłano powiadomienie o nowym filmie.")
                else:
                    print("Brak ustawionego ID kanału powiadomień (YOUTUBE_NOTIFY_CHANNEL_ID).")
        except Exception as e:
            print("Błąd w youtube_listener:", e)
        await asyncio.sleep(YOUTUBE_POLL_INTERVAL)
import os
import asyncio
import aiohttp
import xml.etree.ElementTree as ET
import json
from config import *

async def fetch_latest_video_id():
    url = f"https://www.youtube.com/feeds/videos.xml?channel_id={YOUTUBE_CHANNEL_ID}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.text()
            root = ET.fromstring(content)
            namespaces = {'atom': 'http://www.w3.org/2005/Atom', 
                          'yt': 'http://www.youtube.com/xml/schemas/2015'}
            entries = root.findall('atom:entry', namespaces)
            videos = []
            for entry in entries[:5]:  # Pobierz 5 najnowszych filmów
                video_id = entry.find('yt:videoId', namespaces)
                if video_id is not None:
                    published = entry.find('atom:published', namespaces)
                    if published is not None:
                        videos.append({
                            'id': video_id.text,
                            'published': published.text
                        })
            return sorted(videos, key=lambda x: x['published'], reverse=True) if videos else []
    return []

def read_last_videos():
    try:
        with open(LAST_VIDEO_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'videos': [], 'last_notified': None}

def write_last_videos(videos_data):
    os.makedirs(os.path.dirname(LAST_VIDEO_FILE), exist_ok=True)
    with open(LAST_VIDEO_FILE, 'w', encoding='utf-8') as f:
        json.dump(videos_data, f)

async def youtube_listener(variables):
    bot = variables['bot']
    if not bot:
        print("Nie można znaleźć zmiennej bot zmiennych przekazywanych do async tasks.")
        return

    # Stan inicjalny z pliku
    stored_data = read_last_videos()
    known_video_ids = set(video['id'] for video in stored_data['videos'])
    last_notified = stored_data['last_notified']

    while True:
        try:
            latest_videos = await fetch_latest_video_id()
            if latest_videos:
                newest_video = latest_videos[0]  # Najnowszy film
                
                # Sprawdź czy to naprawdę nowy film
                if (newest_video['id'] not in known_video_ids and 
                    newest_video['id'] != last_notified):
                    
                    # Aktualizuj dane
                    last_notified = newest_video['id']
                    known_video_ids = set(video['id'] for video in latest_videos)
                    stored_data = {
                        'videos': latest_videos,
                        'last_notified': last_notified
                    }
                    write_last_videos(stored_data)

                    # Wyślij powiadomienie
                    message = f"<@&{ROLE_ID_PING_NEW_VIDEO}> **Nowy film na kanale Ani!\nhttps://www.youtube.com/watch?v={newest_video['id']}**"
                    if YOUTUBE_NOTIFY_CHANNEL_ID:
                        await bot.rest.create_message(int(YOUTUBE_NOTIFY_CHANNEL_ID), message, role_mentions=True)
                        print(f"Wysłano powiadomienie o nowym filmie: {newest_video['id']}")
                    else:
                        print("Brak ustawionego ID kanału powiadomień (YOUTUBE_NOTIFY_CHANNEL_ID).")
                
        except Exception as e:
            print(f"Błąd w youtube_listener: {e}")
        
        await asyncio.sleep(YOUTUBE_POLL_INTERVAL)
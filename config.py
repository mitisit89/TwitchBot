import os

import dotenv

dotenv.load_dotenv(".env")
TOKEN = os.getenv("TOKEN")
INIT_CHANNELS=['vs_code','panmitisit']

def playlist() -> None:
    if not os.path.exists("playlist.m3u"):
        os.system("touch playlist.m3u")

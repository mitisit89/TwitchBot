# subprocess.run(["mpv", 'playlist.m3u','--no-terminal','2&>1 1>/dev/null'],capture_output=False)
from bot import bot

if __name__ == "__main__":
    bot.run()

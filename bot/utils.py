import asyncio


def add_to_playlist(song: str):
    with open("playlist.m3u", "a") as playlist:
        playlist.write(song + "\n")


async def run_player():
    await asyncio.create_subprocess_exec(
        "mpv", "playlist.m3u", "--no-terminal", "--keep-open=yes",'--input-ipc-server=/tmp/mpvsocket' "2&>1 1>/dev/null"
    )

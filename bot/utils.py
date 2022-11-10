import asyncio
import json

async def add_to_playlist(song: str):
    cmd=json.dumps({"command": ["loadfile",song,"append-play"]})

    await asyncio.create_subprocess_shell(f"echo '{cmd}' | socat - /tmp/mpvsocket")


async def run_player():
    await asyncio.create_subprocess_exec(
        "mpv",
        "--player-operation-mode=pseudo-gui",
        "--no-terminal",
        "--keep-open=yes",
        "--input-ipc-server=/tmp/mpvsocket",
    )

import asyncio
import json

from config import LOGO


async def get_os_logo() -> str | None:
    lsb_release = await asyncio.subprocess.create_subprocess_shell(
        "lsb_release -sd", stdout=asyncio.subprocess.PIPE
    )
    output, err = await lsb_release.communicate()
    logo = output.decode().rstrip().replace('\"', '')
    return LOGO.get(logo)


async def add_to_playlist(song: str):
    cmd = json.dumps({"command": ["loadfile", song, "append-play"]})

    await asyncio.create_subprocess_shell(f"echo '{cmd}' | socat - /tmp/mpvsocket")


async def run_player():
    await asyncio.create_subprocess_exec(
        "mpv",
        "--player-operation-mode=pseudo-gui",
        "--no-terminal",
        "--keep-open=yes",
        "--input-ipc-server=/tmp/mpvsocket",
    )

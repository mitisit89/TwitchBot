from twitchio import Message
from twitchio.ext import commands

from config import INIT_CHANNELS, TOKEN, playlist

from .utils import add_to_playlist, run_player


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=TOKEN,
            prefix="!",
            initial_channels=INIT_CHANNELS,
        )

    async def event_ready(self) -> None:
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")
        playlist()
        await run_player()

    async def event_message(self, message: Message):
        if message.echo:
            return
        message.content = f"{message.content}"
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command(name="sr")
    async def song_request(self, ctx: commands.Context):
        # Command for song request
        print(ctx.message.content)
        add_to_playlist(ctx.message.content[4:])


bot = Bot()

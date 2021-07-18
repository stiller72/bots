import discord
from discord.ext import commands
from core import backend
import os
from exceptions import BackendError

prefix = os.environ.get("PREFIX")
token = os.environ.get("TOKEN")
bot_channel = os.environ.get("CHANNEL")

bot = commands.Bot(command_prefix=prefix)


async def get_emoj(emoji: str):
    return discord.utils.get(bot.emojis, name=emoji)


@bot.command(name='расскажи')
async def balaboba(ctx, start_string: str = '', *args):
    if not start_string:
        await ctx.send('Ты ебанутый? Чиво рассказать?')
        return

    answer = await backend.balaboba(ctx, start_string, *args)

    await ctx.send(answer)


@bot.listen()
async def on_message(message):
    if message.content.startswith('спасибо'):
        aga = get_emoj("aga")
        await message.channel.send(f'Всегда готов сосать хуи {aga}')


@bot.event
async def on_ready():
    channel = bot.get_channel(828677373054287946)
    await channel.send(f'Залетаю в хату')


@bot.event
async def on_error():
    await channel.send('Кароче я сломался, бачок потик, иди нахуй')

bot.run(token)

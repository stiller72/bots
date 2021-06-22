import discord
from discord.ext import commands
import os
from conf import settings
import backend
import json
import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


def endSong(guild, path):
    os.remove(path)


class MyClient(discord.Client):

    def get_emoji(self, emoji):
        return discord.utils.get(client.emojis, name=emoji)


client = MyClient()


@client.event
async def on_message(message):
    if message.content.startswith('расскажи'):
        body = message.content
        question = {"query": body, "style": 1}
        answer = backend.balaboba(question)
        await message.channel.send(f'{body}{answer}')
    elif message.content.startswith('спасибо'):
        aga = client.get_emoji("aga")
        await message.add_reaction(aga)
        await message.channel.send(f'Всегда готов сосать хуи {aga}')


@client.event
async def on_message(message):
    if message.content.startswith('включи'):
        channel = message.author.voice.channel
        voice_client = await channel.connect()
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            file = ydl.extract_info(
                "https://www.youtube.com/watch?v=UoTPPlDv5cA", download=True)
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")
        guild = message.guild
        voice_client.play(discord.FFmpegPCMAudio(
            path), after=lambda x: endSong(guild, path))

        await voice_client.play("https://open.spotify.com/track/55qmtyvnYHkLsnEZGzrj8C?si=3d77f40795824951")


@client.event
async def on_ready():
    channel = client.get_channel(828677373054287946)
    # await channel.send(f'Залетаю в хату')


@client.event
async def on_resumed():
    await channel.send('Я вернулся')


@client.event
async def on_error():
    await channel.send('Кароче я сломался, бачок потик, иди нахуй')

client.run(settings['token'])

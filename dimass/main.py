import discord
from discord.ext import commands
import os
from conf import settings
import backend

client = discord.Client()


@client.event
async def on_message(message):
    if message.content.startswith('расскажи'):
        body = ('{} arguments: {}'.format(len(args), ', '.join(args)))
        question = {"query": body, "style": 1}
        answer = backend.balaboba(question)
        await message.channel.send(f'{body}{answer}')

@client.event
async def on_ready():
    print('d')

@client.event
async def on_connect():
    print('d')

@client.event
async def on_resumed():
    print('d')

@client.event
async def on_error(message, *args):
    await message.send('Кароче я сломался, бачок потик, иди нахуй')

client.run(settings['token'])

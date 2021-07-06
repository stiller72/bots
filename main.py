import discord
from discord.ext import commands
import backend
import os
from exceptions import BackendError

prefix = os.environ.get("PREFIX")
token = os.environ.get("TOKEN")

bot = commands.Bot(command_prefix=prefix)

# discord.on_command(ctx):
question_string = ["про", "как", "зачем",
                   "почему", "откуда",
                   "где", "какой", "какая",
                   "какое", "чей",
                   "что", "кто"]

styles_list = {
    1: "теорию заговора", 2: "репортаж", 3: "тост", 4: "цитату",
    5: "слоган", 6: "историю", 7: "instagram",
    8: "википедия", 9: "фильм", 10: "гороскоп", 11: "мудрость",

}


def get_emoj(emoji: str):
    return discord.utils.get(bot.emojis, name=emoji)


def get_style(question: str):
    style = 1
    for value, style_desc in styles_list.items():
        if style_desc in question:
            style = value

    return style


def parse_question(*args):
    question = ' '.join([word for word in args])
    return question


def parse_balaboba(start_string: str, question: str, style: int):
    if start_string in question_string:
        start_string = ''
    else:
        pass

    body = f'{start_string } ' + question
    question = {"query": body, "style": style}


@bot.command(name='расскажи')
async def balaboba(ctx, start_string: str = '', *args):

    if not start_string:
        await ctx.send('Ты ебанутый? Чиво рассказать?')
        return

    question = parse_question(*args)
    style = get_style(question)
    balaboba_string = parse_question(start_string, question, style)

    try:
        answer = backend.balaboba(balaboba_string)
    except BackendError:
        raise discord.DiscordException
    await ctx.send(f'{answer}')


@bot.listen()
async def on_message(message):
    if message.content.startswith('спасибо'):
        aga = get_emoj("aga")
        await message.channel.send(f'Всегда готов сосать хуи {aga}')


@bot.event
async def on_ready():
    channel = bot.get_channel(828677373054287946)
    await channel.send(f'Залетаю в хату')


@bot.listen()
async def on_error():
    await channel.send('Кароче я сломался, бачок потик, иди нахуй')

bot.run(token)

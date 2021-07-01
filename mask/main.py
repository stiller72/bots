import discord
from discord.ext import commands
import conf
import backend
import os 

bot = commands.Bot(command_prefix=conf.PREFIX)

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


@bot.command(name='расскажи')
async def balaboba(ctx, start_string: str = '', *args):
    style = 0

    if not start_string:
        await ctx.send('Ты ебанутый? Чиво рассказать?')
        return

    question = ' '.join([i for i in args])

    for value, style_desc in styles_list.items():
        if style_desc in question:
            style = value

    if not style:
        style = 0
    if start_string in question_string:
        start_string = ''
    else:
        pass

    body = f'{start_string } ' + question
    question = {"query": body, "style": style}
    print(question)
    try:
        answer = backend.balaboba(question)
    except BackendError:
        pass
    await ctx.send(f'{answer}')

@bot.listen()
async def on_message(message):
    if message.content.startswith('спасибо'):
        aga = get_emoj("aga")
        await message.channel.send(f'Всегда готов сосать хуи {aga}')


@bot.listen()
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


@bot.event
async def on_ready():
    channel = bot.get_channel(828677373054287946)
    await channel.send(f'Залетаю в хату')


@bot.event
async def on_resumed():
    await channel.send('Я вернулся')


@bot.event
async def on_error():
    await channel.send('Кароче я сломался, бачок потик, иди нахуй')

bot.run(conf.TOKEN)

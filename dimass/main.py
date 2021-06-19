import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


# Не передаём аргумент pass_context, так как он был нужен в старых версиях.
@bot.command()
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    # Объявляем переменную author и записываем туда информацию об авторе.
    author = ctx.message.author
    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(f'Hello, {author.mention}!')

# Обращаемся к словарю settings с ключом token, для получения токена
bot.run(settings['token'])

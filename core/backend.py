from exceptions import BackendError
import asyncio
from utils.balaboba import parse_question, parse_balaboba, get_style, fetch_boba
import discord

async def balaboba(ctx, start_string: str = '', *args):

    question = await parse_question(*args)
    style = await get_style(f'{start_string} {question}')
    context = await parse_balaboba(start_string=start_string, style=style, question=question)

    try:
        answer = await fetch_boba(context)
    except BackendError:
        raise discord.DiscordException

    return answer

import asyncio
import subprocess
from var import *

async def fetch_boba(context):
    query = context.get("query")
    style = context.get("style")
    print(query, style)
    try:
        process = subprocess.Popen(["./fetch.sh", f"{query}", f'{style}'], stdout=subprocess.PIPE)
        process.wait()
        output = process.stdout.read()
    except:
        raise BackendError
    return output.decode("utf-8")


async def get_style(question: str):
    style = 0
    for style_value, style_name in styles_list.items():
        if style_name in question:
            style = style_value

    return style


async def parse_question(*args):
    question = ' '.join(args)
    return question


async def parse_balaboba(start_string: str, style: int, question: str = ''):
    if start_string in question_list:
        start_string = ''
    else:
        pass

    body = f'{start_string } {question}'
    context = {"query": body, "style": style}

    return context

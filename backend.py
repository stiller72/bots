import subprocess
from exceptions import BackendError


def balaboba(context):
    query = context.get("query")
    style = context.get("style")
    try:
        process = subprocess.Popen(["./fetch.sh", f"{query}", f'{style}'], stdout=subprocess.PIPE)
        process.wait()
        output = process.stdout.read()
    except:
        raise BackendError
    return output.decode("utf-8")

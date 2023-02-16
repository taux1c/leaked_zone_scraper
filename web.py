import httpx
import config
headers = {'Referer':'https://leakedzone.com/','User-Agent': config.user_agent}

def visit(location):
    with httpx.Client(headers=headers,http2=True) as c:
        r = c.get(location)
        return r
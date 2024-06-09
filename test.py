import httpx
from selectolax.lexbor import LexborHTMLParser
from urllib.parse import (
    quote_plus,
    quote,
    unquote_plus,
    unquote
)

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 "
        "(Edition GX-CN)"
    )
}
client=httpx.Client()
content={}
result=[]

response=client.get(
    'https://scweb.cwa.gov.tw/zh-tw/earthquake/data',
    headers=headers
)
r=LexborHTMLParser(response.text)
e=r.css(".odd")
print(r.body.text())
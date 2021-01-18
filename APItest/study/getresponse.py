import json
from mitmproxy import http
from pprint import pprint

def response(flow: http.HTTPFlow):
    if "quote.json" in  flow.request.url and "x=" in flow.request.url:
        ##先接收到返回的信息
        data = json.loads(flow.rsponse.content)
        pprint(data)

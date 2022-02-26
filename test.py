# import cbpro
import requests
import json

sandbox = { "Website_bu" : "https://public.sandbox.exchange.coinbase.com",
"REST_API_bu" : "https://api-public.sandbox.exchange.coinbase.com",
"Websocket_Feed_bu" : "wss://ws-feed-public.sandbox.exchange.coinbase.com",
"FIX_API_bu" : "tcp+ssl://fix-public.sandbox.exchange.coinbase.com:4198" }

jso = json.dumps(sandbox)

sandObj = json.loads(jso)

print(sandObj['FIX_API_bu'])

# pc = cbpro.PublicClient()
# result = pc.get_products()

# for row in result:
    # print(row)
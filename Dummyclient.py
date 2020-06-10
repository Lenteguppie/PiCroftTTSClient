#! /usr/bin/env python3

# import sys
# from websocket import create_connection
# msg = 'Test message'
# uri = 'ws://192.168.86.56:8181/core'
# ws = create_connection(uri)
# # print("Sending " + msg + " to " + uri + "...")

# message = '{"utterance": ' + msg +'}' 
# serdat = "{'type': 'speak', 'data': "+ message +", 'context': None}"
# result = ws.send(serdat)  
# print("Receiving..." )
# result = ws.recv()  
# print("Received '%s'" % result)
# ws.close()


# from mycroft_bus_client import MessageBusClient, Message

# print('Setting up client to connect to a local mycroft instance')
# client = MessageBusClient(host='192.168.86.56')
# client.run_in_thread()

# print('Sending speak message...')
# client.emit(Message('speak', data={'utterance': 'Hello there, general Kenobi'}))

import asyncio
import websockets
from websockets import WebSocketServerProtocol
uri = 'ws://192.168.86.56:8181/core'

async def sendMsg(url):
    msg = '{"type": "speak", "data": {"utterance": "I am testing this message right now!"} }'
    # message = '{"type": \'speak\', "data": {"utterance": "I am testing this message right now!"}\}'
    print (msg)
    async with websockets.connect(uri) as ws:
        print("Waiting to receive from: " + url)

        
        result = await ws.send(msg)  
        print("Receiving..." )
        result = await ws.recv()  
        print("Received '%s'" % result)
        await ws.close()

start_server = sendMsg(uri)
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
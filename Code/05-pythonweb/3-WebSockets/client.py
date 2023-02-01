import asyncio
import websockets


async def client():

    websocket = await websockets.connect('ws://localhost:8002/')

    while True:
        name = input("Enter some data: ")

        print("To server: %s" % name)
        await websocket.send(name)

        resp = await websocket.recv()
        print("From server: %s" % resp)

asyncio.run(client())

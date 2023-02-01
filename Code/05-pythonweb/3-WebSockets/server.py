import asyncio
import websockets


async def onconnect(websocket, uri):

    while True:
        datain = await websocket.recv()
        print("From client: %s" % datain)

        dataout = "ECHO! " + datain
        print("To client:   %s" % dataout)

        await websocket.send(dataout)


async def start_server():
    async with websockets.serve(onconnect, 'localhost', 8002):
        await asyncio.Future()

asyncio.run(start_server())

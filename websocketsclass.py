import asyncio
import websockets

class websocketsclass(object):
    def __init__(self):
        print("Creating Websocket Class")

    async def sendMessage(self, websocket, path):
        name = await websocket.recv()
        print(f"< {name}")

        greeting = f"Hello {name}!"

        await websocket.send(greeting)
        print(f"> {greeting}")

    def startServer(self):
        start_server = websockets.serve(self.sendMessage, "localhost", 8765)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

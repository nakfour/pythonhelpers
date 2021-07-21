import asyncio
import websockets
class wesocketsclientclass(object):
    def __init__(self):
        printf("Client Class")

    async def connectToWebsocketServer(self, path):
        #uri = "ws://localhost:8765"
        async with websockets.connect(path) as websocket:
            name = input("What's your name? ")

            await websocket.send(name)
            print(f"> {name}")

            greeting = await websocket.recv()
            print(f"< {greeting}")
    def startClient(self, url):
        asyncio.get_event_loop().run_until_complete(self.connectToWebsocketServer(url))
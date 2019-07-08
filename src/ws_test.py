import asyncio
import websockets
import ssl

class WSTest:

    def __init__(self, uri):
        self.uri = uri
        self.query_parameters = {}

    def with_query_parameter(self, key, value):
        self.query_parameters[key] = value
        return self

    async def run(self):
        async with(websockets.connect(self.uri, ssl=ssl.SSLContext())) as websocket:
            pass
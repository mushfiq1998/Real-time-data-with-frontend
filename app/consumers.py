# Topic - Real time data with frontend example
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self, event):
        print('websocket connected...........', event)
        # Send request to server to accept connection
        self.send({
            'type': 'websocket.accept'
        }) 
    
    # Client sends data to Server, 
    def websocket_receive(self, event):
        print('Message received from client......', event['text'])
        # After receiving data server sends real time data to client.
        for i in range(10):
            self.send({
                'type': 'websocket.send'
                'text': str(i)
            })
            # send data after evry 1 second
            sleep(1)
    
    '''
    # Client sends data to Server, 
    def websocket_receive(self, event):
        print('Message received from client......', event['text'])
        # After receiving data server sends real time data to client.
        for i in range(10):
            self.send({
                'type': 'websocket.send'
                'text': json.dumps({"count": i})
            })
            # send data after evry 1 second
            sleep(1)
    '''

    def websocket_disconnect(self, event):
        print('websocket disconnected........', event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('websocket connected...........', event)
        # Send request to server to accept connection
        await self.send({
            'type': 'websocket.accept'
        }) 
    
    # Client sends data to Server, and Server receives it
    async def websocket_receive(self, event):
        print('Message received from client', event['text'])
        # After receiving data server sends real time data to client.
        for i in range(10):
            await self.send({
                'type': 'websocket.send'
                'text': str(i)
            })
            # server sends data to client after evry 1 second
            await asyncio.sleep(1)

    '''
    # Client sends data to Server, and Server receives it
    async def websocket_receive(self, event):
        print('Message received from client', event['text'])
        # After receiving data server sends real time data to client.
        for i in range(10):
            await self.send({
                'type': 'websocket.send'
                'text': json.dumps({"count": i})
            })
            # server sends data to client after evry 1 second
            await asyncio.sleep(1)
    '''
    
    async def websocket_disconnect(self, event):
        print('websocket disconnected........', event)
        raise StopConsumer()

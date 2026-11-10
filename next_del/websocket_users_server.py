import asyncio

import websockets
from websockets import ServerConnection


async def echo(websockets: ServerConnection):
    async for message in websockets:
        print(f'Получено сообщение: {message}')
        for i in range(5):
            response = f'{i + 1} Сервер обработал сообщение: {message}'
            await websockets.send(response)

async def main():
    server = await websockets.serve(echo, host='localhost', port=8765)
    print('websoket сервер запущен на порту: ws://localhost:8765')
    await server.wait_closed()

asyncio.run(main())
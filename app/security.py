import asyncio


async def on_response_prepare(request, response):
    response.headers['Server'] = 'Risitas'


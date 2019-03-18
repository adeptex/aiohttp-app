from aiohttp import web
import aiohttp_jinja2
import jinja2
import json

async def index_get(request):
    return aiohttp_jinja2.render_template('index.html', request, {
        'message': 'Online'
    })

async def index_post(request):
    return aiohttp_jinja2.render_template('index.html', request, {
        'message': json.dumps(await request.json(), indent=4)
    })
from aiohttp import web
import aiohttp_jinja2
import jinja2
import json

async def index(request):
    return aiohttp_jinja2.render_template('index.html', request, {
        'message': 'Online'
    })

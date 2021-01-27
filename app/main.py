from aiohttp import web
from routes import setup_routes, setup_static_routes
from middlewares import setup_middlewares
from database import sql
from security import on_response_prepare
import threading
import aiohttp_jinja2
import jinja2
import argparse
import yaml
import ssl


def parse_args():
    argsParser = argparse.ArgumentParser(description='')
    argsParser.add_argument("--config", "-c", required=True, help="Configuration file")
    return argsParser.parse_args()

def load_config(config):
    with open(config, 'r') as stream:
        return yaml.safe_load(stream)

def tls(config):
    if config['tls']['enable']:
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain(
            config['tls']['certificate'],
            config['tls']['key'],
        )
    else:
        context = None

    return context

def main():
    # config
    args = parse_args()
    config = load_config(args.config)

    # database
    # print('SQLite {}'.format(sql('select sqlite_version()')[0][0]))

    # bot
    # threading.Thread(target=bot).start()

    # webapp
    app = web.Application()
    app.on_response_prepare.append(on_response_prepare)
    setup_static_routes(app)
    setup_routes(app)
    setup_middlewares(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('app/templates'))
    web.run_app(app, host=config['host'], port=config['port'], ssl_context=tls(config))


main()

from aiohttp import web
from routes import setup_routes, setup_static_routes
from security import on_response_prepare
import threading
import aiohttp_jinja2
import jinja2
import argparse
import yaml


def parse_args():
    argsParser = argparse.ArgumentParser(description='')
    argsParser.add_argument("--config", "-c", required=True, help="Configuration file")
    return argsParser.parse_args()

def load_config(config):
    with open(config, 'r') as stream:
        return yaml.safe_load(stream)


# config
args = parse_args()
config = load_config(args.config)

# bot
# threading.Thread(target=bot).start()

# webapp
app = web.Application()
app.on_response_prepare.append(on_response_prepare)
setup_static_routes(app)
setup_routes(app)
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('app/templates'))
web.run_app(app, host=config['host'], port=config['port'])


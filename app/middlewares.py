from aiohttp import web
from pathlib import Path

LOG = Path(".").resolve().joinpath("access.log")


async def handle_404(request):
    print(request)
    body = None
    if request.method != "GET":
        body = await request.text()
        print(body)
    with LOG.open("a") as fh:
        fh.write(f"{request.method} {request.path}\n")
        if body:
            fh.write(f"{body}\n")
    return web.Response(text="", status=200)


def create_error_middleware(overrides):

    @web.middleware
    async def error_middleware(request, handler):
        try:
            return await handler(request)
        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)
            raise
        except Exception:
            return await overrides[500](request)

    return error_middleware


def setup_middlewares(app):
    print(f"Access log: {LOG}")
    error_middleware = create_error_middleware({
        404: handle_404
    })
    app.middlewares.append(error_middleware)


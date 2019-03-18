from views import index_get, index_post


def setup_static_routes(app):
    app.router.add_static('/img/', path='app/img', name='img')
    app.router.add_static('/css/', path='app/css', name='css')
    app.router.add_static('/js/', path='app/js', name='js')

def setup_routes(app):
    app.router.add_get('/', index_get)
    app.router.add_post('/', index_post)
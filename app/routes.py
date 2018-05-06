from views import index


def setup_static_routes(app):
    app.router.add_static('/images/', path='app/images', name='img')
    app.router.add_static('/css/', path='app/css', name='css')
    app.router.add_static('/js/', path='app/js', name='js')

def setup_routes(app):
    app.router.add_get('/', index)
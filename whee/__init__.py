from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('register_view', '/')
    config.add_route('confirm', '/confirm')
    config.add_static_view('deform_static', 'deform:static/')
    config.scan()
    return config.make_wsgi_app()

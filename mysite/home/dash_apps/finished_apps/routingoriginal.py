
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler


from django.conf.urls import url


from .consumers import MessageConsumer, PokePipeConsumer
from .util import pipe_ws_endpoint_name, http_endpoint, http_poke_endpoint_enabled


# TODO document this and discuss embedding with other routes



http_routes = [
    ]


if http_poke_endpoint_enabled():
    http_routes.append(url(http_endpoint("poke"), PokePipeConsumer))


http_routes.append(url("^", AsgiHandler)) # AsgiHandler is 'the normal Django view handlers'


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(URLRouter([url(pipe_ws_endpoint_name(), MessageConsumer),])),
    'http': AuthMiddlewareStack(URLRouter(http_routes)),
    })

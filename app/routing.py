from app.consumers import ShoutboxConsumer
from channels.routing import route_class

channel_routing = [
    route_class(ShoutboxConsumer, path=r"^/shoutbox"),
]


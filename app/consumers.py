
from app.models import Message
from channels.generic.websockets import JsonWebsocketConsumer
from django.template.defaultfilters import date


class ShoutboxConsumer(JsonWebsocketConsumer):

    def connection_groups(self):
        return ['all']

    def receive(self, content):
        message = Message.objects.create(**content)
        content.update(sent_at=date(message.sent_at, 'r'))
        self.group_send('all', content)

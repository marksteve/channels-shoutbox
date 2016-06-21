from __future__ import unicode_literals

from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)


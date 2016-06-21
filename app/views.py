from app.models import Message
from django.shortcuts import render


def index(request):
    messages = Message.objects.order_by('-sent_at').all()
    return render(request, 'index.html', {'messages': messages})

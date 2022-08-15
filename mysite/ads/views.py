from django.http import HttpResponse
from .models import Ad


def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for ad in Ad.objects.all():
        s += ad.title + '\r\n' + ad.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')

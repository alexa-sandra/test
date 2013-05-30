# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from models import Person


def index(request):
    info = Person.objects.get(pk=1)
    print info
    template = loader.get_template('index.html')
    context = Context({
        'info': info,
    })
    return HttpResponse(template.render(context))

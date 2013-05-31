# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import loader, Context
from models import Person
from testJobs42.personalinfo.forms import PersonForm


def index(request):
    info = Person.objects.get(pk=1)
    template = loader.get_template('index.html')
    context = Context({
        'info': info,
    })
    return HttpResponse(template.render(context))

def edit(request):
    info = Person.objects.get(pk=1)
    if request.method == 'POST': 
            form = PersonForm(request.POST)
            if form.is_valid():
                info.first_name = form.cleaned_data['first_name']
                info.last_name = form.cleaned_data['last_name']
                info.birth_date = form.cleaned_data['birth_date']
                info.bio = form.cleaned_data['bio']
                info.email = form.cleaned_data['email']
                info.jabber = form.cleaned_data['jabber']
                info.other_contacts = form.cleaned_data['other_contacts']
                info.save()
                return HttpResponseRedirect(reverse(index)) # Redirect after POST
        else:
            form = PersonForm(instance=info)
            template = loader.get_template('edit.html')
            #return render_to_response(
            #'about/about_me_edit.html',
            #locals()
            #)
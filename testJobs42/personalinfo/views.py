# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader, Context
from sorl.thumbnail.fields import ImageField
from models import Person
from testJobs42.personalinfo.forms import PersonForm

def index(request):
    try:
        info = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        info = None
    return render(request, 'index.html', {'info': info})

@login_required()
def edit(request):
    try:
        info = Person.objects.get(pk=1)
    except Person.DoesNotExist:
        return render(request,'index.html',{'info':None})
    
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            up_file = request.FILES['photo']

            #img = ImageField(upload_to='images/uploads', null=True, blank=True)
            #img.value_from_object(up_file)
            info.photo = up_file

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
        return render(request, 'edit.html', locals())
        
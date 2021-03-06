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

    if request.is_ajax():#submit ajax form
        form = PersonForm(request.POST, request.FILES, instance=info)
        if form.is_valid():
            if request.FILES:
                form.cleaned_data['photo'] = request.FILES['photo']
            form.save()
            return render(request, 'edit.html', locals()) # Redirect after POST

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES:
                info.photo = request.FILES['photo']
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
        
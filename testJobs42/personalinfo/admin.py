# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class PersonAdmin(admin.ModelAdmin):
    pass

class HttpStoredQueryAdmin(admin.ModelAdmin):
    pass

class ModelsActionsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(HttpStoredQuery, HttpStoredQueryAdmin)
admin.site.register(ModelsActions, ModelsActionsAdmin)
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from personalinfo import views

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^edit/', views.edit, name='edit'),
     url(r'^admin/', include(admin.site.urls)),
)

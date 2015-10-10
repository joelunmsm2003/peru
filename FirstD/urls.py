from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'FirstD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ingresar/$', 'PeruCall.views.ingresar'),
    url(r'^salir/$', 'PeruCall.views.salir'),

    url(r'^menu/$', 'PeruCall.views.menu'),
    url(r'^agentes/$', 'PeruCall.views.agentes'),
    url(r'^data/$', 'PeruCall.views.data'),


)

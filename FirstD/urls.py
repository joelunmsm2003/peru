from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.models import User


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ingresar/$', 'PeruCall.views.ingresar'),
    url(r'^salir/$', 'PeruCall.views.salir'),
    url(r'^menu/$', 'PeruCall.views.menu'),
    url(r'^usuario/$', 'PeruCall.views.usuario'),
    url(r'^usuarios/$', 'PeruCall.views.usuarios'),
    url(r'^agentes/$', 'PeruCall.views.agentes'),
    url(r'^empresa/', 'PeruCall.views.empresa'),
    url(r'^empresas/', 'PeruCall.views.empresas'),
    url(r'^usuarios/$', 'PeruCall.views.usuarios'),
    url(r'^usuario/', 'PeruCall.views.usuario'),
    url(r'^user/', 'PeruCall.views.user'),
    url(r'^nivel/', 'PeruCall.views.nivel'),
    url(r'^$', 'PeruCall.views.ingresar'), 
    url(r'^campania/', 'PeruCall.views.campania'), 
    url(r'^micampania/', 'PeruCall.views.micampania'),
    url(r'^campanias/', 'PeruCall.views.campanias'),  
    url(r'^uploadCampania/', 'PeruCall.views.uploadCampania'),
    url(r'^adminCampania/(\w+)/$', 'PeruCall.views.adminCampania'),
    url(r'^agentesdisponibles/(\w+)/$', 'PeruCall.views.agentesdisponibles'),
    url(r'^agentescampania/(\w+)/$', 'PeruCall.views.agentescampania'),
    url(r'^agregaragente/', 'PeruCall.views.agregaragente'),
    url(r'^quitaragente/', 'PeruCall.views.quitaragente'),
    url(r'^supervisores/', 'PeruCall.views.supervisores'),
    url(r'^monitoreo/(\w+)/$', 'PeruCall.views.monitoreo'),
    url(r'^agentes/(\w+)/$', 'PeruCall.views.agentes'),
    url(r'^troncales/$', 'PeruCall.views.troncales'),

    url(r'^teleoperador/(\w+)/$', 'PeruCall.views.teleoperador'),

)




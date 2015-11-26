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
    url(r'^campanias/', 'PeruCall.views.campanias'),  
    url(r'^uploadCampania/', 'PeruCall.views.uploadCampania'),
    url(r'^adminCampania/(\w+)/$', 'PeruCall.views.adminCampania'),
    url(r'^agentesdisponibles/(\w+)/$', 'PeruCall.views.agentesdisponibles'),
    url(r'^agentescampania/(\w+)/$', 'PeruCall.views.agentescampania'),
    url(r'^agregaragente/', 'PeruCall.views.agregaragente'),
    url(r'^quitaragente/', 'PeruCall.views.quitaragente'),
    url(r'^supervisores/', 'PeruCall.views.supervisores'),
    url(r'^reasignarsupervisor/', 'PeruCall.views.reasignarsupervisor'),

    url(r'^monitoreo/(\w+)/$', 'PeruCall.views.monitoreo'),
    url(r'^agentes/(\w+)/$', 'PeruCall.views.agentes'),
    url(r'^troncales/$', 'PeruCall.views.troncales'),
    url(r'^filtros/(\w+)/$', 'PeruCall.views.filtros'),
    url(r'^carterasupervisor/(\w+)/$', 'PeruCall.views.carterasupervisor'),
    url(r'^carteranosupervisor/(\w+)/$', 'PeruCall.views.carteranosupervisor'),
    url(r'^listafiltros/(\w+)/$', 'PeruCall.views.listafiltros'),
    url(r'^ciudad/', 'PeruCall.views.ciudad'),
    url(r'^grupo/', 'PeruCall.views.grupo'),
    url(r'^segmento/', 'PeruCall.views.segmento'),
    url(r'^cartera/', 'PeruCall.views.cartera'),
    url(r'^carteras/', 'PeruCall.views.carteras'),
    url(r'^agregarfiltro/', 'PeruCall.views.agregarfiltro'),
    url(r'^eliminarfiltro/', 'PeruCall.views.eliminarfiltro'),
    url(r'^reportes/(\w+)/$', 'PeruCall.views.reportes'),
    url(r'^resultadofiltro/(\w+)/$', 'PeruCall.views.resultadofiltro'),
    url(r'^home/', 'PeruCall.views.home'),
    url(r'^agregarcartera/', 'PeruCall.views.agregarcartera'),

  
    url(r'^teleoperador/(\w+)/$', 'PeruCall.views.teleoperador'),
    url(r'^menu/$', 'PeruCall.views.menu'),

    url(r'^status_f/(\w+)/$', 'PeruCall.views.status_f'),
    url(r'^status_g/(\w+)/$', 'PeruCall.views.status_g'),
    url(r'^status_h/(\w+)/$', 'PeruCall.views.status_h'),
    url(r'^resultado/$', 'PeruCall.views.resultado'),


)




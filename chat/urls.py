from django.conf.urls import include, url
from django.contrib import admin
from chatapp import urls
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth_views.login),
    url(r'^', include('chatapp.urls')),
    url(r'^logout/$', auth_views.logout),
]

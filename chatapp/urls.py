from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$',  views.about, name='home'),#about
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
    
]

from django.conf.urls import include, url
from .views import home, register, about, new_room, chat_room

urlpatterns = [

	url(r'^$', home),
    url(r'^register/', register),
    url(r'^$',  views.about, name='about'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]

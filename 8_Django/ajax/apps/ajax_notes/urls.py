from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^notes/$', views.notes, name = "notes"),
    url(r'^create/$', views.create, name = "create"),
    url(r'^delete/$', views.delete, name = "delete"),
    url(r'^update/$', views.update, name = "update"),
]
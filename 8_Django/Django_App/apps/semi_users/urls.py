from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/new$', views.new, name='new'),
    url(r'^users/create$', views.create, name='create'),
    url(r'^users/update$', views.update, name='update'),
    url(r'^users/(?P<userid>\d+)/edit$', views.edit, name='edit'),
    url(r'^users/(?P<userid>\d+)/destroy$', views.destroy, name='destroy'),
    url(r'^users/(?P<userid>\d+)/', views.identify, name='identify'),
]
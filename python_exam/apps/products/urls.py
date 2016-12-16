from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^dashboard$', views.index, name='products_index'),
    url(r'^create$', views.create, name='products_create'),
    url(r'^wish_items/create$', views.createpage, name='products_createpage'),
    url(r'^wish_items/(?P<id>\d+)$', views.wishpage, name='products_wishpage'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='products_delete'),
    url(r'^wishadd/(?P<id>\d+)$', views.wishadd, name='wish_add'),
]

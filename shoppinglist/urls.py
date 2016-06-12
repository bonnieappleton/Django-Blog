from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.shopping_list, name='shopping_list'),
]

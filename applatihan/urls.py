from django.conf.urls import url
from applatihan import views

urlpatterns = [
    url('', views.index, name='index'),
]



# from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns=[
    
    url('',views.index,name='index'),
    url('<int:movies_id>',views.details,name='details')

]
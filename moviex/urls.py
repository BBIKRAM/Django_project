from django.urls import path
# from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns=[
    
    path('',views.index,name='index'),
    path('<int:movies_id>',views.details,name='details')

]
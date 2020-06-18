from django.db import models
from tastypie.resources import ModelResource
from moviex.models import movies
from tastypie.api import Api

# Create your models here.
class MoviesResources(ModelResource):
    class Meta:
        queryset =movies.objects.all()
        resource_name = 'movies'

a_api=Api(api_name='a')
a_api.register(MoviesResources())
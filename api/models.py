from django.db import models
from tastypie.resources import ModelResource
from songs.models import Song


# Create your models here.


class SongResource(ModelResource):
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'songs'
        excludes = ['number_of_plays']
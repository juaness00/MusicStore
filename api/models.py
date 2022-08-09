from django.db import models
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.validation import Validation
from songs.models import Song


# Create your models here.


class SongResource(ModelResource):
    class Meta:
        queryset = Song.objects.all()
        resource_name = 'songs'
        excludes = []
        authorization = Authorization()
        authentication = Authentication()
        validation = Validation()
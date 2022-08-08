from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Song
# Create your views here.

def index(request):
    songs = Song.objects.all()
    return render(request, 'songs/index.html', {'songs': songs})

def detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    return render(request, "songs/detail.html", {'song': song})


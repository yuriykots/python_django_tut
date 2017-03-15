from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

# Create your views here.



def index(request):
    #making a call to database and storing all objects in all_albums
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums }
    #behind a scene render() converts in in http response
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details on album ID  " + str(album_id)+ "</h2>")

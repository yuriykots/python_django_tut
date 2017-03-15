from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

# Create your views here.



def index(request):
    #making a call to database and storing all objects in all_albums
    all_albums = Album.objects.all()
    #behind a scene render() converts in in http response
    return render(request, 'music/index.html', {'all_albums': all_albums })

def detail(request, album_id):
    #using this shortcut instead of try / except loop
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' : album})

# receiving post method.
# request.POST['song'] - will have a value of selected song.
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = request.POST['song'])
# Printing request.POST in console
        print(request.POST)
#If there is an error/DoesNotExist trowing error
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song",
        })
#If everything is good redirecting to detail view.
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album' : album})

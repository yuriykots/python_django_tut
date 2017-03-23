
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Album
from .forms import UserForm
from django.http import HttpResponse



def testDetail(request, pk):
    return HttpResponse("<h1> Test View:  " +str(pk) + "</h1>")

def test(request):
    return render(request, 'music/test.html')

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    # what fields do you need.
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    # what fields do you need.
    fields = ['artist', 'album_title', 'genre', 'album_logo']
    success_url = "/music/"

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    #importing from our forms file
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self, request):
        #We want to show empty form.
        form = self.form_class(None)
        #we are rendering empty html form. Our template gets
        #form object.
        return render(request, self.template_name, {'form': form })

    # process form data
    def post(self, request):
        #We want to submit filled form
        #request.POST will have all information.
        form = self.form_class(request.POST)

        if form.is_valid():

            #it will create an Object from the form.
            #we are storing in localy for now.
            user = form.save(commit=False)
            # cleaned (normalized) data
            # for example you want the same day format.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # whenever you are changing user password
            # u need to use set_password function
            # djnago will has it for you.
            user.set_password(password)
            user.save()

            #this functions check database if this user actually exist.
            user = authenticate(username=username, password=password)
            #returns User object if credentials are correct

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')
        return render(request, self.template_name, {'form': form })







#{% url 'music:album-delete' album.id %}

from django import template
from django.shortcuts import redirect, render
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth import authenticate, login, logout
from .forms import ContactForm, CreateUserForm
from django.urls.base import reverse_lazy


from .models import Album, Artist, Category, Music


class MusicListView(ListView):
    """List of musics"""
    model = Music
    template_name = "musics/index.html"
    context_object_name = "musics"
    queryset = Music.objects.filter(draft=False)
    paginate_by = 3



class AlbumListView(ListView):
    """List of albums"""
    model = Album
    context_object_name = "albums"
    slug_field = "url"
    queryset = Album.objects.all()


class AlbumDetailView(DetailView):
    """Album detail"""
    model = Album
    template_name = 'musics/album_detail.html'
    context_object_name = "album"
    slug_field = "url"


    def get_context_data(self, **kwargs):
        """get selected album objects"""
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['albums'] = self.get_object().music_album.all
        return context


class ArtistListView(ListView):
    "List of artist, composer, lyricist"
    model = Artist
    context_object_name = "artists"
    slug_field = "name"
    queryset = Artist.objects.all()


class ArtistDetailView(DetailView):
    model = Artist
    template_name = 'musics/artist_detail.html'
    context_object_name = 'artists'
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        """get selected artist objects"""
        context = super(ArtistDetailView, self).get_context_data(**kwargs)
        context['artist'] = self.get_object().music_artist.all
        return context


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "musics/index.html")
    form = ContactForm()
    context = {"form": form}
    return render(request, "contact/contact.html", context)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account created" + user)

                return redirect('login')


        context = {"form": form}
        return render(request, "musics/register.html", context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username or password is incorrect")


        # context = {}
        return render(request, "musics/login.html")


def logoutUser(request):
    logout(request)
    return redirect("login")


# def error_404(request, exception):
#     return render(request, "musics/404.html")

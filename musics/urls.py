from django import views
from django.urls import path
from django.conf import settings
# from .views import MusicListView, AlbumListView, ArtistListView, album_detail, ArtistDetailView, ContactFormView
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.MusicListView.as_view(), name="home"),
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    
    path("albums/", views.AlbumListView.as_view(), name="albums"),
    path("artists/", views.ArtistListView.as_view(), name="artists"),
    path('contact/', views.contact_view, name='contact'),
    path("album/<str:slug>/", views.AlbumDetailView.as_view(), name="album_detail"),
    path("artist/<str:slug>/", views.ArtistDetailView.as_view(), name="artist_detail"),
]
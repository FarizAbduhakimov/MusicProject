from django.conf import settings
import os.path
from django.db import models
from django.urls import reverse
from datetime import date
from django.db.models.fields import TextField



class Category(models.Model):
    """Musics categories"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Artist(models.Model):
    """Artists, lyricists & composers"""
    name = models.CharField("Name", max_length=150)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Picture", upload_to="artists/")
    url = models.SlugField(max_length=150, null=True, unique=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Artist, lyricist and composer"
        verbose_name_plural = "Artists"
        ordering = ['-time_create',]


class Genre(models.Model):
    "Genres"
    name = models.CharField("Name", max_length=150)
    description = models.TextField("Description")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"


class Album(models.Model):
    title = models.CharField("Title", null=True, max_length=150)
    description = models.TextField("Description", null=True)
    image = models.ImageField("Picture", null=True, upload_to="albums/")
    url = models.SlugField(max_length=150, null=True, unique=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)

    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        ordering = ['-time_create',]


class Music(models.Model):
    """Musics"""
    # music_id = models.AutoField(primary_key= True)
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description")
    poster = models.ImageField("Poster", upload_to="musics_poster/")
    year = models.PositiveSmallIntegerField("Date of public", default=2022)
    country = models.CharField("Country", max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, verbose_name="artist", related_name="music_artist")
    composer = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, verbose_name="composer", related_name="music_composer")
    lyricist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True, verbose_name="lyricist", related_name="music_lyricist")
    album = models.ForeignKey(Album, null=True, on_delete=models.CASCADE, verbose_name="album", related_name="music_album")
    premiere = models.DateField("Premiere in world", default=date.today)
    genres = models.ManyToManyField(Genre, verbose_name="genres")
    music_file = models.FileField("Music file", upload_to="musics/", null=True)
    category = models.ForeignKey(
        Category, verbose_name="categories", on_delete=models.SET_NULL, null=True
    )
    url = models.SlugField(max_length=150, unique=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('music', kwargs={"slug": self.url})

    def audio_file_player(self):
        if self.audio_file:
            file_url = settings.MEDIA_URL + str(self.audio_file)
            player_string = '<audio src="%s" controls>Your browser does not support the audio element.</audio>' % (file_url)
            return player_string

    audio_file_player.allow_tags = True
    audio_file_player.short_description = ('Audio file player')


    class Meta:
        # db_table="Music"
        verbose_name = "Music"
        verbose_name_plural = "Musics"
        ordering = ['-time_create',]


# class MusicBanners(models.Model):
#     """Banners in music"""
#     title = models.CharField("Title", max_length=150)
#     description = models.TextField("Description")
#     image = models.ImageField("Picture", upload_to="music_banners/")
#     music = models.ForeignKey(Music, verbose_name="Music", on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = "Music banner"
#         verbose_name_plural = "Music banners" 


class Contact(models.Model):
    """Contact"""
    name = models.CharField("Name", max_length=150)
    email = models.EmailField()
    music = models.CharField("Music title", max_length=150)
    message = models.TextField("Message")

    def __str__(self):
        return self.email

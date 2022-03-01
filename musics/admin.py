from django.contrib import admin
from django.forms import fields
from django.utils.safestring import mark_safe
from .models import Category, Artist, Genre, Album, Music, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Cateogry admin"""
    search_fields = ("name",)
    list_display = ("id", "name", "url")
    list_display_links = ("name",)


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "music_file", "url", "draft")
    list_filter = ("category", "artist", "year")
    search_fields = ("title", "category__name")
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    actions = ["publish", "unpublish"]
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (("title"), )
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"), ("music_file"))
        }),
        (None, {
            "fields": (("year", "premiere", "country"), )
        }),
        ("Artist", {
            "classes": ("collapse",),
            "fields": (("artist", "composer", "lyricist"), ("album", "genres", "category"), )
        }),
        ("Options", {
            "fields": (("url", "draft"), )
        }),
        
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100px">')

    def unpublish(self, request, queryset):
        """Unpublish"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 object has been updated"
        else:
            message_bit = f"{row_update} objects has been updated"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Publish"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 object has been updated"
        else:
            message_bit = f"{row_update} objects has been updated"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Publish"
    publish.allowed_permissions = ('change', )

    unpublish.short_description = "Unpublish"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Image"

    get_image.short_description = "Poster"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genre"""
    search_fields = ("name",)
    list_display = ("name", "url")


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    """Album"""
    search_fields = ("title",)
    list_display = ("title", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50px">')

    get_image.short_description = "Image Album"


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    """Artist"""
    search_fields = ("name",)
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50px">')

    get_image.short_description = "Image Artist"

admin.site.register(Contact)
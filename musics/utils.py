# from django.db.models.aggregates import Count
# from .models import *

# class DataMixin:
#     # paginate_by = 3
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         albums = Music.objects.annotate(Count('musics'))

#         # user_menu = menu.copy()
#         # if not self.request.user.is_authenticated:
#         #     user_menu.pop(1)

#         # context['menu'] = user_menu

#         context['albums'] = albums
#         if 'album_selected' not in context:
#             context['album_selected'] = 0
#         return context
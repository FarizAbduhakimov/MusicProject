from django import template
from musics.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    """Output all categories"""
    return Category.objects.all()

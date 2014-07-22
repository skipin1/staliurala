from django.conf import settings
from os.path import join
from django import template

register = template.Library()

@register.simple_tag
def get_font_path():
    return join(settings.STATIC_ROOT, 'catalog/fonts/DejaVuSans.ttf')
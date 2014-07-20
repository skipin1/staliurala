from django.conf.urls import patterns, url
from .views import EasyPDF, CategoryDetailView


urlpatterns = patterns('catalog.views',
    url(r'category/(?P<slug>[a-zA-Z0-9\-]+)/$', CategoryDetailView.as_view(), name='category'),
)

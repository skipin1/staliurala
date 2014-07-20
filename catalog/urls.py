from django.conf.urls import patterns, url
from .views import EasyPDF


urlpatterns = patterns('catalog.views',
    url(r'category/(?P<slug>[a-zA-Z0-9\-]+)/$', 'some_view'),
    url(r'product/(?P<slug>[a-zA-Z0-9\-]+)/$', 'some_view'),
    url(r'product/(?P<slug>[a-zA-Z0-9\-]+)/price/$', 'some_view'),
)

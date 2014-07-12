from django.conf.urls import patterns, url


from .views import EasyPDF

urlpatterns = patterns('catalog.views',
    url(r'test/$', 'catalog_view', name='catalog'),
    url(r'easy-pdf-html/$', 'easy_pdf_html'),
    url(r'easy-pdf/$', EasyPDF.as_view()),
    url(r'pdf/$', 'some_view'),
)

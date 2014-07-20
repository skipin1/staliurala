# -*- coding: utf-8 -*-

from .models import CategoryBlock, Category, Price
from django.views.generic import TemplateView, DetailView
from easy_pdf.views import PDFTemplateView
from tools.parser import Parser


class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['block_list'] = CategoryBlock.objects.filter(is_active=True).prefetch_related('categories')
        return context


class CategoryDetailView(DetailView):
    template_name = 'catalog/category.html'
    model = Category


class EasyPDF(PDFTemplateView):
    template_name = 'price_template.html'
    pdf_filename = 'dudu.pdf'

    def get_context_data(self, **kwargs):
        context = super(EasyPDF, self).get_context_data(
            # pagesize="A4",
            # title="Hi there 22222",
            **kwargs
        )

        context['table'] = self.get_table()
        context['title'] = self.price_obj.title
        return context

    def get_table(self):
        p = Parser()
        return p.get_table(self.price_obj.url)

    def set_file_name(self):
        self.pdf_filename = u'price-%s.pdf' % self.price_obj.pk


    def get(self, request, *args, **kwargs):
        self.price_obj = Price.objects.get(pk=kwargs['pk'])
        self.set_file_name()
        return super(EasyPDF, self).get(request, *args, **kwargs)

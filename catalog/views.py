# -*- coding: utf-8 -*-

from .models import CategoryBlock, Category, Price
from django.views.generic import TemplateView, DetailView
from easy_pdf.views import PDFTemplateView


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
        return super(EasyPDF, self).get_context_data(
            pagesize="A4",
            title="Hi there 22222",
            **kwargs
        )
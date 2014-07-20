# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render
from easy_pdf.views import PDFTemplateView


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class EasyPDF(PDFTemplateView):
    template_name = 'price_template.html'
    pdf_filename = 'dudu.pdf'

    def get_context_data(self, **kwargs):
        return super(EasyPDF, self).get_context_data(
            pagesize="A4",
            title="Hi there 22222",
            **kwargs
        )
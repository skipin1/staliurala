# -*- coding: utf-8 -*-

from .models import CategoryBlock, Category, Price
from django.views.generic import TemplateView, DetailView
# from easy_pdf.views import PDFTemplateView
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



from django.http import HttpResponse, Http404
from xhtml2pdf import pisa


class PDFTemplateView(TemplateView):
    template_name = 'price_template.html'
    pdf_file_name = ''

    def get_context_data(self, **kwargs):
        context = super(PDFTemplateView, self).get_context_data(**kwargs)
        context['title'] = self.price_obj.title
        context['table'] = str(self.get_table())
        return context

    def render_to_response(self, context, **response_kwargs):
        template_response = super(PDFTemplateView, self).render_to_response(context, **response_kwargs)
        html = str(template_response.render())

        response = HttpResponse(mimetype='application/pdf')
        # response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % self.pdf_file_name
        response['Content-Type'] = 'application/pdf'

        try:
            pisaStatus = pisa.CreatePDF(
                src = html,
                dest=response,
                encoding='utf-8',
            )
        except:
            raise Http404

        return response

    def get_table(self):
        p = Parser()
        return p.get_table(self.price_obj.url)

    def set_file_name(self):
        self.pdf_file_name = u'price-%s.pdf' % self.price_obj.pk


    def get(self, request, *args, **kwargs):
        self.price_obj = Price.objects.get(pk=kwargs['pk'])
        self.set_file_name()
        return super(PDFTemplateView, self).get(request, *args, **kwargs)

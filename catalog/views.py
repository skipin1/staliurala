# -*- coding: utf-8 -*-

from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.shortcuts import render


def some_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    p = canvas.Canvas(response)
    p.drawString(100, 100, 'Hello world.')

    p.showPage()
    p.save()
    return response


def catalog_view(request):
    return HttpResponse('<h3>Catalog page</h3>')


def easy_pdf_html(request):
    return render(request, 'easy_pdf.html')


from easy_pdf.views import PDFTemplateView

class EasyPDF(PDFTemplateView):
    template_name = 'easy_pdf.html'
    pdf_filename = 'dudu.pdf'

    def get_context_data(self, **kwargs):
        return super(EasyPDF, self).get_context_data(
            pagesize="A4",
            title="Hi there 22222",
            **kwargs
        )
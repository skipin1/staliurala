from django.contrib import admin
from .models import Partner
from django_summernote.admin import SummernoteModelAdmin


class PartnerAdmin(SummernoteModelAdmin):
    list_display = ('logo', 'title')


admin.site.register(Partner, PartnerAdmin)

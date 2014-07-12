from django.contrib import admin
from .models import Partner


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title')


admin.site.register(Partner, PartnerAdmin)

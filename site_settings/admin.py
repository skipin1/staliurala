from django.contrib import admin
from .models import SiteSetting, HeaderPhone, ManagerPhone, LogisticPhone
from django.http import HttpResponseRedirect


class HeaderPhoneInline(admin.TabularInline):
    model = HeaderPhone
    extra = 0


class ManagerPhoneInline(admin.TabularInline):
    model = ManagerPhone
    extra = 0


class LogisticPhoneInlline(admin.TabularInline):
    model = LogisticPhone
    extra = 0


class SiteSettingAdmin(admin.ModelAdmin):
    inlines = [
        HeaderPhoneInline,
        ManagerPhoneInline,
        LogisticPhoneInlline,
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def response_change(self, request, obj):
        if request.POST.has_key('_save'):
            return HttpResponseRedirect('/admin/')
        else:
            return super(SiteSettingAdmin, self).response_change(request, obj)



admin.site.register(SiteSetting, SiteSettingAdmin)


# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import CategoryBlock, Category, Price
from .forms import CategoryBlockAdminForm, CategoryAdminForm
from django.contrib.auth.models import User, Group
from django_summernote.admin import SummernoteModelAdmin



class CategoryBlockAdmin(SummernoteModelAdmin):
    form = CategoryBlockAdminForm
    list_display = ('title', 'form_type', 'move_list', 'is_active')
    list_filter = ('is_active', 'form_type')
    fields = ('title', 'is_active', 'image', 'description', 'form_type', 'move_type',)
    # search_fields = ('title',)

    def move_list(self, obj):
        move_list = obj.move_type.all()
        if len(move_list) == 2:
            return u'%s и %s' % (move_list[0], move_list[1])
        else:
            return u'%s' % move_list[0]
    move_list.short_description = u'Увеличение блока'


class PriceInline(admin.TabularInline):
    model = Price
    extra = 0
    fields = ('title', 'url', 'is_active')


class CategoryAdmin(SummernoteModelAdmin):
    form = CategoryAdminForm
    list_display = ('title', 'block', 'is_active')
    ordering = ('title',)
    list_filter = ('is_active', 'block')
    fieldsets = (
        (None, {
            'fields': ('title', 'is_active', 'block', 'image', 'description')
        }),
        ('SEO параметры', {
            'fields': ('seo_title', 'seo_keywords', 'seo_description')
        }),
    )
    # search_fields = ('title',)

    inlines = [
        PriceInline
    ]


class PriceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'is_active')
    fields = ('title', 'is_active', 'url', 'category')


admin.site.register(CategoryBlock, CategoryBlockAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Price, PriceAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)


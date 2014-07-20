# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import CategoryBlock, Category, Product
from .forms import CategoryBlockAdminForm, CategoryAdminForm, ProductAdminForm
from django.contrib.auth.models import User, Group


class CategoryBlockAdmin(admin.ModelAdmin):
    form = CategoryBlockAdminForm
    list_display = ('title', 'form_type', 'move_list', 'is_active')

    def move_list(self, obj):
        move_list = obj.move_type.all()
        if len(move_list) == 2:
            return u'%s и %s' % (move_list[0], move_list[1])
        else:
            return u'%s' % move_list[0]
    move_list.short_description = u'Увеличение блока'


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = ('title',)


class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('title',)


admin.site.register(CategoryBlock, CategoryBlockAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)


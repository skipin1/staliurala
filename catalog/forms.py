# -*- coding: utf-8 -*-

from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import CategoryBlock, MoveType, Category, Product
from .validators import validate_move_types
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget


class AdminFileWidgetWithPreview(AdminFileWidget):

    def render(self, name, value, attrs=None):
        output = []
        if value and hasattr(value, "url"):
            output.append(('<p><img src="%s"/></p>' % value.url))

        output.append(super(AdminFileWidgetWithPreview, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class CategoryBlockAdminForm(ModelForm):
    move_type = ModelMultipleChoiceField(
        label=u'Увеличение блока',
        widget = CheckboxSelectMultiple,
        queryset=MoveType.objects.all(),
        validators=[validate_move_types],
    )

    class Meta:
        model = CategoryBlock
        widgets = {
            'image': AdminFileWidgetWithPreview(),
        }

    class Media:
        css = {
            'all': ('admin/admin.checkbox.inline.css',)
        }


class CategoryAdminForm(ModelForm):
    class Meta:
        model = Category
        widgets = {
            'image': AdminFileWidgetWithPreview(),
        }


class ProductAdminForm(ModelForm):
    class Meta:
        model = Product
        widgets = {
            'image': AdminFileWidgetWithPreview(),
        }


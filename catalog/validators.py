# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError


def validate_move_types(value):
    if '1' in value and '2' in value:
        raise ValidationError(u'Неверная комбинация')
    elif '3' in value and '4' in value:
        raise ValidationError(u'Неверная комбинация')
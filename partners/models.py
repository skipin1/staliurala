# -*- coding: utf-8 -*-

from django.db import models


class Partner(models.Model):
    title = models.CharField(u'Название', max_length=500)
    logo = models.ImageField(u'Логотип', upload_to='partner_logo')
    description = models.TextField(u'Описание')
    url = models.URLField(u'Ссылка на сайт')

    class Meta:
        verbose_name = u'Партнер'
        verbose_name_plural = u'Партнеры'
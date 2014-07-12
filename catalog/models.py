# -*- coding: utf-8 -*-

from django.db import models


class Category(models.Model):
    title = models.CharField(u'Название', max_length=500)
    parent = models.ForeignKey('self', verbose_name=u'Родительская категория', blank=True, null=True)
    image = models.ImageField(u'Изображение', upload_to='catalog/category/')
    description = models.TextField(u'Описание')

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Product(models.Model):
    title = models.CharField(u'Название', max_length=500)
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    image = models.ImageField(u'Изображение', upload_to='catalog/product/')
    description = models.TextField(u'Описание')

    class Meta:
        verbose_name = u'Продукт'
        verbose_name_plural = u'Продукты'

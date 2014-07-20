# -*- coding: utf-8 -*-

from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django.core.urlresolvers import reverse


class CommonFields(TimeStampedModel):
    title = models.CharField(u'Название', max_length=500)
    description = models.TextField(u'Описание', blank=True)
    is_active = models.BooleanField(u'Активный', default=True)

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        abstract = True


class MoveType(models.Model):
    DIRECTION_CHOICES = (
        ('double-to-left', u'Влево'),
        ('double-to-right', u'Вправо'),
        ('double-to-top', u'Вверх'),
        ('double-to-bottom', u'Вниз'),
    )
    type = models.CharField(max_length=16, choices=DIRECTION_CHOICES)

    def __unicode__(self):
        return u'%s' % filter(lambda x: x[0] == self.type, self.DIRECTION_CHOICES)[0][1]


class CategoryBlock(CommonFields):
    FORM_CHOICES = (
        ('simple', u'Обычный'),
        ('double-width', u'Двойная ширина'),
        ('double-height', u'Двойная высота'),
    )

    image = models.ImageField(u'Картинка', upload_to='catalog/blocks/')
    form_type = models.CharField(u'Форма блока', max_length=13, choices=FORM_CHOICES, default='simple')
    move_type = models.ManyToManyField(MoveType)

    class Meta():
        verbose_name = u'Блок'
        verbose_name_plural = u'Блоки'


class Category(CommonFields):
    block = models.ForeignKey(CategoryBlock, verbose_name=u'Блок', related_name='categories')
    image = models.ImageField(u'Картинка', upload_to='catalog/category/', blank=True)
    slug = AutoSlugField(populate_from='title')

    def get_absolute_url(self):
        return reverse('catalog:category', args=[self.slug])

    class Meta():
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class Price(CommonFields):
    category = models.ForeignKey(Category, related_name='prices')
    url = models.CharField('URL', max_length=500)

    class Meta():
        verbose_name = u'Прайс'
        verbose_name_plural = u'Прайсы'

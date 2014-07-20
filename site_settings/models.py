# -*- coding: utf-8 -*-

from django.db import models


class SiteSetting(models.Model):
    about_us = models.TextField(u'О компании', blank=True)
    address = models.CharField(u'Адресс', max_length=2000, blank=True)

    def __unicode__(self):
        return u'Настройки сайта'

    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'

class Phone(models.Model):
    number = models.CharField(max_length=30)
    site = models.ForeignKey(SiteSetting)

    class Meta:
        abstract = True


class HeaderPhone(Phone):
    pass


class ManagerPhone(Phone):
    pass


class LogisticPhone(Phone):
    pass
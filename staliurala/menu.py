# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from admin_tools.menu import items, Menu


class CustomMenu(Menu):
    """
    Custom Menu for staliurala admin site.
    """
    def __init__(self, **kwargs):
        Menu.__init__(self, **kwargs)
        self.children += [
            items.MenuItem(_('Dashboard'), reverse('admin:index')),
            items.MenuItem(_(u'Настройки'), '/admin/site_settings/',
                children=[
                    items.MenuItem(u'Настройки сайта', '/admin/site_settings/sitesetting/1/')
                ]
            ),
            items.MenuItem(_(u'Контент'),
                children=[
                    items.MenuItem(u'Партнеры', '/admin/partners/partner/'),
                    items.MenuItem(u'Блоки на главной', '/admin/catalog/categoryblock/'),
                    items.MenuItem(u'Категории', '/admin/catalog/category/'),
                    items.MenuItem(u'Прайсы', '/admin/catalog/price/'),
                ]
            ),

        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomMenu, self).init_with_context(context)

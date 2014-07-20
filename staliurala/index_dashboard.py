# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard
from admin_tools.utils import get_admin_site_name


class SettingsModule(modules.DashboardModule):
    # draggable = False
    # collapsible = False
    # deletable = False
    title = u'Раздел настроек'
    post_content = 'content'
    template = 'admin-tools/site-settings.html'


class ContentModule(modules.DashboardModule):
    # draggable = False
    # collapsible = False
    # deletable = False
    title = u'Контент сайта'
    post_content = 'content'
    template = 'admin-tools/site-content.html'

class CustomIndexDashboard(Dashboard):
    class Media:
        css = ('admin-tools/css/style.css',)

    columns = 1

    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        self.children.append(SettingsModule())
        self.children.append(ContentModule())
        self.children.append(modules.RecentActions(_('Recent Actions'), 10))
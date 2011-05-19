# -*- coding: utf-8 -*-
# * File Name : cms_plugins.py
#
# * Copyright (C) 2010 Gaston TJEBBES <tonthon21@gmail.com>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 19-05-2011
# * Last Modified : jeu. 19 mai 2011 16:24:10 CEST
#
# * Project : cmsplugin_wrappedtext
#
"""
    django cms declaration
"""
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from models import WrappedText
from cms.plugins.text.cms_plugins import TextPlugin
from cms.plugins.text.utils import plugin_tags_to_user_html
from django.conf import settings

class WrappedTextPlugin(TextPlugin):
    """
        Subclass of the text plugin just adding a surrounding div
        with a configurable css class
    """
    model = WrappedText
    name = _("WrappedText")
    render_template = "plugins/wrappedtext/wrappedtext.html"

    def render(self, context, instance, placeholder):
        if settings.CMS_DBGETTEXT:
            from dbgettext.parser import parsed_gettext
            instance.body = parsed_gettext(instance, 'body')
        context.update({
            'body': plugin_tags_to_user_html(instance.body, context, placeholder),
            'css' : instance.css,
            'placeholder': placeholder,
            'object': instance
        })
        return context

plugin_pool.register_plugin(WrappedTextPlugin)

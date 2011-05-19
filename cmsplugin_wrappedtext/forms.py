# -*- coding: utf-8 -*-
# * File Name : forms.py
#
# * Copyright (C) 2010 Gaston TJEBBES <tonthon21@gmail.com>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 19-05-2011
# * Last Modified : jeu. 19 mai 2011 16:24:40 CEST
#
# * Project : cmsplugin_wrappedtext
#
"""
    Extended form for the cmsplugin_wrappedtext plugin
"""
from django.forms.models import ModelForm
from cms.plugins.text.models import WrappedText
from django import forms


class WrappedTextForm(ModelForm):
    body = forms.CharField()

    class Meta:
        model = WrappedText
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')


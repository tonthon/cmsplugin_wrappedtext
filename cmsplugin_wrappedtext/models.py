# -*- coding: utf-8 -*-
# * File Name : models.py
#
# * Copyright (C) 2010 Gaston TJEBBES <tonthon21@gmail.com>
#   This software is distributed under GPLV3
#   License: http://www.gnu.org/licenses/gpl-3.0.txt
#
# * Creation Date : 19-05-2011
# * Last Modified : jeu. 19 mai 2011 16:24:21 CEST
#
# * Project : cmsplugin_wrappedtext
#
"""
    Our extended model
"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.plugins.text.models import AbstractText


class WrappedText(AbstractText):
    """ Subclass of the Text plugin model, adding the css attr """
    css = models.CharField(_('Wrapping css class'), max_length='150',help_text=_('Additional CSS class to apply'), blank=True)

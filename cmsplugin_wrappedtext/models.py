from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags
from django.utils.text import truncate_words
from django.conf import settings
from cms.models import CMSPlugin
from cms.plugins.text.models import AbstractText


class WrappedText(AbstractText):
    """ Subclass of the Text plugin model, adding the css attr """
    css = models.CharField(_('Wrapping css class'), max_length='150',help_text=_('Additional CSS class to apply'), blank=True)

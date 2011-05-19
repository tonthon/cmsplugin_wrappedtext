from django.forms.models import ModelForm
from cms.plugins.text.models import WrappedText
from django import forms


class WrappedTextForm(ModelForm):
    body = forms.CharField()

    class Meta:
        model = WrappedText
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')

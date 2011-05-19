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

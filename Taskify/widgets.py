from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class DropZoneFileField(Widget):
    template_name = 'my_widget.html'


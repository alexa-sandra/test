from django.conf import settings
from django.forms import ModelForm, Textarea
from testJobs42.personalinfo.models import Person
from django import forms

class DatePickerWidget(forms.DateInput):
    class Media:
        css = {
            'all': (settings.STATIC_URL+"css/ui-lightness/jquery-ui-1.10.3.custom.min.css",)
        }
        js = (
            settings.STATIC_URL+"js/jquery-ui-1.10.3.custom.min.js",
            settings.STATIC_URL+"js/jquery.ui.core.js",
            settings.STATIC_URL+"js/jquery.ui.widget.js",
            settings.STATIC_URL+"js/jquery.ui.datepicker.js",
        )

    def __init__(self, params='', attrs=None):
        self.params = params
        super(DatePickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(DatePickerWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            $('#id_%s').datepicker({%s});
            </script>'''%(name, self.params,))

class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'bio':Textarea({'cols':40, 'rows':10}),
            'other_contacts':Textarea({'cols':40, 'rows':10}),
            'birth_date':DatePickerWidget(params="dateFormat: 'dd.mm.yy', changeYear: true")
                }


    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

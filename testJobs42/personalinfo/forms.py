from django.forms import ModelForm, Textarea
from testJobs42.personalinfo.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        widgets = {
            'bio':Textarea({'cols':40, 'rows':10}),
            'other_contacts':Textarea({'cols':40, 'rows':10})
                }


    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)

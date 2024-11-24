from django import forms
from django.forms.models import inlineformset_factory
from courses.models import Course, Work


class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        widget=forms.HiddenInput
    )

    def __init__ (self, *args, **kwargs):
        super(CourseEnrollForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.all()

ModuleFormSet = inlineformset_factory(
    Course,
    Work,
    fields=['title'],
    extra=2,
    can_delete=True
)
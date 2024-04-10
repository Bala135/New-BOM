from django import forms
from .models import SiteInformation

class SiteInformationForm(forms.ModelForm):
    RING_NUMBER_CHOICES = [
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
    ]

    ring_number = forms.ChoiceField(label='Ring Number', choices=RING_NUMBER_CHOICES)
    class Meta:
        model = SiteInformation
        fields = '__all__'


class ResultsForm(forms.Form):
    # Define fields based on Results model
    pass

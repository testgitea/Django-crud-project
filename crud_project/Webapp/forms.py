from .models import company
from django import forms
class NewForm(forms.ModelForm):
    class meta:
        model=company
        fields=[
            'company_name',
            'company_logo',
             'company_city',
        ]
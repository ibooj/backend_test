from django import forms
from django.utils.translation import ugettext_lazy as _


class SmsForm(forms.Form):
    tel = forms.CharField(max_length=16, required=True, label=_('tel'), widget=forms.NumberInput)
    msg = forms.CharField(max_length=140, required=True, label=_('msg'), widget=forms.Textarea(attrs={'rows': 5}))

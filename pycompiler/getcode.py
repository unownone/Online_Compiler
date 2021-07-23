from django import forms
from django.forms.widgets import HiddenInput

class codeForm(forms.Form):
    code=forms.CharField(widget=forms.Textarea,label="Code")
    params=forms.CharField(widget=forms.Textarea,label="ENTER INPUT IF ANY",required=False)
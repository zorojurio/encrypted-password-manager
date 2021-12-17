from .models import MasterPassword
from django import forms

class MastersPasswordForm(forms.ModelForm):
    class Meta:
        model = MasterPassword
        fields = ['password']
    



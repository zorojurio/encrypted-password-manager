from .models import MasterPassword
from django import forms

class MastersPasswordForm(forms.ModelForm):
    class Meta:
        model = MasterPassword
        fields = ['password']
    
class CheckMasterPasswordForm(forms.Form):
    master = forms.CharField(widget=forms.PasswordInput)


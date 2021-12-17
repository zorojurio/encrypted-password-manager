from django import forms


from passwords.models import PlatformPassword


class MasterForm(forms.Form):
    master = forms.CharField(widget=forms.PasswordInput)


class PlatformPasswordForm(forms.ModelForm):
    class Meta:
        model = PlatformPassword
        fields = ('email', 'username', 'password', 'platform')

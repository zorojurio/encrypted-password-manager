from django import forms


from passwords.models import PlatformPassword


class PlatformPasswordForm(forms.ModelForm):
    class Meta:
        model = PlatformPassword
        fields = ('email', 'username', 'password', 'platform')

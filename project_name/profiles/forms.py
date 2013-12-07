from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from captcha.fields import CaptchaField

from .models import AppUser


class AppUserCreationForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': _("A user with that email already exists."),
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput)

    class Meta:
        model = AppUser
        fields = ('email', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(AppUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


class AppUserRegisterationForm(AppUserCreationForm):
    captcha = CaptchaField()


class AppUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(label=_("Password"))

    class Meta:
        model = AppUser

    def __init__(self, *args, **kwargs):
        super(AppUserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')

    def clean_password(self):
        return self.initial["password"]

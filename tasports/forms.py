from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordResetForm, UserCreationForm

from .models import CustomUser, Teams

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Enter Password')
    confirmpassword = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'confirmpassword']

    def clean_password(self):
        cleaneddata = super().clean()
        password = cleaneddata.get('password')
        confirmpassword = cleaneddata.get('confirmpassword')
        if password and confirmpassword and password != confirmpassword:
            raise forms.ValidationError("Your passwords do not match.")

        return password

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SelectTeamsForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['favouriteteams']
        widgets = {
            'favouriteteams': forms.CheckboxSelectMultiple(),
        }


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User
from .models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=12, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateProfileForm(forms.ModelForm):
    avatar = forms.ImageField(required=False)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    first_name = forms.CharField(required=False, max_length=20)
    email = forms.CharField(required=False, max_length=100)
    username = forms.CharField(required=False, max_length=20)
    last_name = forms.CharField(required=False, max_length=20)

    class Meta:
        model = Profile
        fields = ('avatar', 'phone',)


class EmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.get(email=email)
        if user is None:
            raise forms.ValidationError('юзер с таким эмейл не зарегистрирован')


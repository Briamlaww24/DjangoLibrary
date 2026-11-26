from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, min_length=3, required=True)
    first_name = forms.CharField(max_length=150, min_length=3, required=True)
    last_name = forms.CharField(max_length=150, min_length=3, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')

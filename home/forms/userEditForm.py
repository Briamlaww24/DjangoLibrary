from django import forms
from django.contrib.auth import get_user_model

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(max_length=150, min_length=3, required=True)
    last_name = forms.CharField(max_length=150, min_length=3, required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo electrónico',
        }
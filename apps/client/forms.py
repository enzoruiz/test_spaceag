from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password'
        )

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 6:
            raise forms.ValidationError(
                'La contraseña debe tener un minimo de 6 digitos!'
            )
        return make_password(password)

from django.forms import ModelForm
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.validationError("Cet utilisateur n'existe pas")
            if not user.check_password(password):
                raise forms.validationError('Mot de passe incorrect')
            if not user.is_active:
                raise forms.validationError('Cet utilisateur n est pas activé')
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =[
            'username',
            'email',
            'password',
            'password2'
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "Cet adresse mail existe deja"
            )
        return email

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Vous devez confirmer votre mot de passe")
        if password != password2:
            raise forms.ValidationError("Vos mots de passe ne correspondent pas!")
        return password2
"""
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Les adresse mail doivent correspondent")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.validationError(
                "Cet adresse mail existe deja"
            )
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas!")
        return password1


class  CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
"""

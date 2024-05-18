from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class ClienteLoginForm(AuthenticationForm):
    class Meta:
        model = Cliente
        fields = ['username', 'password']


class ClienteCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), required=False)
    distrito = forms.ModelChoiceField(queryset=Distrito.objects.all(), required=False)

    class Meta(UserCreationForm.Meta):
        model = Cliente
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'pais', 'region', 'ciudad', 'distrito')


class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email', 'pais', 'region', 'ciudad', 'distrito']


class PerfilEmbarazoRegistroForm(forms.ModelForm):
    class Meta:
        model = PerfilEmbarazo
        fields = ['num_semana_embarazo']


class PerfilEmbarazoEdicionForm(forms.ModelForm):
    class Meta:
        model = PerfilEmbarazo
        fields = ['num_semana_embarazo', 'fecha_ultima_menstruacion', 'edad', 'sintomas']
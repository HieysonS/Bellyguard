from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import Cliente, PerfilEmbarazo, HistorialMedico, PASistolicammHg, Etnias, PADiastolicammHg, ProteinaOrina, \
    Pais, Region, Ciudad, Distrito, AntecedentesFamiliares, EstiloVida, NivelesActividadFisica


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
    email = forms.EmailField(required=False)
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(), required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
    ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), required=False)
    distrito = forms.ModelChoiceField(queryset=Distrito.objects.all(), required=False)

    class Meta:
        model = Cliente
        fields = ['first_name', 'last_name', 'email', 'pais', 'region', 'ciudad', 'distrito']

    def __init__(self, *args, **kwargs):
        super(ClienteProfileForm, self).__init__(*args, **kwargs)
        self.fields['pais'].queryset = Pais.objects.all()
        self.fields['pais'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['region'].queryset = Region.objects.all()
        self.fields['region'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['ciudad'].queryset = Ciudad.objects.all()
        self.fields['ciudad'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['distrito'].queryset = Distrito.objects.all()
        self.fields['distrito'].label_from_instance = lambda obj: "%s" % obj.nombre


class PerfilEmbarazoRegistroForm(forms.ModelForm):
    class Meta:
        model = PerfilEmbarazo
        fields = ['edad_gestacional']

    edad_gestacional = forms.IntegerField(label='edad_gestacional', min_value=3, max_value=38)


class PerfilEmbarazoEdicionForm(forms.ModelForm):
    class Meta:
        model = PerfilEmbarazo
        fields = ['edad', 'edad_gestacional', 'last_mestruacion', 'num_fetos', 'peso_kg', 'altura_cm',
                  'ganancia_peso_kg', 'etnia', 'pa_sistolica_mmhg', 'pa_diastolica_mmhg', 'proteina_orina']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['etnia'].queryset = Etnias.objects.all()
        self.fields['etnia'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['pa_sistolica_mmhg'].queryset = PASistolicammHg.objects.all()
        self.fields['pa_sistolica_mmhg'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['pa_diastolica_mmhg'].queryset = PADiastolicammHg.objects.all()
        self.fields['pa_diastolica_mmhg'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['proteina_orina'].queryset = ProteinaOrina.objects.all()
        self.fields['proteina_orina'].label_from_instance = lambda obj: "%s" % obj.nombre


class PEmbaForm(ModelForm):
    class Meta:
        model = PerfilEmbarazo
        fields = '__all__'


class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['hipertension_previa', 'hist_preeclampsia', 'diabetes', 'enfermed_renal']


class AntecedentesFamiliaresForm(forms.ModelForm):
    class Meta:
        model = AntecedentesFamiliares
        fields = ['preclampsia_familiar', 'hist_enferm_cardiovasculares_fam']


class EstiloVidaForm(forms.ModelForm):
    class Meta:
        model = EstiloVida
        fields = ['nivel_activ_fisica', 'dieta', 'consumo_tabaco', 'consumo_alcohol']

    def __init__(self, *args, **kwargs):
        super(EstiloVidaForm, self).__init__(*args, **kwargs)
        self.fields['nivel_activ_fisica'].queryset = NivelesActividadFisica.objects.all()
        self.fields['nivel_activ_fisica'].label_from_instance = lambda obj: "%s" % obj.nombre

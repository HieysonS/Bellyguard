from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import Cliente, PerfilEmbarazo, HistorialMedico, PASistolicammHg, Etnias, PADiastolicammHg, ProteinaOrina, \
    Pais, Region, Ciudad, Distrito, AntecedentesFamiliares, EstiloVida, NivelesActividadFisica, Sintomas


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

    edad_gestacional = forms.IntegerField(label='edad_gestacional', min_value=1, max_value=38)


class PerfilEmbarazoEdicionForm(forms.ModelForm):
    class Meta:
        model = PerfilEmbarazo
        fields = ['edad', 'edad_gestacional', 'last_mestruacion', 'num_fetos', 'peso_kg', 'altura_cm',
                  'ganancia_peso_kg', 'etnia', 'pa_sistolica_mmhg', 'pa_diastolica_mmhg', 'proteina_orina']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['edad'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200',
            'placeholder': 'Edad',
            'min': '16',
            'max': '60'
        })
        self.fields['edad_gestacional'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200',
            'placeholder': 'Edad',
            'min': '1',
            'max': '40'
        })
        self.fields['last_mestruacion'].widget = forms.DateInput(format='%Y-%m-%d', attrs={
            'type': 'date',
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200'
        })
        self.fields['num_fetos'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200',
            'placeholder': '# Fetos',
            'min': '1',
            'max': '5'
        })
        self.fields['peso_kg'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200',
            'placeholder': 'Kg',
            'min': '40',
            'max': '150'
        })
        self.fields['altura_cm'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200',
            'placeholder': 'CM',
            'min': '120',
            'max': '210'
        })
        self.fields['ganancia_peso_kg'].widget.attrs.update({
            'class': 'w-full px-3 py-2 border border-zinc-300 dark:border-zinc-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 dark:bg-zinc-800 dark:text-zinc-200',
            'placeholder': 'Peso Ganado (Kg)',
            'min': '1',
            'max': '50'
        })
        self.fields['etnia'].queryset = Etnias.objects.all()
        self.fields['etnia'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['pa_sistolica_mmhg'].queryset = PASistolicammHg.objects.all()
        self.fields['pa_sistolica_mmhg'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['pa_diastolica_mmhg'].queryset = PADiastolicammHg.objects.all()
        self.fields['pa_diastolica_mmhg'].label_from_instance = lambda obj: "%s" % obj.nombre
        self.fields['proteina_orina'].queryset = ProteinaOrina.objects.all()
        self.fields['proteina_orina'].label_from_instance = lambda obj: "%s" % obj.nombre


class HistorialMedicoForm(forms.ModelForm):
    HIPERTENSION_CHOICES = [(True, 'Sí'), (False, 'No')]
    hipertension_previa = forms.ChoiceField(choices=HIPERTENSION_CHOICES, widget=forms.RadioSelect)
    hist_preeclampsia = forms.ChoiceField(choices=HIPERTENSION_CHOICES, widget=forms.RadioSelect)
    diabetes = forms.ChoiceField(choices=HIPERTENSION_CHOICES, widget=forms.RadioSelect)
    enfermed_renal = forms.ChoiceField(choices=HIPERTENSION_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = HistorialMedico
        fields = ['hipertension_previa', 'hist_preeclampsia', 'diabetes', 'enfermed_renal']


class AntecedentesFamiliaresForm(forms.ModelForm):
    AMF_CHOICES = [(True, 'Sí'), (False, 'No')]
    preclampsia_familiar = forms.ChoiceField(choices=AMF_CHOICES, widget=forms.RadioSelect)
    hist_enferm_cardiovasculares_fam = forms.ChoiceField(choices=AMF_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = AntecedentesFamiliares
        fields = ['preclampsia_familiar', 'hist_enferm_cardiovasculares_fam']


class EstiloVidaForm(forms.ModelForm):
    EVF_CHOICES = [(True, 'Sí'), (False, 'No')]
    dieta = forms.ChoiceField(choices=EVF_CHOICES, widget=forms.RadioSelect)
    consumo_tabaco = forms.ChoiceField(choices=EVF_CHOICES, widget=forms.RadioSelect)
    consumo_alcohol = forms.ChoiceField(choices=EVF_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = EstiloVida
        fields = ['nivel_activ_fisica', 'dieta', 'consumo_tabaco', 'consumo_alcohol']

    def __init__(self, *args, **kwargs):
        super(EstiloVidaForm, self).__init__(*args, **kwargs)
        self.fields['nivel_activ_fisica'].queryset = NivelesActividadFisica.objects.all()
        self.fields['nivel_activ_fisica'].label_from_instance = lambda obj: "%s" % obj.nombre


class SintomasForm(forms.ModelForm):
    S_CHOICES = [(True, 'Sí'), (False, 'No')]
    contraccion = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    cuello_uterino_dilatado = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    perdida_liquido_amniotico = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    sangrado_vaginal = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    infeccion_vaginal = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    malformacion_uterina = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    anemia = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)
    parto_prematuro_anterior = forms.ChoiceField(choices=S_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Sintomas
        fields = ['contraccion', 'cuello_uterino_dilatado', 'perdida_liquido_amniotico',
                  'sangrado_vaginal', 'infeccion_vaginal', 'malformacion_uterina', 'anemia',
                  'parto_prematuro_anterior']

from datetime import datetime, date

import joblib
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ClienteCreationForm, ClienteLoginForm, ClienteProfileForm, \
    PerfilEmbarazoRegistroForm, PerfilEmbarazoEdicionForm, HistorialMedicoForm, AntecedentesFamiliaresForm, \
    EstiloVidaForm, SintomasForm
from webapp.models import Cliente, PerfilEmbarazo, InfoEmbarazo, HistorialMedico, AntecedentesFamiliares, EstiloVida, \
    Sintomas


# Create your views here.
def inicio(request):
    if request.user.is_authenticated:
        return redirect('bienvenido')
    else:
        return render(request, 'PortadasWeb/inicio.html')


def mas_informacion(request):
    return render(request, 'PortadasWeb/mas_informacion.html')


def contacto(request):
    return render(request, 'PortadasWeb/contacto.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        form = ClienteLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('bienvenido')
    else:
        form = ClienteLoginForm()
    return render(request, 'Login/iniciar_sesion.html', {'form': form})


def registrarse(request):
    if request.method == 'POST':
        form = ClienteCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('bienvenido_nuevo')
    else:
        form = ClienteCreationForm()
    return render(request, 'Login/registrarse.html', {'form': form})


@login_required
def bienvenido(request):
    return render(request, 'Contenidos/bienvenido.html')


@login_required
def bienvenido_nuevo(request):
    return render(request, 'Contenidos/bienvenido_nuevo.html')


def herramientas(request):
    pass


@login_required
def perfil(request):
    cliente = Cliente.objects.get(username=request.user.username)
    return render(request, 'Perfiles/perfil.html', {'cliente': cliente})


@login_required
def editar_perfil(request):
    try:
        edit_perfil = HistorialMedico.objects.get(cliente=request.user)
    except HistorialMedico.DoesNotExist:
        edit_perfil = HistorialMedico(cliente=request.user)
    if request.method == 'POST':
        form = ClienteProfileForm(request.POST, instance=edit_perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ClienteProfileForm(instance=edit_perfil)
    return render(request, 'Perfiles/editar_perfil.html', {'form': form})


@login_required
def registro_semanas(request):
    if request.method == 'POST':
        form = PerfilEmbarazoRegistroForm(request.POST)
        if form.is_valid():
            perfil_embarazo = form.save(commit=False)
            perfil_embarazo.cliente = request.user
            perfil_embarazo.save()
            return redirect('bienvenido')
    else:
        form = PerfilEmbarazoRegistroForm()
    return render(request, 'Contenidos/registro_semanas.html', {'form': form})


@login_required
def editar_perfil_embarazo(request):
    try:
        perfil_embarazo = get_object_or_404(PerfilEmbarazo, cliente=request.user)
    except HistorialMedico.DoesNotExist:
        perfil_embarazo = PerfilEmbarazo(cliente=request.user)
    if request.method == 'POST':
        form = PerfilEmbarazoEdicionForm(request.POST, instance=perfil_embarazo)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = PerfilEmbarazoEdicionForm(instance=perfil_embarazo)
    return render(request, 'Contenidos/editar_perfil_embarazo.html', {'form': form})


@login_required
def registro_historial_medico(request):
    try:
        historial_medico = HistorialMedico.objects.get(cliente=request.user)
    except HistorialMedico.DoesNotExist:
        historial_medico = HistorialMedico(cliente=request.user)
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST, instance=historial_medico)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = HistorialMedicoForm(instance=historial_medico)
    return render(request, 'Contenidos/historial_medico_form.html', {'form': form})


@login_required
def registro_antecedentes_familiares(request):
    try:
        antecedentes_familiares = AntecedentesFamiliares.objects.get(cliente=request.user)
    except AntecedentesFamiliares.DoesNotExist:
        antecedentes_familiares = AntecedentesFamiliares(cliente=request.user)
    if request.method == 'POST':
        form = AntecedentesFamiliaresForm(request.POST, instance=antecedentes_familiares)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = AntecedentesFamiliaresForm(instance=antecedentes_familiares)
    return render(request, 'Contenidos/registro_antecedentes_familiares.html', {'form': form})


@login_required
def registro_estilo_vida(request):
    try:
        estilo_vida = EstiloVida.objects.get(cliente=request.user)
    except EstiloVida.DoesNotExist:
        estilo_vida = EstiloVida(cliente=request.user)
    if request.method == 'POST':
        form = EstiloVidaForm(request.POST, instance=estilo_vida)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = EstiloVidaForm(instance=estilo_vida)
    return render(request, 'Contenidos/registro_estilo_vida.html', {'form': form})


@login_required
def registro_sintomas(request):
    try:
        sintomas = Sintomas.objects.get(cliente=request.user)
    except Sintomas.DoesNotExist:
        sintomas = Sintomas(cliente=request.user)
    if request.method == 'POST':
        form = SintomasForm(request.POST, instance=sintomas)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = SintomasForm(instance=sintomas)
    return render(request, 'Contenidos/registro_sintomas.html', {'form': form})


@login_required
def predecir_preeclampsia(request):
    modeloPreeclampsia = joblib.load('modelosML/modeloPreeclampsia.pkl')
    perfil_embarazo = get_object_or_404(PerfilEmbarazo, cliente=request.user)
    historial_medico = get_object_or_404(HistorialMedico, cliente=request.user)
    antecedentes_familiares = get_object_or_404(AntecedentesFamiliares, cliente=request.user)
    estilo_vida = get_object_or_404(EstiloVida, cliente=request.user)

    datos_completos = pd.DataFrame({'HipertensiónPrevia': [int(historial_medico.hipertension_previa)],
                                    'HistPreeclampsia': [int(historial_medico.hist_preeclampsia)],
                                    'Diabetes': [int(historial_medico.diabetes)],
                                    'EnfermedRenal': [int(historial_medico.enfermed_renal)],
                                    'Edad': [perfil_embarazo.edad],
                                    'PesoKg': [perfil_embarazo.peso_kg],
                                    'AlturaCM': [perfil_embarazo.altura_cm],
                                    'Etnia': [perfil_embarazo.etnia.id],
                                    'PreclaampsiaFamiliar': [int(antecedentes_familiares.preclampsia_familiar)],
                                    'HistEnfermCardiovascularesFam': [int(antecedentes_familiares.hist_enferm_cardiovasculares_fam)],
                                    'PASistolicammHg': [perfil_embarazo.pa_sistolica_mmhg.id],
                                    'PADiastolicammHg': [perfil_embarazo.pa_diastolica_mmhg.id],
                                    'ProteinaOrina': [perfil_embarazo.proteina_orina.id],
                                    'GananciaPesoKg': [perfil_embarazo.ganancia_peso_kg],
                                    'EdadGestacional': [perfil_embarazo.edad_gestacional],
                                    'NumFetos': [perfil_embarazo.num_fetos],
                                    'NivelActivFisica': [estilo_vida.nivel_activ_fisica.id],
                                    'Dieta': [int(estilo_vida.dieta)],
                                    'ConsumoTabaco': [int(estilo_vida.consumo_tabaco)],
                                    'ConsumoAlcohol': [int(estilo_vida.consumo_alcohol)]})

    probabilidad = modeloPreeclampsia.predict_proba(datos_completos)
    probabilidad_preeclampsia = probabilidad[:, 1]
    porcentaje_preeclampsia = probabilidad_preeclampsia * 100
    porcentaje_formateado = "{:.2f}".format(porcentaje_preeclampsia[0])

    return render(request, 'Contenidos/predecir_preeclampsia.html',
                  {'porcentaje_formateado': porcentaje_formateado})


@login_required
def predecir_fecha_parto(request):
    modeloPartoFecha = joblib.load('modelosML/modeloPartoFecha.pkl')
    perfil_embarazo = get_object_or_404(PerfilEmbarazo, cliente=request.user)
    last_mestruacion = pd.to_datetime(perfil_embarazo.last_mestruacion, format='%d/%m/%Y').toordinal()
    fechaPredicha = modeloPartoFecha.predict([[last_mestruacion]])
    fechaParto = datetime.fromordinal(int(fechaPredicha[0]))
    fecha_parto_formateada = fechaParto.strftime('%Y-%m-%d')
    return render(request, 'Contenidos/predecir_fecha_parto.html',
                  {'fecha_parto': fecha_parto_formateada})


@login_required
def predecir_parto_prematuro(request):
    modeloPartoPrematuro = joblib.load('modelosML/modeloPartoPrematuro.pkl')
    sintomas = get_object_or_404(Sintomas, cliente=request.user)
    historial_medico = get_object_or_404(HistorialMedico, cliente=request.user)
    datoApredecir = pd.DataFrame({'Contracciones': [int(sintomas.contraccion)],
                                  'DilatacionCuelloUterino': [int(sintomas.cuello_uterino_dilatado)],
                                  'PerdidaLiquidoAmniotico': [int(sintomas.perdida_liquido_amniotico)],
                                  'SangradoVaginal': [int(sintomas.sangrado_vaginal)],
                                  'Infeccion': [int(sintomas.infeccion_vaginal)],
                                  'EnfermedadRenal': [int(historial_medico.enfermed_renal)],
                                  'Anemia': [int(sintomas.anemia)],
                                  'MalformacionUterina': [int(sintomas.malformacion_uterina)],
                                  'PartoPrematuroAnterior': [int(sintomas.parto_prematuro_anterior)]})
    res = modeloPartoPrematuro.predict(datoApredecir)
    if res == [1]:
        result = "Prematuridad extrema: Nacimiento prematuro antes de la semana 28"
    elif res == [2]:
        result = "Parto prematuro severo: Entre la semana 28 y 31 de gestación"
    elif res == [3]:
        result = "Prematuridad moderada: Parto entre las semanas 32 y 33"
    elif res == [4]:
        result = "Parto prematuro límite o leve: A partir de la semana 34 a la 36"
    else:
        result = "No hay riesgo de parto prematuro"

    return render(request, 'Contenidos/predecir_parto_prematuro.html',
                  {'result': result})


@login_required
def info_embarazo(request):
    lista_info_embarazo = InfoEmbarazo.objects.all().order_by('semana')
    paginator = Paginator(lista_info_embarazo, 1)  # Muestra 1 semanas por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'Contenidos/info_embarazo.html', {'info_embarazo_list': page_obj})


@login_required
def notificaciones(request):
    return render(request, 'Contenidos/notificaciones.html')


def salir(request):
    logout(request)
    return redirect('inicio')

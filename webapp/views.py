from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from webapp.forms import ClienteCreationForm, ClienteLoginForm, ClienteProfileForm,\
    PerfilEmbarazoRegistroForm, PerfilEmbarazoEdicionForm
from webapp.models import Cliente, PerfilEmbarazo, InfoEmbarazo


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def mas_informacion(request):
    return render(request, 'mas_informacion.html')


def contacto(request):
    return render(request, 'contacto.html')


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
    return render(request, 'iniciar_sesion.html', {'form': form})


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
    return render(request, 'registrarse.html', {'form': form})


def bienvenido(request):
    return render(request, 'bienvenido.html')


def bienvenido_nuevo(request):
    return render(request, 'bienvenido_nuevo.html')


def herramientas(request):
    pass


def perfil(request):
    cliente = Cliente.objects.get(username=request.user.username)
    return render(request, 'perfil.html', {'cliente': cliente})


def editar_perfil(request):
    if request.method == 'POST':
        form = ClienteProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ClienteProfileForm(instance=request.user)
    return render(request, 'editar_perfil.html', {'form': form})


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
    return render(request, 'registro_semanas.html', {'form': form})


def editar_perfil_embarazo(request):
    perfil_embarazo = get_object_or_404(PerfilEmbarazo, cliente=request.user)
    if request.method == 'POST':
        form = PerfilEmbarazoEdicionForm(request.POST, instance=perfil_embarazo)
        if form.is_valid():
            form.save()
            return redirect('bienvenido')
    else:
        form = PerfilEmbarazoEdicionForm(instance=perfil_embarazo)
    return render(request, 'editar_perfil_embarazo.html', {'form': form})


def info_embarazo(request):
    lista_info_embarazo = InfoEmbarazo.objects.all().order_by('semana')
    paginator = Paginator(lista_info_embarazo, 1)  # Muestra 1 semanas por página

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'info_embarazo.html', {'info_embarazo_list': page_obj})


def notificaciones(request):
    return render(request, 'notificaciones.html')


def salir(request):
    logout(request)
    return redirect('inicio')
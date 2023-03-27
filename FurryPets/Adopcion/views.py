from django.shortcuts import render
from .models import Mascotas
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

from .forms import MascotasForm

def registrar(request):
    if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username= form.cleaned_data['username']
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, "registroU.html", context )

def acceder(request):
    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def Pubmascotas(request):
    mascota_form = MascotasForm()
    template_name="Publicar_mascotas.html"
    if request.method == "POST":
        form = MascotasForm(request.POST, request.FILES)
        if form.is_valid():
            nom= form.cleaned_data.get("nombre")
            tpm= form.cleaned_data.get("tipo_mascota")
            pic = form.cleaned_data.get("foto")
            due=form.cleaned_data.get("dueño")
            ciu= form.cleaned_data.get("ciudad")
            descrip= form.cleaned_data.get("descripcion")
            obj=Mascotas.objects.create(
                nombre=nom,
                tipo_mascota=tpm,
                foto=pic,
                dueño=due,
                ciudad=ciu,
                descripcion=descrip,
            )
            obj.save()
    else:
        form = MascotasForm()
    context = { 'form' : form}
    return render(request,'Publicar_mascotas.html', {"form": mascota_form})


def Padopcion(request):
    template_name = "PageAdopcion.html"
    return render(request, template_name)

# Create your views here.
def index(request):
    template_name = "index.html"
    mascotas=Mascotas.objects.all() #Select * from mascotas
    context = {'mascotas': mascotas}

    return render(request, template_name, context)

def InicioS(request):
    template_name = "IniciarSesion.html"
    return render(request, template_name)

def dudas(request):
    template_name = "dudas.html"
    return render(request, template_name)


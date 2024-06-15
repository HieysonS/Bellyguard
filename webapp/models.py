from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Pais(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Region(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Distrito(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Cliente(AbstractUser):
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
    distrito = models.ForeignKey(Distrito, on_delete=models.SET_NULL, null=True)


class Etnias(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class PASistolicammHg(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class PADiastolicammHg(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class ProteinaOrina(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class PerfilEmbarazo(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField(null=True)
    edad_gestacional = models.PositiveIntegerField()
    last_mestruacion = models.DateField(null=True)
    num_fetos = models.PositiveIntegerField(null=True)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    altura_cm = models.PositiveIntegerField(null=True)
    ganancia_peso_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    etnia = models.ForeignKey(Etnias, on_delete=models.SET_NULL, null=True)
    pa_sistolica_mmhg = models.ForeignKey(PASistolicammHg, on_delete=models.SET_NULL, null=True)
    pa_diastolica_mmhg = models.ForeignKey(PADiastolicammHg, on_delete=models.SET_NULL, null=True)
    proteina_orina = models.ForeignKey(ProteinaOrina, on_delete=models.SET_NULL, null=True)


class HistorialMedico(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    hipertension_previa = models.BooleanField(default=False)
    hist_preeclampsia = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    enfermed_renal = models.BooleanField(default=False)


class AntecedentesFamiliares(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    preclampsia_familiar = models.BooleanField(default=False)
    hist_enferm_cardiovasculares_fam = models.BooleanField(default=False)


class NivelesActividadFisica(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class EstiloVida(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    nivel_activ_fisica = models.ForeignKey(NivelesActividadFisica, on_delete=models.SET_NULL, null=True)
    dieta = models.BooleanField(default=False)
    consumo_tabaco = models.BooleanField(default=False)
    consumo_alcohol = models.BooleanField(default=False)


class Sintomas(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    contraccion = models.BooleanField(default=False)
    cuello_uterino_dilatado = models.BooleanField(default=False)
    perdida_liquido_amniotico = models.BooleanField(default=False)
    sangrado_vaginal = models.BooleanField(default=False)
    infeccion_vaginal = models.BooleanField(default=False)
    malformacion_uterina = models.BooleanField(default=False)
    anemia = models.BooleanField(default=False)
    parto_prematuro_anterior = models.BooleanField(default=False)


class InfoEmbarazo(models.Model):
    semana = models.IntegerField(verbose_name='Número de Semana')
    imagen = models.ImageField(verbose_name=_('Imagen'), upload_to='infoembarazo/', null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return f'Semana {self.semana}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()


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


class Sintoma(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class PerfilEmbarazo(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    num_semana_embarazo = models.IntegerField()
    fecha_ultima_menstruacion = models.DateField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    sintomas = models.ManyToManyField(Sintoma, blank=True)


class Enfermedad(models.Model):
    nombre = models.CharField(max_length=200)


class Medicamento(models.Model):
    nombre = models.CharField(max_length=200)


class Intervencion(models.Model):
    nombre = models.CharField(max_length=200)


class HistoriaClinica(models.Model):
    embarazos_previos = models.IntegerField()
    imc = models.FloatField()
    enfermedades = models.ManyToManyField(Enfermedad)
    medicamentos = models.ManyToManyField(Medicamento)
    intervenciones = models.ManyToManyField(Intervencion)


class HistoriaFamPreeclampsia(models.Model):
    parentesco = models.CharField(max_length=200)
    preeclampsia = models.BooleanField()
    fecha = models.DateField()


class DatosProteomicas(models.Model):
    nombre = models.CharField(max_length=200)
    nivel = models.FloatField()


class DatosMedicos(models.Model):
    perfil_embarazo = models.ForeignKey(PerfilEmbarazo, on_delete=models.CASCADE)
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    historia_fam_preeclampsia = models.ForeignKey(HistoriaFamPreeclampsia, on_delete=models.CASCADE)
    peso = models.FloatField()
    presion_arterial = models.CharField(max_length=50)
    datos_proteomicas = models.ManyToManyField(DatosProteomicas)


class PrediccionPreeclampsia(models.Model):
    datos_medicos = models.ForeignKey(DatosMedicos, on_delete=models.CASCADE)
    fecha_prediccion = models.DateField()
    riesgo = models.FloatField()


class InfoEmbarazo(models.Model):
    semana = models.IntegerField(verbose_name='Número de Semana')
    imagen = models.ImageField(verbose_name=_('Imagen'), upload_to='infoembarazo/', null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción')

    def __str__(self):
        return f'Semana {self.semana}'

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
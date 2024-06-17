# Generated by Django 5.0.4 on 2024-06-13 01:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_descripcion_nivelesactividadfisica_nombre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='hist_enferm_cardiovasculares_fam',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='antecedentesfamiliares',
            name='preclampsia_familiar',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estilovida',
            name='consumo_alcohol',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estilovida',
            name='consumo_tabaco',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='estilovida',
            name='dieta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historialmedico',
            name='diabetes',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historialmedico',
            name='enfermed_renal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historialmedico',
            name='hipertension_previa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='historialmedico',
            name='hist_preeclampsia',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Sintomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contraccion', models.BooleanField(default=False)),
                ('cuello_uterino_dilatado', models.BooleanField(default=False)),
                ('perdida_liquido_amniotico', models.BooleanField(default=False)),
                ('sangrado_vaginal', models.BooleanField(default=False)),
                ('infeccion_vaginal', models.BooleanField(default=False)),
                ('malformacion_uterina', models.BooleanField(default=False)),
                ('anemia', models.BooleanField(default=False)),
                ('parto_prematuro_anterior', models.BooleanField(default=False)),
                ('cliente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-22 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adopcion', '0002_alter_mascotas_ciudad_alter_mascotas_tipo_mascota'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dueño',
            fields=[
                ('codigo', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=12)),
                ('correo', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='ciudad',
            field=models.CharField(max_length=200),
        ),
        migrations.AddField(
            model_name='mascotas',
            name='dueño',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Adopcion.dueño'),
        ),
    ]

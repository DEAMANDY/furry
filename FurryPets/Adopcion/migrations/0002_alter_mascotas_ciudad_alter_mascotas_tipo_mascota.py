# Generated by Django 4.1.7 on 2023-03-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adopcion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotas',
            name='ciudad',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mascotas',
            name='tipo_mascota',
            field=models.CharField(max_length=100),
        ),
    ]

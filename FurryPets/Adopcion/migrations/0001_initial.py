# Generated by Django 4.1.7 on 2023-03-22 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='mascotas')),
                ('tipo_mascota', models.TextField()),
                ('ciudad', models.TextField()),
                ('descripcion', models.TextField()),
            ],
        ),
    ]

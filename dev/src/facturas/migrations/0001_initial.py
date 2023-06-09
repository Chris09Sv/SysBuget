# Generated by Django 4.2.2 on 2023-06-08 01:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('no_factura', models.IntegerField(unique=True)),
                ('ncf', models.IntegerField(unique=True)),
                ('rnc', models.CharField(max_length=15)),
                ('cliente', models.CharField(max_length=100)),
                ('combustible', models.DecimalField(decimal_places=2, max_digits=10)),
                ('distancia', models.DecimalField(decimal_places=2, max_digits=10)),
                ('desde', models.CharField(max_length=120)),
                ('hasta', models.CharField(max_length=120)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
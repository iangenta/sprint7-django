# Generated by Django 4.0.5 on 2022-08-11 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(default='usuario', max_length=12)),
                ('email', models.EmailField(default='email', max_length=50)),
                ('passw', models.CharField(default='password', max_length=16)),
                ('dni', models.IntegerField(default='dni')),
                ('cliente_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
        ),
    ]

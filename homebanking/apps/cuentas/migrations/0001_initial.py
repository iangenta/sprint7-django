# Generated by Django 4.1 on 2022-08-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('cuenta_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cliente_id', models.IntegerField(max_length=50)),
                ('balance', models.IntegerField()),
                ('tipo_cuenta', models.CharField(max_length=50)),
            ],
        ),
    ]

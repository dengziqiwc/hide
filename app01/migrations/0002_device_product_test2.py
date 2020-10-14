# Generated by Django 3.1.2 on 2020-10-14 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=32, unique=True)),
                ('productkey', models.CharField(max_length=32, unique=True)),
                ('productsecret', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Test2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=32)),
                ('event_time', models.IntegerField()),
                ('event_date', models.DateField()),
                ('CurrentTemperature', models.FloatField()),
                ('CurrentHumidity', models.FloatField()),
                ('product_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.product', to_field='productkey')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('devicename', models.CharField(max_length=32)),
                ('devicesecret', models.CharField(max_length=32)),
                ('productname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.product', to_field='productname')),
            ],
        ),
    ]
# Generated by Django 3.1.2 on 2020-10-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_device_product_test2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test2',
            name='event_date',
            field=models.DateTimeField(),
        ),
    ]

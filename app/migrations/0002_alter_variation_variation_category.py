# Generated by Django 3.2.8 on 2022-06-10 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('colors', 'colors'), ('sizes', 'sizes')], max_length=100),
        ),
    ]

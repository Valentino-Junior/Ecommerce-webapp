# Generated by Django 3.2.8 on 2022-06-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_cart_id_cart_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]

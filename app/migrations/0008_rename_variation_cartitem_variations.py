# Generated by Django 3.2.9 on 2022-03-24 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_cartitem_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='variation',
            new_name='variations',
        ),
    ]

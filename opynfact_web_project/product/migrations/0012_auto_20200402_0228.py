# Generated by Django 3.0.4 on 2020-04-02 00:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20200402_0227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zproduct',
            old_name='brand',
            new_name='brands',
        ),
    ]
# Generated by Django 3.0.4 on 2020-04-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20200402_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='zsearch',
            name='alternatives',
            field=models.ManyToManyField(blank=True, related_name='zsearches', to='product.ZFavorite'),
        ),
    ]
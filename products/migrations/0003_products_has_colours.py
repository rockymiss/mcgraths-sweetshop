# Generated by Django 3.2 on 2022-12-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20221205_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='has_colours',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

# Generated by Django 2.2.5 on 2022-06-11 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20220607_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bedrooms',
            field=models.IntegerField(default=1),
        ),
    ]
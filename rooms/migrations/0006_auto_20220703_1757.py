# Generated by Django 2.2.5 on 2022-07-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20220617_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='house_rule',
            new_name='house_rules',
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]

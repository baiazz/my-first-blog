# Generated by Django 2.2.3 on 2019-07-12 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pet_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='age',
            new_name='idade',
        ),
    ]

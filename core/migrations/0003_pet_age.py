# Generated by Django 2.2.3 on 2019-07-12 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190712_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190712_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='age',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
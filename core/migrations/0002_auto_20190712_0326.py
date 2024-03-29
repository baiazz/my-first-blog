# Generated by Django 2.2.3 on 2019-07-12 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pet',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='phone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pet'),
        ),
        migrations.AlterModelTable(
            name='pet',
            table='pet_lost',
        ),
    ]

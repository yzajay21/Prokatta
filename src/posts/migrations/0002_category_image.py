# Generated by Django 2.1.2 on 2018-10-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='upload_location', width_field='width_field'),
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-21 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_posts_short_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload_location'),
        ),
    ]

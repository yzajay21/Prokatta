# Generated by Django 2.1.2 on 2018-10-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_posts_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='short_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
# Generated by Django 2.2.6 on 2019-10-03 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='photo',
            field=models.ImageField(null=True, upload_to='gallery'),
        ),
    ]

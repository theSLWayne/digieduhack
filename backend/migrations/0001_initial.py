# Generated by Django 2.2.6 on 2019-10-03 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter ingredient name.', max_length=100)),
                ('manufacturer', models.CharField(help_text='Enter manufacturer.', max_length=100)),
                ('price', models.FloatField(help_text='Enter price.')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter user name.', max_length=100)),
                ('email', models.EmailField(help_text='Enter email.', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter title', max_length=100)),
                ('description', models.TextField(help_text='Enter description')),
                ('created_on', models.DateField(help_text='Enter created date')),
                ('ingredients', models.ManyToManyField(help_text='Enter ingredients.', to='backend.Ingredient')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.User')),
            ],
        ),
    ]

# Generated by Django 3.2.3 on 2021-05-17 20:05

import autoslug.fields
import commons.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_1', models.CharField(max_length=200)),
                ('street_2', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='configchoice',
            options={'verbose_name': 'Config Choice', 'verbose_name_plural': 'Config Choices'},
        ),
        migrations.AlterModelOptions(
            name='configchoicecategory',
            options={'verbose_name': 'Config Choice Category', 'verbose_name_plural': ' Config Choice Categories'},
        ),
        migrations.AlterField(
            model_name='configchoice',
            name='name',
            field=models.CharField(help_text='Required and Unique', max_length=255, unique=True, verbose_name='Config Choice Name'),
        ),
        migrations.AlterField(
            model_name='configchoice',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=commons.models.slugify, verbose_name='Config Choice Slug'),
        ),
        migrations.AlterField(
            model_name='configchoicecategory',
            name='name',
            field=models.CharField(help_text='Required and Unique', max_length=255, unique=True, verbose_name='Config Choice Category Name'),
        ),
        migrations.AlterField(
            model_name='configchoicecategory',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', slugify=commons.models.slugify, verbose_name='Config Choice Category Slug'),
        ),
    ]

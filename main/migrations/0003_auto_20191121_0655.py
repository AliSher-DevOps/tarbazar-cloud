# Generated by Django 2.2.7 on 2019-11-21 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191120_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frenchise',
            name='address',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='frenchise',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='organization',
            name='iseller',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='ismanufecturer',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
    ]

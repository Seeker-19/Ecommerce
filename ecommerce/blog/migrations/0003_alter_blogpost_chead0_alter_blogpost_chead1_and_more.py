# Generated by Django 5.0.1 on 2024-01-13 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_chead0_blogpost_chead1_blogpost_chead2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
# Generated by Django 3.0.8 on 2020-08-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary_main', '0006_delete_carer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='images',
            field=models.ImageField(default=None, upload_to='', verbose_name='Превью выполненной работы'),
        ),
    ]

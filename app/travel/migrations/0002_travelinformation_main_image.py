# Generated by Django 2.0.3 on 2018-04-17 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelinformation',
            name='main_image',
            field=models.ImageField(default=1, upload_to='main_image', verbose_name='대표이미지'),
            preserve_default=False,
        ),
    ]
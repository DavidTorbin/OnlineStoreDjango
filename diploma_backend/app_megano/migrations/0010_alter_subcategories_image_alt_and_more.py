# Generated by Django 4.1.7 on 2023-03-19 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_megano', '0009_alter_subcategories_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategories',
            name='image_alt',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='subcategories',
            name='image_src',
            field=models.ImageField(blank=True, null=True, upload_to='images/category/', verbose_name='изображение'),
        ),
    ]

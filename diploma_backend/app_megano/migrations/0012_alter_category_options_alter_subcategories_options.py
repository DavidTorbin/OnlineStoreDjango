# Generated by Django 4.1.7 on 2023-03-22 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_megano', '0011_alter_category_options_category_index_sort_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['index_sort'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='subcategories',
            options={'ordering': ['index_sort'], 'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
    ]

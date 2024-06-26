# Generated by Django 5.0.3 on 2024-03-24 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('M', 'Мужское'), ('W', 'Женское')], default=('M', 'Мужское'), max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изминения'),
        ),
    ]

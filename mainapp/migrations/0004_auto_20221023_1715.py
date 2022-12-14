# Generated by Django 3.2 on 2022-10-23 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_courseteacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courseteacher',
            options={'verbose_name': 'преподаватель', 'verbose_name_plural': 'преподаватели'},
        ),
        migrations.AddField(
            model_name='courseteacher',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Создано'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='courseteacher',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AddField(
            model_name='courseteacher',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновлено'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-06-25 18:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_hero', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='heroi',
            name='descricao',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

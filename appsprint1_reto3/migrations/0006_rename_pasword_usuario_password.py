# Generated by Django 4.1 on 2022-09-08 04:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsprint1_reto3', '0005_rename_nombre_empresa_nombre_empresa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='pasword',
            new_name='password',
        ),
    ]
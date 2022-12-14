# Generated by Django 4.1 on 2022-09-04 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsprint1_reto3', '0003_rename_nit_empresa_nit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='apellidos',
            new_name='Apellidos',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='correo',
            new_name='Correo',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='fecha_creacion',
            new_name='Fecha_creacion',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='id_empleado',
            new_name='Id_empleado',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='id_empresa',
            new_name='Id_empresa',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='id_usuario',
            new_name='Id_usuario',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='nombre_empresa',
            new_name='Nombre_empresa',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='nombres',
            new_name='Nombres',
        ),
        migrations.RenameField(
            model_name='empleado',
            old_name='telefono',
            new_name='Telefono',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='ciudad',
            new_name='Ciudad',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='direccion',
            new_name='Direccion',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='fecha_creacion',
            new_name='Fecha_creacion',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='id_empresa',
            new_name='Id_empresa',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='id_usuario',
            new_name='Id_usuario',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='nit',
            new_name='Nit',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='nombre',
            new_name='Nombre',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='serctor_productivo',
            new_name='Serctor_productivo',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='telefono',
            new_name='Telefono',
        ),
    ]

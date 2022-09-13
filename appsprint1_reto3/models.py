from pyexpat import model
from django.db import models
class usuario(models.Model):
    id_usuario=models.IntegerField(primary_key=True)
    correo=models.CharField(max_length=30)
    imagen=models.CharField(max_length=30)
    nombre_usuario=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    rol=models.CharField(max_length=30) 
    fecha_creacion=models.DateField(max_length=10)
def __str__(self):
    return self.id_usuario,self.correo,self.imagen,self.nombre,self.pasword,self.rol,self.fecha_creacion,
class empresa(models.Model):
    Id_empresa=models.IntegerField(primary_key=True)
    Nombre_empresa=models.CharField(max_length=20)
    Nit=models.CharField(max_length=15) 
    Ciudad=models.CharField(max_length=30)
    Direccion=models.CharField(max_length=30) 
    Telefono=models.IntegerField(max_length=15) 
    Sector_productivo=models.CharField(max_length=30) 
    Fecha_creacion=models.DateField(max_length=10)
    Id_usuario=models.ForeignKey(usuario, on_delete=models.CASCADE)

class empleado(models.Model):
    Id_empleado=models.IntegerField(primary_key=True)
    Nombres=models.CharField(max_length=40)
    Apellidos=models.CharField(max_length=40)
    Correo=models.CharField(max_length=20)
    Telefono=models.IntegerField(max_length=15)
    Nombre_empresa=models.CharField(max_length=40)
    Fecha_creacion=models.DateField(max_length=10)
    Id_empresa=models.ForeignKey(empresa, on_delete=models.CASCADE)
    Id_usuario=models.ForeignKey(usuario, on_delete=models.CASCADE)

class registros(models.Model):
        Id_empresa=models.ForeignKey(empresa, on_delete=models.CASCADE)
        Resgistro_ingreso=models.IntegerField(max_length=10)
        Resgistro_gasto=models.IntegerField(max_length=10)
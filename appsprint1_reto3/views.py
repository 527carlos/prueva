from django.shortcuts import render
from calendar import Calendar
import json
from optparse import Values
from pdb import line_prefix
from django.shortcuts import render
from django.views import View
from .models import usuario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class usuarioviews(View):
 @method_decorator(csrf_exempt)
 def dispatch(sel,request,*args,**kwargs)  :
      return super().dispatch(request,*args,**kwargs) 
#consultar y agregar
 def get(self,request,doc=0):
   if doc>0:
      usu=list(usuario.objects.filter(id_usuario=doc).values())
      if len(usu)>0:
         usurespuesta=usu[0]
         datos={"usuario":usurespuesta}
      else:
         datos={"respuesta":" datos no encontrados"}
   else:
    usu=list(usuario.objects.values())
    datos={'listado_ususario':usu}
   return JsonResponse (datos)
#consulta con un parametro

 def post(self,request):
     datos=json.loads(request.body)
     usuario.objects.create(documento=datos['documento'],nombre=datos['nombre'],apellido=datos['apellido'],correo=datos['correo'],celular=datos['celular'])
     return JsonResponse(datos)
#insertar
 def put(self,request,doc):
   datos=json.loads(request.body)
   usu=list(usuario.objects.filter(id_usuario=doc).values()) 
   if len(usu)>0:
    usuario=usuario.objects.get(id_usuario=doc)
    usuario.correo=datos['correo']
    usuario.imagen=datos['imagen']
    usuario.nombre_usuario=datos['nombre_usuraio']
    usuario.password=datos['password']
    usuario.rol=datos['rol'] 
    usuario.fecha_creacion=['fecha_creacion']
    mensaje={"respuesta":"datos almacenado correctamente"}
   else:
      mensaje={"respuesta":"dotos no encontrados"}
   return JsonResponse(mensaje)
# eliminar
 def delete(self,request,doc):
   usu=list(usuario.objects.filter(id_usuario=doc).values())
   if len(usu)>0:
      usuario.objects.filter(id_usuario=doc).delete()
      mensaje={"mensaje":"el registro fue eliminado"}
   else:
      mensaje={"respuesta":"dotos no encontrados"}  
   return JsonResponse (mensaje)    
# Create your views here.

from django.urls import path
from appsprint1_reto3.views import usuarioviews

urlpatterns=[
    
    path('usuario/',usuarioviews.as_view(),name="listar"),
    path('usuario/<int:doc>', usuarioviews.as_view(), name="actualizar")
]

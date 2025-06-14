from django.urls import path
from .views import *

urlpatterns = [
    path("productos/index/", index_productos, name="index_productos"),
    path("productos/nuevo", registrar_productos, name="nuevo_productos"),
    path("productos/editar/<int:producto_id>/", editar_productos, name="editar_productos"),
    path("productos/eliminar/<int:id>", eliminar_productos, name="eliminar_productos")
]


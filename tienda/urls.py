from django.contrib import admin
from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('productos/listado', ProductosLista.as_view(), name='listado'),
    path('productos/crear', CrearProducto.as_view(), name='crear'),
    path('productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('productos/<int:pk>/edit', ProductoEditar.as_view(), name='producto_editar'),
    path('productos/<int:pk>/del', ProductoBorrar.as_view(), name='producto_borrar'),
    path('', ComprarProducto.as_view(), name='compra_listado'),
    #path('checkout/<int:pk>',Checkout.as_view(),name='checkout'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('perfil',PerfilView.as_view(),name='perfil'),
    path('informes',views.informes,name='informes'),
]
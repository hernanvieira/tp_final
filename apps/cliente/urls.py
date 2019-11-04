from django.urls import path
from .views import CrearCliente, ListarCliente, EditarCliente, EliminarCliente, ClienteHome, Auditoria

urlpatterns = [
        path ('crear_cliente/',CrearCliente,name='crear_cliente'),
        path ('listar_cliente/',ListarCliente,name='listar_cliente'),
        path ('editar_cliente/<int:dni>',EditarCliente,name='editar_cliente'),
        path ('eliminar_cliente/<int:dni>',EliminarCliente,name='eliminar_cliente'),
        path ('cliente_home/',ClienteHome,name='cliente_home'),
        path('auditoria/', Auditoria, name = 'auditoria')
]

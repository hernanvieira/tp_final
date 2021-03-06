from django.urls import path
from .views import CrearEstado, ListarEstado, EditarEstado, EliminarEstado
from .views import CrearEstado_pedido, ListarEstado_pedido, EditarEstado_pedido, EliminarEstado_pedido
from .views import CrearEstado_lote, ListarEstado_lote, EditarEstado_lote, EliminarEstado_lote

from django.contrib.auth.decorators import login_required

urlpatterns = [
                #URL Estado
                path ('crear_estado/',login_required(CrearEstado),name='crear_estado'),
                path ('listar_estado/',login_required(ListarEstado),name='listar_estado'),
                path ('editar_estado/<int:id_estado>',login_required(EditarEstado),name='editar_estado'),
                path ('eliminar_estado/<int:id_estado>',login_required(EliminarEstado),name='eliminar_estado'),

                #URL Estado_pedido
                path ('crear_estado_pedido/',login_required(CrearEstado_pedido),name='crear_estado_pedido'),
                path ('listar_estado_pedido/',login_required(ListarEstado_pedido),name='listar_estado_pedido'),
                path ('editar_estado_pedido/<int:id_estado_pedido>',login_required(EditarEstado_pedido),name='editar_estado_pedido'),
                path ('eliminar_estado_pedido/<int:id_estado_pedido>',login_required(EliminarEstado_pedido),name='eliminar_estado_pedido'),

                #URL Estado_lote
                path ('crear_estado_lote/',login_required(CrearEstado_lote),name='crear_estado_lote'),
                path ('listar_estado_lote/',login_required(ListarEstado_lote),name='listar_estado_lote'),
                path ('editar_estado_lote/<int:id_estado_lote>',login_required(EditarEstado_lote),name='editar_estado_lote'),
                path ('eliminar_estado_lote/<int:id_estado_lote>',login_required(EliminarEstado_lote),name='eliminar_estado_lote')
]

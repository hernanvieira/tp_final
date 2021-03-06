#Django 2.2

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout
from apps.cliente.views import Home, Auditoria, Estadistica
from apps.usuario.views import Login, logoutUsuario, VerPerfil, SignUp
from config.views import configuracion, configuracionMensaje

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente/',include(('apps.cliente.urls','cliente')),name='cliente'),
    path('estado/',include(('apps.estado.urls','estado'))),
    path('material/',include(('apps.material.urls','material'))),
    path('pedido/',include(('apps.pedido.urls','pedido'))),
    path('prenda/',include(('apps.prenda.urls','prenda')),name='prenda'),
    path('estado/',include(('apps.estado.urls','estado')),name='estado'),
    path('usuario/',include(('apps.usuario.urls','usuario')),name='usuario'),

    path('home/',login_required(Home), name = 'index'),
    path('estadistica/', login_required(Estadistica), name = 'estadistica'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/logout/', login_required(logoutUsuario), name='logout'),
    path('accounts/signup/', login_required(SignUp), name='signup'),
    path('config/configuracion/', login_required(configuracion), name='configuracion'),
    path('config/configuracion_mensaje/', login_required(configuracionMensaje), name='configuracion_mensaje'),
    path('usuario/ver_perfil/', login_required(VerPerfil), name='ver_perfil')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""musica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from musica import settings
from django.views.generic import TemplateView

from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from clasemusica.views import Vernota, Insertarnota, Editarnota, Eliminarnota
from clasemusica.views import Verdocente, Agregardocente
from clasemusica.views import Verestudiante, Agregarestudiante
from clasemusica.views import Verasignatura, Agregarasignatura
from clasemusica.views import Agregarperfil, Verperfil

from django.conf.urls.static import static

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    ##nota
    path('vernota/', Vernota.as_view()),
    path('insertarnota/', Insertarnota.as_view()),
    path('editarnota/<int:pk>', Editarnota.as_view()),
    path('eliminarnota/<int:pk>', Eliminarnota.as_view()),
    ##docente
    path('verdocente/', Verdocente.as_view()),
    path('agregardocente/', Agregardocente.as_view()),
    ##estudiante
    path('agregarestudiante/', Agregarestudiante.as_view()),
    path('verestudiante/', Verestudiante.as_view()),
    ##asignatura
    path('verasignatura/', Verasignatura.as_view()),
    path('agregarasignatura/', Agregarasignatura.as_view()),
    ##perfil
    path('verperfil/', Verperfil.as_view()),
    path('agregarperfil/', Agregarperfil.as_view()),
    ##login
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view()),

]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

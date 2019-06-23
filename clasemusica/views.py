from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Notas, Docente, Estudiante, Asiganatura, Profile
from.forms import Formularionota, Formulariodocente, FormularioEstudiante, Formularioasignatura, Formularioperfil

class Vernota(PermissionRequiredMixin, ListView):
    permission_required = 'clasemusica.view_notas'
    login_url = 'login'
    model = Notas
    template_name = 'vernota.html'

    #def get_queryset(self):
     #   queryset = super(Vernota, self).get_queryset()

      ##  if self.request.user.groups.filter(name="grupoestu").exists():
        ##    queryset = queryset.filter(estudiante__user=self.request.user)

       ## if self.request.user.groups.filter(name="grupoprofe").exists():
         ##   queryset = queryset.filter(docente__user=self.request.user)

        ##return queryset

class Insertarnota(PermissionRequiredMixin, FormView):
    permission_required = 'clasemusica.add_notas'
    login_url = 'login'
    form_class = Formularionota
    template_name = 'insertarnota.html'
    success_url = '/vernota'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Editarnota(PermissionRequiredMixin, UpdateView):
    permission_required = 'clasemusica.change_notas'
    login_url = 'login'
    model = Notas
    form_class = Formularionota
    template_name = 'editarnota.html'
    success_url = '/vernota'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class Eliminarnota(PermissionRequiredMixin, DeleteView):
    permission_required = 'clasemusica.del_notas'
    login_url = 'login'
    model = Notas
    template_name = 'eliminarnota.html'
    success_url ='/vernota'


class Verdocente(PermissionRequiredMixin, ListView):
    permission_required = 'clasemusica.view_docente'
    login_url = 'login'
    model = Docente
    template_name = 'verdocente.html'

   ## def get_queryset(self):
     ##   queryset = super(Vernota, self).get_queryset()

       ## if self.request.user.groups.filter(name="grupoestu").exists():
         ##   queryset = queryset.filter(estudiante__user=self.request.user)

        ##if self.request.user.groups.filter(name="grupoprofe").exists():
          ##  queryset = queryset.filter(docente__user=self.request.user)

        ##return queryset

class Agregardocente(PermissionRequiredMixin, FormView):
    permission_required = 'clasemusica.add_docente'
    login_url = 'login'
    form_class = Formulariodocente
    template_name = 'agregardocente.html'
    success_url = ' /verdocente'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Verestudiante(PermissionRequiredMixin, ListView):
    permission_required = 'clasemusica.view_estudiante'
    login_url = 'login'
    model = Estudiante
    template_name = 'Verestudiante.html'

    ##def get_queryset(self):
      ##  queryset = super(Vernota, self).get_queryset()

        ##if self.request.user.groups.filter(name="grupoestu").exists():
          ##  queryset = queryset.filter(estudiante__user=self.request.user)

        ##if self.request.user.groups.filter(name="grupoprofe").exists():
          ##  queryset = queryset.filter(docente__user=self.request.user)

       ## return queryset

class Agregarestudiante(PermissionRequiredMixin, FormView):
    permission_required = 'clasemusica.add_estudiante'
    login_url = 'login'
    form_class = FormularioEstudiante
    template_name = 'agregarestudiante.html'
    success_url = '/verestudiante'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Verasignatura(LoginRequiredMixin, ListView):
    permission_required = 'clasemusica.view_asignatura'
    login_url = 'login'
    model = Asiganatura
    template_name = 'verasignatura.html'

   ## def get_queryset(self):
     ##   queryset = super(Vernota, self).get_queryset()

       ## if self.request.user.groups.filter(name="grupoestu").exists():
         ##   queryset = queryset.filter(estudiante__user=self.request.user)

       ## if self.request.user.groups.filter(name="grupoprofe").exists():
        ##    queryset = queryset.filter(docente__user=self.request.user)

        ##return queryset

class Agregarasignatura(PermissionRequiredMixin, FormView):
    permission_required = 'clasemusica.add_asignatura'
    login_url = 'login'
    form_class = Formularioasignatura
    template_name = 'agregarasignatura.html'
    success_url = '/verasignatura'
    def form_valid(self, form):
         form.save()
         return super().form_valid(form)


class Verperfil(PermissionRequiredMixin, ListView):
    permission_required = 'clasemusica.view_perfil'
    login_url = 'login'
    model = Profile
    template_name = 'verperfil.html'

    ##def get_queryset(self):
      ##3  queryset = super(Vernota, self).get_queryset()

       ## if self.request.user.groups.filter(name="grupoestu").exists():
         ##   queryset = queryset.filter(estudiante__user=self.request.user)

        ##if self.request.user.groups.filter(name="grupoprofe").exists():
          ##  queryset = queryset.filter(docente__user=self.request.user)

        ##return queryset

class Agregarperfil(PermissionRequiredMixin, FormView):
    permission_required = 'clasemusica.add_perfil'
    login_url = 'login'
    form_class = Formularioperfil
    template_name = 'agregarperfil.html'
    success_url = '/verperfil'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# Create your views here.

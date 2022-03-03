

from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from reparation.models import Sinistre
from reparation.forms import SinistreForm

#from reparation.views import SinistreListePageView, SinistreCreatePageView, SinistreDeletePageView, SinistreUpdatePageView

class SinistreListePageView(LoginRequiredMixin,ListView):
  model = Sinistre
  template_name = "reparation/sinistre-list.html"
  context_object_name = "sinistres"




class SinistreCreatePageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = Sinistre
  form_class = SinistreForm
  template_name = "reparation/sinistre-add.html"
  context_object_name = "sinistre"


  def get_success_url(self):
    return reverse("sinistre:sinistre-list")

  success_message = "Sinistre  ajouté avec succès!"

  def get_form_kwargs(self):
    kwargs = super(SinistreCreatePageView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

class SinistreUpdatePageView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Sinistre
  form_class = SinistreForm
  template_name = "reparation/sinistre-edit.html"
  context_object_name = "sinistre"

  success_message = "Sinistre modifiée avec succès!!"

  def get_success_url(self):
    return reverse("sinistre:sinistre-list")

  def get_form_kwargs(self):
    kwargs = super(SinistreUpdatePageView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs



class SinistreDeletePageView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  model = Sinistre
  template_name = "reparation/sinistre-delete.html"
  context_object_name = "sinistre"

  success_message = "Sinistre supprimée avec succès!"

  def get_success_url(self):
    return reverse("sinistre:sinistre-list")



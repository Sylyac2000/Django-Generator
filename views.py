

from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from reparation.models import Reparation
from reparation.forms import ReparationForm

from reparation.views import ReparationListePageView, ReparationCreatePageView, ReparationDeletePageView, ReparationUpdatePageView

class ReparationListePageView(LoginRequiredMixin,ListView):
  model = Reparation
  template_name = "reparation/reparation-list.html"
  context_object_name = "reparations"




class ReparationCreatePageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = Reparation
  form_class = ReparationForm
  template_name = "reparation/reparation-add.html"
  context_object_name = "reparation"


  def get_success_url(self):
    return reverse("reparation:reparation-list")

  success_message = "Reparation  ajouté avec succès!"

  def get_form_kwargs(self):
    kwargs = super(ReparationCreatePageView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

class ReparationUpdatePageView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = Reparation
  form_class = ReparationForm
  template_name = "reparation/reparation-edit.html"
  context_object_name = "reparation"

  success_message = "Reparation modifiée avec succès!!"

  def get_success_url(self):
    return reverse("reparation:reparation-list")

  def get_form_kwargs(self):
    kwargs = super(ReparationUpdatePageView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs



class ReparationDeletePageView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  model = Reparation
  template_name = "reparation/reparation-delete.html"
  context_object_name = "reparation"

  success_message = "Reparation supprimée avec succès!"

  def get_success_url(self):
    return reverse("reparation:reparation-list")



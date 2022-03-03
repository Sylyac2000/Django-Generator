import os
file_name = 'views.py'
f = open(file_name, 'w+')  # open file in append mode

appname ="reparation"

modelname="Sinistre"
modelnameLower ="sinistre"
modelnamePlural ="sinistres"

fields = ['vehicule','chauffeur','descriptionsinistre','imagedusinistre','datedusinistre','datedusinistre','datecreation','statut']

templatefolder ="templates/"

args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural}
strCodeViews = """

from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from {appname}.models import {modelname}
from {appname}.forms import {modelname}Form

#from {appname}.views import {modelname}ListePageView, {modelname}CreatePageView, {modelname}DeletePageView, {modelname}UpdatePageView

class {modelname}ListePageView(LoginRequiredMixin,ListView):
  model = {modelname}
  template_name = "{appname}/{modelnameLower}-list.html"
  context_object_name = "{modelnamePlural}"




class {modelname}CreatePageView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
  model = {modelname}
  form_class = {modelname}Form
  template_name = "{appname}/{modelnameLower}-add.html"
  context_object_name = "{modelnameLower}"


  def get_success_url(self):
    return reverse("{modelnameLower}:{modelnameLower}-list")

  success_message = "{modelname}  ajouté avec succès!"

  def get_form_kwargs(self):
    kwargs = super({modelname}CreatePageView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

class {modelname}UpdatePageView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
  model = {modelname}
  form_class = {modelname}Form
  template_name = "{appname}/{modelnameLower}-edit.html"
  context_object_name = "{modelnameLower}"

  success_message = "{modelname} modifiée avec succès!!"

  def get_success_url(self):
    return reverse("{modelnameLower}:{modelnameLower}-list")

  def get_form_kwargs(self):
    kwargs = super({modelname}UpdatePageView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs



class {modelname}DeletePageView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
  model = {modelname}
  template_name = "{appname}/{modelnameLower}-delete.html"
  context_object_name = "{modelnameLower}"

  success_message = "{modelname} supprimée avec succès!"

  def get_success_url(self):
    return reverse("{modelnameLower}:{modelnameLower}-list")


""".format(**args)
f.write(strCodeViews)

f.close()

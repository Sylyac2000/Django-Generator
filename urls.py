

from django.urls import path

from reparation.views import SinistreListePageView, SinistreCreatePageView, SinistreDeletePageView, SinistreUpdatePageView


app_name="reparation"

urlpatterns = [

  path('sinistre/', SinistreListePageView.as_view(), name='sinistre-list'),
  path('sinistre/add', SinistreCreatePageView.as_view(), name='sinistre-add'),
  path('reparation/edit/<int:pk>', SinistreUpdatePageView.as_view(), name='sinistre-edit'),
  #path('sinistre/details/<int:pk>', SinistreDetailsPageView.as_view(), name='sinistre-details'),
  path('sinistre/delete/<int:pk>', SinistreDeletePageView.as_view(), name='sinistre-delete'),

]


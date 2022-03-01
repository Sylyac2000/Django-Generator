

from django.db import models

# Create your models here.

class Assignation(models.Model):
  vehicule = models.CharField(max_length=50)
	chauffeur = models.CharField(max_length=50)
  agence = models.CharField(max_length=50)
  dateassignation = models.CharField(max_length=50)
	datecreation = models.CharField(max_length=50)
	

    def __str__(self):
        return self.vehicule

     class Meta:
        ordering = ['vehicule','chauffeur','agence','dateassignation','datecreation',]


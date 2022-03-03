

from django.utils.safestring import mark_safe
from django import forms
from django.forms import ModelForm

from  reparation.models import Sinistre
class SinistreForm(ModelForm):

    class Meta:
        model = Sinistre

        fields = ("vehicule","chauffeur","descriptionsinistre","imagedusinistre","datedusinistre","datecreation","statut",)

        #fields = '__all__'

        labels = {
		"vehicule":  mark_safe('vehicule<span class="text-danger">*</span>'),
		"chauffeur":  mark_safe('chauffeur<span class="text-danger">*</span>'),
		"descriptionsinistre":  mark_safe('descriptionsinistre<span class="text-danger">*</span>'),
		"imagedusinistre":  mark_safe('imagedusinistre<span class="text-danger">*</span>'),
		"datedusinistre":  mark_safe('datedusinistre<span class="text-danger">*</span>'),
		"datecreation":  mark_safe('datecreation<span class="text-danger">*</span>'),
		"statut":  mark_safe('statut<span class="text-danger">*</span>'),
		}
	
        widgets = {
		"vehicule":  forms.TextInput(attrs={'class': 'form-control'}),
		"chauffeur":  forms.TextInput(attrs={'class': 'form-control'}),
		"descriptionsinistre":  forms.TextInput(attrs={'class': 'form-control'}),
		"imagedusinistre":  forms.TextInput(attrs={'class': 'form-control'}),
		"datedusinistre":  forms.TextInput(attrs={'class': 'form-control'}),
		"datecreation":  forms.TextInput(attrs={'class': 'form-control'}),
		"statut":  forms.TextInput(attrs={'class': 'form-control'}),
		}
	

    def __init__(self, user, *args, **kwargs):
        super(SinistreForm, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.user = user

      def clean_vehicule(self):
			vehicule = self.cleaned_data['vehicule']
			 return vehicule

		 def clean_chauffeur(self):
			chauffeur = self.cleaned_data['chauffeur']
			 return chauffeur

		 def clean_descriptionsinistre(self):
			descriptionsinistre = self.cleaned_data['descriptionsinistre']
			 return descriptionsinistre

		 def clean_imagedusinistre(self):
			imagedusinistre = self.cleaned_data['imagedusinistre']
			 return imagedusinistre

		 def clean_datedusinistre(self):
			datedusinistre = self.cleaned_data['datedusinistre']
			 return datedusinistre

		 def clean_datecreation(self):
			datecreation = self.cleaned_data['datecreation']
			 return datecreation

		 def clean_statut(self):
			statut = self.cleaned_data['statut']
			 return statut

		 



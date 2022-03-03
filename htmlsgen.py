import os
file_name = 'forms.py'
f = open(file_name, 'w+')  # open file in append mode

appname ="reparation"

modelname="Sinistre"
modelnameLower ="sinistre"
modelnamePlural ="sinistres"

fields = ['vehicule','chauffeur','descriptionsinistre','imagedusinistre','datedusinistre','datecreation','statut']

fieldslabels = "labels = {\n\t\t"

formfields = ''

for field in fields:
  formfields += '"{0}",'.format(field)


for field in fields:
  fieldslabels += '"{0}":  mark_safe(\'{0}<span class="text-danger">*</span>\'),\n\t\t'.format(field)

fieldslabels += "}\n\t"

fieldswidget = "widgets = {\n\t\t"

for field in fields:
  fieldswidget += '"{0}":  forms.TextInput(attrs={{\'class\': \'form-control\'}}),\n\t\t'.format(field)

fieldswidget += "}\n\t"


fieldsvalidation = ""

for field in fields:
  fieldsvalidation += "def clean_{0}(self):\n\t\t\t{0} = self.cleaned_data['{0}']\n\t\t\t return {0}\n\n\t\t ".format(field)

fieldsvalidation += ""


args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural,
'fields':fields,'formfields':formfields,'fieldslabels':fieldslabels,'fieldswidget':fieldswidget,'fieldsvalidation':fieldsvalidation}


strCode = """

from django.utils.safestring import mark_safe
from django import forms
from django.forms import ModelForm

from  {appname}.models import {modelname}
class {modelname}Form(ModelForm):

    class Meta:
        model = {modelname}

        fields = ({formfields})

        #fields = '__all__'

        {fieldslabels}
        {fieldswidget}

    def __init__(self, user, *args, **kwargs):
        super({modelname}Form, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.user = user

      {fieldsvalidation}


""".format(**args)
f.write(strCode)

f.close()

fieldsdefinition = """ 
<form id="form" class="" method="post" enctype="multipart/form-data">
{% csrf_token %}
{% for field in form %}\n
<div class="mb-3 row">\n
  \t<label class="col-sm-2 form-label" for="{{ field.id_for_label  }}">{{ field.label }}</label>\n
  <div class="col-sm-10">\n
  \t{{ field }}\n
  {% for error in field.errors %}\n
   \t<div class="alert alert-danger ml-3">{{ error }}</div>\n
   {% endfor %}\n
   </div>\n
  </div>\n
  {% endfor %}
<div class="line"></div><br>
                                        <div class="mb-3 row">
                                            <div class="col-sm-4 offset-sm-2">
												<a class="btn btn-warning  mb-2" href="{% url 'organisation:chauffeur-list' %}"><i class="fas fa-times"></i> Annuler</a>

                                                <button type="submit" class="btn btn-primary mb-2"><i class="fas fa-paper-plane"></i> Envoyer</button>
                                            </div>
                                        </div>
                                    </form>
                                                
"""


html_file_name = 'forms.html'
fht = open(html_file_name, 'w+') 
fht.write(fieldsdefinition)

fht.close()                                                   

# Gen folder for html fields
directory ='{0}/'.format(appname)
if not os.path.exists(directory):
    os.makedirs(directory)
os.replace(html_file_name,directory+html_file_name)

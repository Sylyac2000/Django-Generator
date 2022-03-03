import os
file_name = 'urls.py'
f = open(file_name, 'w+')  # open file in append mode

appname ="reparation"

modelname="Sinistre"
modelnameLower ="sinistre"
modelnamePlural ="sinistres"

fields = ['vehicule','chauffeur','descriptionsinistre','imagedusinistre','datedusinistre','datecreation','statut']






args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural,
'fields':fields}


strCode = """

from django.urls import path

from {appname}.views import {modelname}ListePageView, {modelname}CreatePageView, {modelname}DeletePageView, {modelname}UpdatePageView


app_name="{appname}"

urlpatterns = [

  path('{modelnameLower}/', {modelname}ListePageView.as_view(), name='{modelnameLower}-list'),
  path('{modelnameLower}/add', {modelname}CreatePageView.as_view(), name='{modelnameLower}-add'),
  path('{appname}/edit/<int:pk>', {modelname}UpdatePageView.as_view(), name='{modelnameLower}-edit'),
  #path('{modelnameLower}/details/<int:pk>', {modelname}DetailsPageView.as_view(), name='{modelnameLower}-details'),
  path('{modelnameLower}/delete/<int:pk>', {modelname}DeletePageView.as_view(), name='{modelnameLower}-delete'),

]

""".format(**args)
f.write(strCode)

f.close()
'''
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
os.replace(html_file_name,directory+html_file_name)'''

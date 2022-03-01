import os
file_name = 'forms.py'
f = open(file_name, 'w+')  # open file in append mode

appname ="activite"

modelname="Activite"
modelnameLower ="activite"
modelnamePlural ="activites"

fields = ['activite', 'description', 'datecreation']

args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural,
'fields':fields}
strCode = """

from django.forms import ModelForm

from  .models import {modelname}
class {modelname}Form(ModelForm):

    class Meta:
        model = {modelname}

        fields = ('{fields[0]}','{fields[1]}')
        #fields = '__all__'
        
    def __init__(self, user, *args, **kwargs):
        super({modelname}Form, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None)
        self.user = user
""".format(**args)
f.write(strCode)

f.close()

fieldsdefinition = """ {{% extends 'base.html' %}}
    {{% load static %}}
    {{% block content %}}
    <div class="app-admin-wrap layout-sidebar-large">
       {{% include 'myaccount/navbar.html' %}}
        {{% include 'myaccount/leftsidebar.html' %}}        <!-- =============== Left side End ================-->\n<div class="main-content-wrap sidenav-open d-flex flex-column">\n<!-- ============ Body content start ============= -->\n<div class="main-content"><div class="breadcrumb">
                    <h1 class="mr-2">&nbsp;</h1>
                    <ul>
                        <li><a href="">Ajout des utilisateurs / membres</a></li>

                    </ul>
                </div><div class="separator-breadcrumb border-top"></div>\n<div class="row"><div class="col-lg-12"><div class="card">\n<div class="card-body">\n<div class="card-title">Formulaire {modelname}</div>\n<form id="form{modelnameLower}" action="" method="post">\n<div class="card-body">""".format(**args)

for field in fields:
  fieldsdefinition += """\n<div class="form-row">
        \n\t<div class="form-group col-md-12">\n
        <label class="ul-form__label" for="inputEmail4">{0}:                 </label>
          <div class="input-group mb-3">
         <input name="{0}"  value="{{{{form.{0}.value}}}}"  class="form-control" type="text" placeholder="{0}" aria-label="nom" aria-describedby="basic-addon1" />                                     </div>
         {{% for erreur in form.{0}.errors %}}
              <div class="alert alert-danger ml-3">{{{{ erreur }}}}</div>
          {{% endfor %}}
        </div>
  </div>\n\t""".format(field)


strbtn = """<input class="btn btn-primary btn-block m-1 mb-3" type="submit" value="Enregistrer" /></div></form>\n</div>\n</div>\n</div>\n</div>\n</div>\n
<!-- Footer Start -->
<div class="flex-grow-1"></div>
{{% include 'myaccount/footer.html' %}}
{{% endblock %}}
<!-- fotter end -->
\n</div>
    </div>"""
fieldsdefinition += strbtn

html_file_name = 'forms.html'
fht = open(html_file_name, 'w+') 
fht.write(fieldsdefinition)

fht.close()                                                   

# Gen folder for html fields
directory ='{0}/'.format(appname)
if not os.path.exists(directory):
    os.makedirs(directory)
os.replace(html_file_name,directory+html_file_name)

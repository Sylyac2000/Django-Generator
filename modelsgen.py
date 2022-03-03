file_name = 'models.py'
f = open(file_name, 'w+')  # open file in append mode

appname ="reparation"

modelname="Sinistre"
modelnameLower ="sinistre"
modelnamePlural ="sinistres"

fields = ['vehicule','chauffeur','descriptionsinistre','imagedusinistre','datedusinistre','datecreation','statut']

fieldsdefinition = "";
fieldstrfunc = "def __str__(self):\n\t\treturn ";
ordering = "ordering = [";

for field in fields:
  fieldsdefinition += "{0} = models.CharField(max_length=50)\n\t".format(field)
  fieldstrfunc += "self.{0} +' '+".format(field)
  ordering += "'{0}',".format(field)

ordering += "]"


  
args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural,
'fields':fields, 'fieldsdefinition':fieldsdefinition, 'fieldstrfunc':fieldstrfunc, 'ordering':ordering}

fieldsdefinition += """
 def __str__(self):
        return self.{fields[0]}
  """.format(**args)

strCode = """

from django.db import models

# Create your models here.

class {modelname}(models.Model):
    {fieldsdefinition}

    def __str__(self):
        return self.{fields[0]}

     class Meta:
        {ordering}

""".format(**args)
f.write(strCode)

f.close()
import os
from pathlib import Path
appname ="reparation"

modelname="Sinistre"
modelnameLower ="sinistre"
modelnamePlural ="sinistres"

fields = ['vehicule','chauffeur','descriptionsinistre','imagedusinistre','datedusinistre','datecreation','statut']

args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural,
'fields':fields,}


maintemplatesfolder ="templates/"

##########add########################
addTemplate = 'bootstrap-simple-admin-template-add.html'
#addTemplate = 'test.html'

file = maintemplatesfolder + '/' + addTemplate

thecontents = Path(file).read_text()

thecontents = thecontents.format(**args)



directory ='{0}/'.format(modelnameLower)
if not os.path.exists(directory):
    os.makedirs(directory)

html_add_layout_file = '{0}/{0}-add.html'.format(modelnameLower)
fht = open(html_add_layout_file, 'w+') 
fht.write(thecontents)

fht.close() 

################edit########################
editTemplate = 'bootstrap-simple-admin-template-edit.html'
#addTemplate = 'test.html'

file = maintemplatesfolder + '/' + editTemplate

thecontents = Path(file).read_text()

thecontents = thecontents.format(**args)



directory ='{0}/'.format(modelnameLower)
if not os.path.exists(directory):
    os.makedirs(directory)

html_edit_layout_file = '{0}/{0}-edit.html'.format(modelnameLower)
fht = open(html_edit_layout_file, 'w+') 
fht.write(thecontents)

fht.close() 

#######List #####

listTemplate = 'bootstrap-simple-admin-template-list.html'

file = maintemplatesfolder + '/' + listTemplate

thecontents = Path(file).read_text()

thecontents = thecontents.format(**args)

directory ='{0}/'.format(modelnameLower)
if not os.path.exists(directory):
    os.makedirs(directory)

html_list_layout_file = '{0}/{0}-list.html'.format(modelnameLower)
fht = open(html_list_layout_file, 'w+') 
fht.write(thecontents)

fht.close() 

################delete########################
deleteTemplate = 'bootstrap-simple-admin-template-delete.html'


file = maintemplatesfolder + '/' + deleteTemplate

thecontents = Path(file).read_text()

thecontents = thecontents.format(**args)



directory ='{0}/'.format(modelnameLower)
if not os.path.exists(directory):
    os.makedirs(directory)

html_delete_layout_file = '{0}/{0}-delete.html'.format(modelnameLower)
fht = open(html_delete_layout_file, 'w+') 
fht.write(thecontents)

fht.close() 

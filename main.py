import os
file_name = 'views.txt'
f = open(file_name, 'w+')  # open file in append mode

appname ="immobilier"

modelname="Locataire"
modelnameLower ="locataire"
modelnamePlural ="locataires"

templatefolder ="templates/"

args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural}
strCodeViews = """

def ajout(request):
    form = {modelname}ModelForm()

    if request.method =='POST':
        form = {modelname}ModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste')

    context = {{
        'form':form
    }}
    return render(request,'{appname}/ajout.html',context)

def liste(request):

    {modelnamePlural} = {modelname}.objects.all()


    context = {{
        '{modelnamePlural}': {modelnamePlural}
    }}

    return render(request,'{appname}/liste.html', context)

def update(request, pk):

    {modelnameLower} = {modelname}.objects.get(id=pk)

    form = {modelname}ModelForm(instance={modelnameLower})
    if request.method == 'POST':
        form = {modelname}ModelForm(request.POST, instance={modelnameLower})
        if form.is_valid():
            form.save()
            return redirect('liste')



    context = {{
        form: form,
        '{modelnameLower}': {modelnameLower},
    }}

    return render(request,'{appname}/update.html', context)
""".format(**args)
f.write(strCodeViews)

f.close()

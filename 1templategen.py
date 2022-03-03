import os


appname ="reparation"

modelname="Sinistre"
modelnameLower ="sinistre"
modelnamePlural ="sinistres"

maintemplatefolder ="templates/"

appname ="immobilier"
modelname="Locataire"
modelnameLower ="locataire"
modelnamePlural ="locataires"

fields = ['nom', 'prenom', 'mobile']

args = {'appname':appname, 'modelname':modelname, 'modelnameLower':modelnameLower, 'modelnamePlural':modelnamePlural,
'fields':fields}

#mainLayout 
strBaseHtml = """{{% load static %}}
<!DOCTYPE html>
<html lang="en" dir="">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Admin ESPAGRI</title>
    <link href="https://fonts.googleapis.com/css?family=Nunito:300,400,400i,600,700,800,900" rel="stylesheet" />
    <link href="{{% static 'css/themes/lite-purple.css' %}}" rel="stylesheet" />
    <link href="{{% static 'css/plugins/perfect-scrollbar.min.css' %}}" rel="stylesheet" />
    <link href="{{% static 'css/plugins/fontawesome-5.css' %}}" rel="stylesheet" />
    <link href="{{% static 'css/plugins/datatables.min.css' %}}" rel="stylesheet" />


</head>

<body class="text-left">
{{% block content %}}
{{% endblock content %}}
{{% include 'scripts.html' %}}
</body>
</html>"""

html_layout_file = 'base.html'
fht = open(html_layout_file, 'w+') 
fht.write(strBaseHtml)

fht.close() 

# Gen folder for html template
directory ='{0}/'.format(maintemplatefolder)
if not os.path.exists(directory):
    os.makedirs(directory)

strJs ="""{{% load static %}}
    <script src="{{% static 'js/plugins/jquery-3.3.1.min.js'%}}"></script>
    <script src="{{% static 'js/plugins/bootstrap.bundle.min.js'%}}"></script>
    <script src="{{% static 'js/plugins/perfect-scrollbar.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/script.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/sidebar.large.script.min.js'%}}"></script>
    <script src="{{% static 'js/plugins/apexcharts.min.js'%}}"></script>
    <script src="{{% static 'js/plugins/echarts.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/echart.options.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/dashboard.v3.script.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/apexcharts.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/card.metrics.script.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/widgets-statistics.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/customizer.script.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/apexColumnChart.script.min.js'%}}"></script>

    <script src="{{% static 'js/plugins/datatables.min.js'%}}"></script>
    <script src="{{% static 'js/scripts/datatables.script.min.js'%}}"></script>
    <script>

   $( document ).ready(function() {{
       $("#{modelnameLower}form").validate({{}});
    }});
""".format(**args)
js_file = 'script.html'
fht = open(js_file, 'w+') 
fht.write(strJs)

fht.close() 

os.replace(html_layout_file,directory+html_layout_file)
os.replace(js_file,directory+js_file)

from django.shortcuts import render
from . models import project,projectCatogery
def blog(req):
    projectdatabase = project.objects.all()
    category = projectCatogery.objects.all()
    catid = req.GET.get('category')

    if catid:
        projectdatabase = project.objects.filter(project_catogery_name = catid)
    else:
        pass

    dic = {'database':projectdatabase,'category':category}
    return render (req, 'home.html', dic)

def artical(req, pk):
    projectdatabase = project.objects.get(project_id = pk)
    return render(req, 'artical.html', {'project':projectdatabase})

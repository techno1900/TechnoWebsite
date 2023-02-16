from django.shortcuts import render
from .models import personalDetails

def about(req):
    personaldatabase = personalDetails.objects.all()
    return render(req, 'about.html', {'personal':personaldatabase})

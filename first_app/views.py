from django.shortcuts import render,redirect
from .form import base_forms
from . import models
# Create your views here.
def form_page (request):
    return render(request, 'form.html')
def home(request):
    myModel = models.myModel.objects.all()
    return render(request,"home.html", {'data': myModel})

def DjangoForm(request):
    student = models.myModel.objects.all()
    f = base_forms(request.POST)
    if f.is_valid():
        print(f.cleaned_data)
    return render(request, 'form.html', {'form':f})

def delete_student(request, roll):
    std = models.Student.objects.get(pk = roll).delete()
    return redirect("homepage")
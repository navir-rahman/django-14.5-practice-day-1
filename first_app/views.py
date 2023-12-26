from django.shortcuts import render
from .form import base_forms
# Create your views here.
def form_page (request):
    return render(request, 'form.html')

def DjangoForm(request):
    f = base_forms(request.POST)
    if f.is_valid():
        print(f.cleaned_data)
    return render(request, 'form.html', {'form':f})
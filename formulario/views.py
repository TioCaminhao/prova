from django.shortcuts import render, redirect
from .models import*
from .forms import*

def cadastro(request):
    forms = formulario2(request.POST or None)
    if forms.is_valid():
        forms.save()
        return redirect('dados')
    return render(request, 'cadastro.html', { 'forms': forms })

def dados(request):
    forms = formulario.objects.all()
    return render(request, 'dados.html', { 'forms': forms})



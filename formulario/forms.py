from .models import formulario
from django import forms

class formulario2(forms.ModelForm):
    class Meta:
        model = formulario
        fields = '__all__'


        widgets = {
            'nome':  forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
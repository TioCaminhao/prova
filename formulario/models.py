from django.db import models

class formulario(models.Model):
    nome = models.CharField(max_length=200)
    data = models.DateField()
    email = models.EmailField()
    

from django.db import models

# Create your models here.
class ClientData(models.Model):
    name = models.CharField(max_length=200, help_text='Digite seu nome')

    cpf = models.IntegerField(max_length=11)

    
    def __str__(self) -> str:
        return self.name
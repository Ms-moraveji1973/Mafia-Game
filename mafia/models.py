from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class MafiaRoleModel(models.Model):
    name = models.CharField(max_length=50 , null=True)
    role = models.CharField(max_length=10, choices=(('mafia', 'Mafia'), ('citizen', 'Citizen')))

    def __str__(self):
        return self.name + " (" + self.role + ")"



class Player(models.Model):
    pass

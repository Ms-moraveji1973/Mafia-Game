from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class MafiaRoleModel(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=100, choices=(('godfather', 'GodFather'),('citizen', 'Citizen') ,
                             ('doctor' , 'Doctor') , ('leon' , 'Leon'), ('nostradamus','Nostradamus') ,
                             ('constantine' , 'Constantine') , ('ken' , 'Ken') ))

    def __str__(self):
        return self.name + " (" + self.role + ")"


class CartModel(models.Model):
    cart_id = models.CharField(max_length=50)
    cart = models.CharField(max_length=200 , choices =( ('silence' , 'Silence') , ('face_off' , 'Face_Off') , ('imagin' , 'Imagin') ,
                                                         ('person' , 'Person') , ('dastband' , 'Dastband') ))

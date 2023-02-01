from django.db import models


# Create your models here.


# class Type_Sexe(models.TextChoices):
#     f = "feminin"
#     m = "masculin"


class Client(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    prenom = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    sexe = models.CharField(max_length=10)
    cni = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom} {self.prenom} {self.phone} {self.sexe} {self.cni}"


class Type_Fete(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    montant = models.IntegerField(default=0)
    code = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom} {self.montant} {self.code}"


class Type_Decor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=32)
    montant = models.IntegerField(default=0)
    code = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.nom} {self.montant} {self.code}"


class Reservation(models.Model):
    id = models.BigAutoField(primary_key=True)
    # on_delete cascade si tu supprime un client, nivyiw vyose birajana
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    #  on_delete protect si tu supprime la fete, hari ayandi ma données ajany na fete ahandi ntibikunda
    type_fete = models.ForeignKey(Type_Fete, on_delete=models.PROTECT)
    type_decor = models.ForeignKey(Type_Decor, on_delete=models.PROTECT)
    date_de_reservation = models.DateField()
    avance = models.IntegerField(default=0)
    a_payer = models.IntegerField(default=0)
    date_avance = models.DateTimeField(auto_now=True)
    date_payer_total = models.DateField(null=True)

   # surcharge des methodes   :: guteranya le montant de la fête et le montant du décor

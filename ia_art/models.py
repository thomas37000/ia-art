from django.db import models


# style de peintures
class Movement(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50, null=False)
    lastname = models.CharField(max_length=50, null=False)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True)
    age = models.IntegerField(null=True)
    is_alive = models.BooleanField(null=True)
    country = models.CharField(max_length=50, null=True)
    movements = models.ManyToManyField(Movement, blank=True)

    def __str__(self):
        return self.name + " " + self.lastname

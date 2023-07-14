from django.db import models
from django.core.exceptions import ValidationError


def validate_image_size(value):
    # Taille maximale en octets (1 Mo)
    max_size = 1024 * 1024

    if value.size > max_size:
        raise ValidationError("La taille de l'image ne doit pas dépasser 1 Mo.")


class Painting(models.Model):
    image = models.ImageField(
        upload_to="ia_art/paintings/", validators=[validate_image_size], blank=True, null=True
    )
    image_url = models.URLField(max_length=300, null=True, blank=True)

    def __str__(self):
        return (
            self.image_url if self.image_url else self.image.name if self.image else ""
        )


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
    paintings = models.ManyToManyField(Painting, blank=True)

    def __str__(self):
        return self.name + " " + self.lastname

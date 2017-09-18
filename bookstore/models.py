from django.db import models

class Author(models.Model):
    """
    This class represents the author of a book.
    """
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

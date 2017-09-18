from django.db import models

class Author(models.Model):
    """
    This class represents the author of a book.
    """
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

class Book(models.Model):
    """
    This class represents the books.
    """
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    isbn = models.CharField("ISBN", max_length=13)
    summary = models.TextField(max_length=1000)
    title = models.CharField(max_length=200)

class Rating(models.Model):
    """
    This class represents the rating of a book.
    """
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    five_stars = models.PositiveIntegerField()
    four_stars = models.PositiveIntegerField()
    three_stars = models.PositiveIntegerField()
    two_stars = models.PositiveIntegerField()
    one_stars = models.PositiveIntegerField()

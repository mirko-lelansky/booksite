from django.db import models

class Author(models.Model):
    """
    This class represents the author of a book.
    """
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField("Died", null=True, blank=True)

    def __str__(self):
        return self.firstname + " " + self.lastname

    class Meta:
        ordering = ['lastname', 'firstname']

class Book(models.Model):
    """
    This class represents the books.
    """
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    isbn = models.CharField("ISBN", max_length=13)
    summary = models.TextField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Rating(models.Model):
    """
    This class represents the rating of a book.
    """
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(choices=((0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)), default=0)

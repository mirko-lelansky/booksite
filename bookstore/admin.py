from django.contrib import admin

from bookstore.models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
     fields = ["firstname", "lastname", ("date_of_birth", "date_of_death")]
     list_display = ("firstname", "lastname", "date_of_birth", "date_of_death")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

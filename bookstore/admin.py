from django.contrib import admin

from bookstore.models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
     fields = ["firstname", "lastname", ("date_of_birth", "date_of_death")]
     list_display = ("firstname", "lastname", "date_of_birth", "date_of_death")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ["isbn", "title", "author", "summary"]
    list_display = ("isbn", "title", "author")
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = Author.objects.order_by('lastname', 'firstname')
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

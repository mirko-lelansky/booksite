# Copyright 2017 Mirko Lelansky <mlelansky@mail.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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

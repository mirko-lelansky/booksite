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
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import Author, Book, Rating

def index(request):
    """
    This is the base index page.
    """
    authors_count = Author.objects.count()
    books_count = Book.objects.count()

    return render(request, "bookstore/index.html", context={
        "authors_count": authors_count,
        "books_count": books_count
    })

class RatingsListView(ListView):
    """
    This class represents the current top ratings.
    """
    template_name = "bookstore/ratings.html"

    def get_queryset(self):
        """
        This method returns the current ten top ratings.
        """
        ratings = Rating.objects.filter(stars__gte=1).annotate(scount=Count('stars'))
        ratings_converted = self._convert_ratings(ratings)
        result = [(key, self._calculate_star(value["values"], value["weights"])) for key, value in ratings_converted.items()]
        result.sort(key=lambda x: x[1])
        return result[:10]

    def _convert_ratings(self, ratings):
        """
        """
        result = {}
        for rating in ratings:
            title = rating.book.title
            value = rating.scount
            weight = rating.stars

            if title not in result:
                result[title] = {}
            if "values" not in result[title]:
                result[title]["values"] = []
            if "weights" not in result[title]:
                result[title]["weights"] = []

            result[title]["values"].append(value)
            result[title]["weights"].append(weight)
        return result

    def _calculate_star(self, values, weights):
        s = sum(values)
        sw = sum([values[i] * weights[i] for i in range(len(values))])
        return round(sw/s, 2)

class RatingFormView(CreateView):
    """
    This class represents the rating of a book.
    """
    fields = ["book", "stars"]
    model = Rating
    success_url = reverse_lazy("bookstore:ratings")

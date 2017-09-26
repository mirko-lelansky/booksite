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
from django.core.management.base import BaseCommand, CommandError
from bookstore.models import Book, Rating
import random
import threading

class Command(BaseCommand):
    help = "Create some test commands."

    def add_arguments(self, parser):
        parser.add_argument("clients", default=5, nargs="?", type=int)
        parser.add_argument("requests_per_client", default=20, nargs="?", type=int)

    def handle(self, *args, **options):
        threads = [ClientThread(options["requests_per_client"]) for i in range(options["clients"])]
        [thread.start() for thread in threads]
        for x in threads:
            x.join()

class ClientThread(threading.Thread):
    """
    """
    def __init__(self, max_requests):
        super().__init__()
        self._requests = 0
        self._max_requests = max_requests

    def run(self):
        while(self._requests < self._max_requests):
            books = Book.objects.all()
            book = random.choice(books)
            rate = random.randint(1, 5)
            rating = Rating()
            rating.book = book
            rating.stars = rate
            rating.save()
            self._requests = self._requests + 1

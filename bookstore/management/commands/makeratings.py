from django.core.management.base import BaseCommand, CommandError
from bookstore.models import Book, Rating
import random
import threading

class Command(BaseCommand):
    help = "Create some test commands."

    def add_arguments(self, parser):
        parser.add_argument("num_clients", default=20, nargs="?", type=int)

    def handle(self, *args, **options):
        threads = [ClientThread() for i in range(options["num_clients"])]
        [thread.start() for thread in threads]
        for x in threads:
            x.join()

class ClientThread(threading.Thread):
    """
    """
    def __init__(self):
        super().__init__()

    def run(self):
        books = Book.objects.all()
        book = random.choice(books)
        rate = random.randint(1, 5)
        rating = Rating()
        rating.book = book
        rating.stars = rate
        rating.save()

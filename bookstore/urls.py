from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

app_name = 'bookstore'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ratings/$', cache_page(60 * 15)(views.RatingsListView.as_view()), name="ratings"),
    url(r'^rating/$', views.RatingFormView.as_view(), name="rating")
]

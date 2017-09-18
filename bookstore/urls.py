from django.conf.urls import url

from . import views

app_name = 'bookstore'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ratings/$', views.RatingsListView.as_view(), name="ratings"),
    url(r'^rating/$', views.RatingFormView.as_view(), name="rating")
]

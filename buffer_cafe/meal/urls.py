from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="index"),
    path("about-us/", views.about_us, name="about_us"),
    path("show-item/", views.show_item, name="show_item")
]

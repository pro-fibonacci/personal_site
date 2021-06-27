from django.conf.urls import url
from .import views
from django.contrib import admin
from .import views as contact
from django.urls import path


app_name = "portFolioApp"


urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact, name="contact")


]

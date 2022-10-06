from django.contrib import admin
from django.urls import path
from welcome import views


urlpatterns = [
  path("", views.index, name='welcome'),
  path("about", views.about, name='about'),
  path("contact", views.contact, name='contact'),
  path("services", views.services, name='services')
]

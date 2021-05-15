# Copyright © 2021 Papillon. All rights reserved.

from django.urls import path

from . import views

app_name = 'collection'
urlpatterns = [
    path('isbn', views.ISBNView.as_view(), name="isbn"),
    path('registration', views.RegistrationView.as_view(), name="registration"),
]
import imp
from django.urls import path
# from the current folder import views
from . import views


urlpatterns  = [
    path('playground/', views.sayHello)
]
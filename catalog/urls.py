from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('hello/', views.hello_world),
    path('hash/<str:input_text>/', views.hash_text, name="hash_text"),
]
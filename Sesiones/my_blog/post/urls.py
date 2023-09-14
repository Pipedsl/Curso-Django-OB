from django.urls import path, include
from . import views

urlpatterns = [
    path('queries/', views.queries, name="queries"),
    path('update/', views.update, name="update")
]
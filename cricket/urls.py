from django.urls import path
from . import views

urlpatterns = [
    path(' ',views.main,name='main'),
    path('cricket/', views.cricket, name='cricket'),
     path('testing/', views.testing, name='testing'), 
    path('cricket/details/<int:id>',views.details,name='details'),
]
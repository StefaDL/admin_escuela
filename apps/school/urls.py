from django.urls import path
from . import views

app_name = 'school'

urlpatterns = [
    path('',views.materia, name='index')
]
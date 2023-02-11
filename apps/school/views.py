from django.shortcuts import render
from django.http import HttpResponse

def materia(request):
    return HttpResponse(f"<h1>hola<h1>")

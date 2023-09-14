from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


def test(request):
    return HttpResponse("Funciona correctamente")

def create(request):
    #Forma 1 de crear objeto en la tabla bd
    #comment = Comment(name="Felipe", score="5", comment="Este es un comentario")
    #comment.save()
    #Forma 2 de crear objeto en la tabla bd
    comment = Comment.objects.create(name="Felipe")
    return HttpResponse("Ruta para probar la creacion de modelos")

def delete(request):
    #Forma 1 de eliminar objetos en la tabla bd
    #comment = Comment.objects.get(id=1)
    #comment.delete()
    #Forma 2 de eliminar objetos en la tabla bd
    Comment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar los borrados")

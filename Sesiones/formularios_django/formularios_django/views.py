from django.shortcuts import render
from django.http import HttpResponse
from .forms import CommentForm, ContactForm

def form(request):
    comment_form = CommentForm({'name': 'felipe', 'url':'https://felipe.com', 'comment':'comentario'})
    return render(request, 'form.html', {'comment_form' : comment_form})

def goal(request):
    if request.method != 'POST':
        HttpResponse("Método no permitido")
    
    return HttpResponse(request.POST['name'])

def widget(request):
    if request.method == 'GET': 
        form = ContactForm()
        return render(request, 'widget.html', {'form':form})
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #todas las acciones a realizar cuando los datos son correctos
            return HttpResponse("Válido")
        else:
            #Avisamos al usuario cuando los datos no son validos
            return render(request, 'widget.html', {'form':form})
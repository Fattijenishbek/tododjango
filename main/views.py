from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list= ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})

def third(request):
    return HttpResponse("This is the third page")

def add_todo(request):
    form=request.POST
    text=form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)
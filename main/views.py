from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo
from .models import Book

# Create your views here.

def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list= ToDo.objects.all()
    return render(request, "test.html", {"todo_list":todo_list})

def read(request):
    book_list=Book.objects.all()
    return render(request, "book.html",{"book_list":book_list})

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

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite=False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo=ToDo.objects.get(id=id)
    todo.is_closed=not todo.is_closed
    todo.save()
    return redirect(test)

def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    book = Book(title=title, subtitle=subtitle, description=description, price=price, genre=genre, author=author, year=year)
    book.save()
    return redirect(read)

def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(read)

def mark_book(request, id):
    book = Book.objects.get(id=id)
    book.is_favorite = not book.is_favorite
    book.save()
    return redirect(read)

def book(request, id):
    book_object = Book.objects.get(id=id)
    return render(request, "books_detail.html", {"book_object": book_object})

def close_book(request, id):
    book = Book.objects.get(id=id)
    book.is_closed = not book.is_closed
    book.save()
    return redirect(read)

def add(request):
    return render(request, "add.html")

def update(request):
    return render(request, "update.html")

def deleted(request):
    return render(request, "deleted.html")
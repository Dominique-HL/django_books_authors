from django.shortcuts import render,redirect
from. models import Book, Author

#Books functions
def books(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request,"books.html",context)

def add_book(request):
    if request.POST['title'] and request.POST['desc']:
        Book.objects.create(title=request.POST['title'],desc=request['desc'])
        return redirect("/")

def book_info(request,book_id):
    context ={
        'books': Book.objects.get(id=book_id),
        'authors':Book.objects.get(id=book_id).authors.all(),
        'all_authors': Author.objects.all()
    }
    return render(request,"book_info.html",context)

def add_authors(request,book_id):
    print(request.POST['author_to_add'])
    print(book_id)
    if request.POST['author_to_add']:
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=request.POST['author_to_add'])
        book.authors.add(author)
    return redirect("/")

def authors(request):
    context ={
        "all_authors": Author.objects.all()
    }
    return render(request,"authors.html",context)

def add_author_to_authors(request):
    if request.POST['first_name'] and request.POST['last_name'] and request.POST['notes']:
        Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect("/authors")

def author_info(request,author_id):
    context ={
        'author': Author.objects.get(id=author_id),
        'books':Author.objects.get(id=author_id).books.all(),
        'all_books': Book.objects.all()
    }
    return render(request,"author_info.html",context)

def add_books(request,author_id):
    if request.POST['book_to_add']:
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=request.POST['book_to_add'])
        author.books.add(book)
    return redirect("/")


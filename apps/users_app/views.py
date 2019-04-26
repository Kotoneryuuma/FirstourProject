from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author
# from .models import users

# ＃＃＃＃＃＃＃＃＃＃＃＃
# index  show books
# ＃＃＃＃＃＃＃＃＃＃＃＃
def index(request):
    return render(request, "users_app/index.html")

def books(request,idr):
    context = {
        "book":Book.objects.get(id=idr),
        "author_name":Book.objects.get(id=idr).authors.all().values(),
        "all_author_name":Author.objects.all().values(),
    }
    print(context["author_name"])
    return render(request, "users_app/books.html",context)

def process(request):
    if request.method == "POST":
        data = {
            "a_id": request.POST["author_id"],
            "b_id": request.POST["book_id"],
        }
        this_book = Book.objects.get(id=data["a_id"])
        this_author = Author.objects.get(id=data["b_id"])
        this_author.books.add(this_book)
        return redirect("/")

def authors(request):
    context = {
    	"authors": Author.objects.all()
    }
    return render(request, "users_app/authors.html", context)


def show_author(request,idr):
    context = {
        "author":Author.objects.get(id=idr),
        "author_books":Author.objects.get(id=idr).books.all().values(),
        "all_book_titles":Book.objects.all().values(),
    }
    print(context["author_books"])
    return render(request, "users_app/authors_show.html",context)

def process_author(request):
    if request.method == "POST":
        data = {
            "b_id": request.POST["book_id"],
            "a_id": request.POST["author_id"],
        }
        # this_book = Book.objects.get(id=data["b_id"])
        # this_author = Author.objects.get(id=data["a_id"])
        # this_book.authors.add(this_author)
        print(data)
        
        return redirect("/")








# def index_author(request):
#     context = {
#     	"books": Book.objects.all()
#     }
#     return render(request, "users_app/index.html", context)

##i need to insert the data from DB to Templates

# def info(request):
#     if request.method == "POST":
#         val_from_field_one = request.POST["one"]
#     	val_from_field_two = request.POST["two"]
    
#     return render(request, "users_app/index.html", context)

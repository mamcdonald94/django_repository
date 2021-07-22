import bcrypt
from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages


def index(request):
    return render(request, "login_reg.html")

def create_user(request):
    if request.method == "POST":
        # validation check before database save
        errors = User.objects.registration_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # creates a variable that holds the hashed pw, which then will be used to create a User
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hash_pw
        )
        # holds the id of the currently logged in user
        request.session['logged_user_id'] = new_user.id
        return redirect('/user/dashboard')

    return redirect('/')

def create_book(request):
    if request.method == 'POST':
        book_errors = Book.objects.book_validator(request.POST)

        if book_errors:
            for key, error in book_errors.items():
                print(error)
                messages.error(request, error)
            return redirect('/user/dashboard')

        user = User.objects.get(id=request.session['logged_user_id'])

        book = Book.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            created_by = user,
        )

        book.favorited_by.add(user)
        return redirect('/user/dashboard')
    return redirect('/')

def edit_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    book_errors = Book.objects.book_validator(request.POST)

    if book_errors:
        for error in book_errors:
            messages.error(request, error)
        return redirect(f'/book/{this_book.id}')
    this_book.title = request.POST['title']
    this_book.description = request.POST['description']
    this_book.save()
    return redirect(f'/book/{this_book.id}')

def delete_book(request, book_id):
    this_book = Book.objects.get(id=book_id)
    this_book.delete()
    return redirect('/user/dashboard')

def remove_favorite(request, book_id):
    this_book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['logged_user_id'])

    user.books_favorited.remove(this_book)
    return redirect(f'/book/{this_book.id}')

def add_favorite(request, book_id):
    this_book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['logged_user_id'])

    user.books_favorited.add(this_book)
    return redirect(f'/book/{this_book.id}')

def dashboard(request):
    if 'logged_user_id' not in request.session:
        messages.error(request, "You must be logged in or registered to access this page!")
        return redirect('/')
    context = {
        'all_books': Book.objects.all(),
        'logged_user': User.objects.get(id=request.session['logged_user_id'],),
    }
    return render(request, 'dashboard.html', context)

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        
        if user:
            logged_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user_id'] = logged_user.id
                return redirect('/user/dashboard')
        messages.error(request, "invalid email or password")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def book_info(request, book_id):
    if 'logged_user_id' not in request.session:
        messages.error(request, "You must be logged in or registered to access this page!")
        return redirect('/')
    context = {
        "logged_user": User.objects.get(id=request.session['logged_user_id']),
        "this_book": Book.objects.get(id=book_id)
    }
    return render(request, 'book_info.html', context)
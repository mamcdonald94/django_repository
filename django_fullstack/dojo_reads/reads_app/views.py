import bcrypt
from django.shortcuts import render, redirect
from .models import User, Author, Book, Review
from django.contrib import messages
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    if request.method == "POST":
        # validation check before database save
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # creates a variable that holds the hashed pw, which then will be used to create a User
        hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            name = request.POST['name'],
            alias = request.POST['alias'],
            email = request.POST['email'],
            password = hash_pw
        )
        request.session['logged_user'] = new_user.id # request.session['logged_user'] is the ID of the currently logged in user
        return redirect('/user/dashboard')

    return redirect('/')

def dashboard(request):
    if 'logged_user' not in request.session:
        messages.error(request, "You must be logged in or registered to access this!")
        return redirect('/')
    context = {
        'logged_user': User.objects.get(id=request.session['logged_user']),
        'all_books': Book.objects.all(),
        'recent_reviews': Review.objects.order_by('created_at').reverse()[:3]
    }
    return render(request, 'dashboard.html', context)

def user_page(request, user_id):
    if 'logged_user' not in request.session:
        messages.error(request, "You must be logged in or registered to access this!")
        return redirect('/')
    user = User.objects.get(id=user_id)
    context = {
        'this_user': user,
    }
    return render(request, 'user_page.html', context)

def create_book(request):
    if request.method == 'POST':
        book_errors = Book.objects.book_validator(request.POST)
        review_errors = Review.objects.review_validator(request.POST)
        errors = list(book_errors.values()) + list(review_errors.values())
        
        if request.POST['author_dropdown'] == "-1":
            if request.POST['author_name'] == "":
                messages.error(request, "Please either choose an author from the dropdown menu, or create a new one.")
            else:
                author_errors = Author.objects.author_validator(request.POST)
                errors += list(author_errors.values())
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('/book/book_form')
        
        if request.POST['author_dropdown'] == '-1':
            author = Author.objects.create(name=request.POST['author_name'])
        else:
            author = Author.objects.get(id=request.POST['author_dropdown'])
        
        book = Book.objects.create(title=request.POST['title'])
        user = User.objects.get(id=request.session['logged_user'])
        review = Review.objects.create(content=request.POST['content'], rating=int(request.POST['rating']), user_review=user, book_reviewed=book)
        book.authors.add(author)
        book.book_reviews.add(review)
        return redirect(f'/book/{book.id}')

    return redirect('/book/book_form')

def show_book(request, book_id):
    context = {
        'this_book': Book.objects.get(id=book_id)
    }
    return render(request, 'book_info.html', context)

def add_review(request):
    if request.method == "POST":

        errors = Review.objects.review_validator(request.POST)
        book = Book.objects.get(id=request.POST['book_reviewed'])

        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/book/{book.id}')
        user = User.objects.get(id=request.session['logged_user'])
        review = Review.objects.create(content=request.POST['content'], rating=int(request.POST['rating']), user_review=user, book_reviewed=book)

        return redirect(f'/book/{book.id}')

def delete_review(request, review_id):
    if 'logged_user' not in request.session:
        messages.error(request, "You must be logged in or registered to access this!")
        return redirect('/')
    this_review = Review.objects.get(id=review_id)
    this_review.delete()
    return redirect(f'/book/{this_review.book_reviewed.id}')

def book_form(request):
    # prevents someone that is not logged in from accessing form via GET request
    if 'logged_user' not in request.session:
        messages.error(request, "You must be logged in or registered to access this!")
        return redirect('/')
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'add_book.html', context)

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        
        if user:
            logged_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['logged_user'] = logged_user.id
                return redirect('/user/dashboard')
        messages.error(request, "invalid email or password")
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')
from django.shortcuts import render, redirect
from .models import User, Taco


# Create your views here.
def index(request):
    context = {
        'users': User.objects.all(),
        'tacos': Taco.objects.all(),
    }
    return render(request, 'index.html', context)

def create_user(request):
    user1 = User.objects.create(
        name = request.POST['name'],
        weight = request.POST['weight'],
        age = request.POST['age'],
        always_hungry = request.POST['hungry']
    )
    return redirect('/')

def create_taco(request):
    taco1 = Taco.objects.create(
        name = request.POST['name'],
        toppings = request.POST['toppings'],
        meat = request.POST['meat'],
        spicy = request.POST['spicy'],
        user = User.objects.get(id=request.POST['user'])
    )
    return redirect('/')
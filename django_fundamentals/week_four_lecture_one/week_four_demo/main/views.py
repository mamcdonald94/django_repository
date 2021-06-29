from django.shortcuts import render
from .models import Truck

# Create your views here.
def index(request):
    context = {
        'truck': Truck.objects.get(id=1),
        'all_trucks': Truck.objects.all(),
    }
    return render(request, 'index.html', context)
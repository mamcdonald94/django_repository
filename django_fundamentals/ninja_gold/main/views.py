from django.shortcuts import render, redirect, HttpResponse
import random
from time import strftime, localtime

def index(request):
    if 'gold_total' not in request.session:
        request.session['gold_total'] = 0
        request.session['history'] = []
    return render(request, 'index.html')

def money(request):
    if request.method == 'POST':
        if 'farm' in request.POST:
            amount = random.randint(10, 20)
            request.session['gold_total'] += amount
            request.session['history'].append(f'gained {amount} gold ' + strftime('%Y/%m/%d %H:%M %p', localtime()))
            print(request.session['gold_total'])
        elif 'cave' in request.POST:
            amount = random.randint(5, 10)
            request.session['gold_total'] += amount
            request.session['history'].append(f'gained {amount} gold ' + strftime('%Y/%m/%d %H:%M %p', localtime()))
            print(request.session['gold_total'])
        elif 'house' in request.POST:
            amount = random.randint(2, 5)
            request.session['gold_total'] += amount
            request.session['history'].append(f'gained {amount} gold ' + strftime('%Y/%m/%d %H:%M %p', localtime()))
            print(request.session['gold_total'])
        else:
            amount = random.randint(10, 50)
            if random.randint(0, 1) == 0:
                request.session['gold_total'] += amount
                request.session['history'].append(f'gained {amount} gold ' + strftime('%Y/%m/%d %H:%M %p', localtime()))
            else:
                request.session['gold_total'] -= amount
                request.session['history'].append(f'lost {amount} gold ' + strftime('%Y/%m/%d %H:%M %p', localtime()))
            print(request.session['gold_total'])
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')
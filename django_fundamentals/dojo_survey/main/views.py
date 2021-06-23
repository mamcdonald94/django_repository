from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')

def submit(request):
    if request.method == 'POST':
        info = {
            'name': request.POST['name'],
            'dojo': request.POST['dojo'],
            'lang': request.POST['lang'],
            'comment': request.POST['comment'],
        }
        return render(request, 'result.html', info)

def back(request):
    return render(request, 'index.html')

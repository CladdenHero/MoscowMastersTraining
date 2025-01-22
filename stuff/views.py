from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def place(request):
    return render(request, 'place.html')

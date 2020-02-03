from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "intro/index.html")

def intro(request):
    return render(request, "intro/introduction.html")

def overview(request):
    return render(request, "intro/overview.html")

def history(request):
    return render(request, "intro/history.html")

def numbers(request):
    return render(request, "intro/numbers.html")

def location(request):
    return render(request, "intro/location.html")

def status(request):
    return render(request, "intro/status.html")
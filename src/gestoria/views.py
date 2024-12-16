from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "gestoria/index.html")

def about(request):
    return render(request, "gestoria/about.html")
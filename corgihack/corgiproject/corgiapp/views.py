from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'corgiapp/home.html')

def secondpage(request):
    return render(request, 'corgiapp/secondpage.html')

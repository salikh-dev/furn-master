from django.shortcuts import render, reverse
from furn.models import *
from django.views import generic
from .form import *

def home(request):
    
    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)

    base = Carousel.objects.all()
    blog = Blog.objects.all()
    products = Product.objects.all()
    categires = Category.objects.all()
    context = {
        "base": base, 
        "arrivals":arrivals, 
        "blog":blog,
        "products":products, 
        "categoryes":categires
    }
    return render(request, 'pages/home.html', context)  


def arrivals_detail(request, pk):
    arrivals_detalis = Arrival.objects.get(id=pk)

    context ={
        "arrivals_detalis":arrivals_detalis
    }

    return render(request, "detalis/arrivals_detalis.html", context)

# ro`yhatdan o`tish qismi

def signup(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return reverse("furn:home")
    else:
        form = Registration()        
    
    return render(request, 'registration/signup.html', {"form":form})

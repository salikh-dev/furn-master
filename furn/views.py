from django.shortcuts import render, redirect
from furn.models import *
from furn.form import Followers

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
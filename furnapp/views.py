from multiprocessing import context
from django.shortcuts import render, reverse, redirect
from .models import *
from django.views import generic
from .form import *

from django.urls import reverse_lazy

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
    
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    return render(request, 'registration/signup.html', {"form":form})

# class Profileview(generic.TemplateView):
#     template_name = "pages/profile/profile.html"

def profile(request):
    if request.method == 'POST':
        user_form == EditProfileForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to="profile")
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context ={
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, 'pages/profile/profile.html', context)

def updateProfileView(request, pk):
    if request.method == 'POST':
        user_form == EditProfileForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILE, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile.save()
            return redirect(to="profile")
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context ={
        "user_form":user_form,
        "profile_form":profile_form
    }
    return render(request, 'pages/profile/edit_profile.html', context)

# class EditProfileView(generic.UpdateView):
#     form_class = EditProfileForm
#     template_name = "pages/profile/edit_profile.html"
#     success_url = reverse_lazy('furn:profile')
#     def get_object(self):
#         return self.request.user
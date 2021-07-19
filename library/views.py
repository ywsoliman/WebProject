from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import *

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created successfully!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(request, f'Your account information has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'pages/profile.html', context)

def search(request):
    return render(request, 'pages/booksearch.html')

def ONsearch(request):
    context2={
       'books' : Book.objects.all(),
    }
    return render(request, 'pages/ONsearch.html',context2)

def browseall(request):
    search = Book.objects.all()
    title = None
    category = None
    author = None
    if 'BookName' in request.GET:
        title = request.GET['BookName']
        if title:
            search = search.filter(title__icontains=title)

    elif 'BookCategory' in request.GET:
        category = request.GET['BookCategory']
        if category:
            search = search.filter(category__icontains=category)

    elif 'BookAuthor' in request.GET:
        author = request.GET['BookAuthor']
        if author:
            search = search.filter(author__icontains=author)

    context = {
        'books': search
    }
    return render(request, 'pages/browseall.html',context)
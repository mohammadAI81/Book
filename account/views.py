from django.shortcuts import render, redirect
from django.contrib import auth
from django.conf import settings
from .models import CustomAdmin

from blog.models import Blog, Comment

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         if password and username:
#             user = auth.authenticate(request, password=password, username=username)
#             if user is not None :
#                 auth.login(request, user)
#                 if request.GET:
#                     return redirect(request.GET['next'])
#                 else:
#                     return redirect('home')
#             else:
#                 return redirect('login')    
#         else:
#             return redirect('login')
#     return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if username and email and password and password2:
            if CustomAdmin.objects.filter(username=username).exists():
                return redirect('signup')
            else:
                if password == password2:
                    user = CustomAdmin.objects.create_user(username=username, email=email, password=password)
                    return redirect('login')
                else:
                    return redirect('signup')
        else:
            return redirect('signup')
    return render(request, 'registration/signup.html')


def dashboard(request):
    user = request.user
    comments_blog = user.auhtor_comments.all()

    context = {
        'comments_blogs': comments_blog,
    }
    return render(request, 'registration/dashboard.html', context)


def logout(request):
    auth.logout(request)    
    return redirect('home')

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import CreateBlogForm
from .models import Blog
import readtime
import datetime
import markdown2


CATEGORY_CHOICES = [
    ("None", "None"),
    ("Tech", "Tech"),
    ("Health", "Health"),
    ("Sports", "Sports"),
    ("Business", "Business"),
    ("Finance", "Finance"),  
]


# Index page
def index(request):
    if len(Blog.objects.all()) != 0:
        latest = Blog.objects.last()
        blogs = Blog.objects.exclude(id=latest.id)
        return render(request, "blog/index.html", {
            "blogs": blogs.order_by('-date_time'),
            "latest": latest
        })
    return render(request, "blog/index.html")


# User creation
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = User.objects.create_user( username=username, password=password)
            user = authenticate(username=username, password=password)


            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "blog/register.html", {
                    "message": "Failed to create user account!",
                    "form": UserCreationForm()
                })

    else:
        form = UserCreationForm()
        
    return render(request, "blog/register.html", {
            "form": form
        })


# User login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "blog/login.html")


# User logout
def logout_view(request):
    logout(request)
    return redirect("index")


# Create Blog function
def create_blog(request):
    if request.method == "POST":
        form = CreateBlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog = Blog()
            new_blog.author = request.user
            new_blog.title = form.cleaned_data.get("title")
            new_blog.content = form.cleaned_data.get("content")
            read_time = readtime.of_text(new_blog.content)
            new_blog.readtime = read_time
            date_time = datetime.datetime.now()
            new_blog.date_time = date_time.strftime("%c")
            new_blog.image = form.cleaned_data.get("image")
            new_blog.image_caption = form.cleaned_data.get("image_caption")
            new_blog.category = form.cleaned_data.get("category")
            new_blog.save()
            return redirect("index")

    else:
        form = CreateBlogForm()

    return render(request, "blog/create_blog.html", {
        "form": form
    })


# View blog
@login_required(login_url="login")
def view_blog(request, blog_id):
    is_author = False
    blog = Blog.objects.get(id=blog_id)
    content = markdown2.markdown(blog.content)
    read_time = readtime.of_text(content)
    if request.user == blog.author:
        is_author = True
        
    return render(request, "blog/view_blog.html", {
        "blog": blog,
        "is_author": is_author,
        "content": content,
        "readtime": read_time
    })


# Delete blog
def delete_blog(request, blog_id):
    Blog.objects.filter(id=blog_id).delete()
    return redirect("index")


# Show category
def show_category(request, category):
    return render(request, "blog/show_category.html", {
        "blogs": Blog.objects.filter(category = category),
        "category": category
    })


# Display user
def display_user(request, user_id):
    user = User.objects.get(id=user_id)
    blogs = Blog.objects.filter(author=user)
    return render(request, "blog/user.html", {
        "user": user,
        "blogs": blogs
    })


# Searches based on article name
def search(request):
    print(request)
    if request.method == "POST":
        query = request.POST["query"]
        search_result = Blog.objects.filter(title__contains=query)
        return render(request, "blog/search.html", {
            "search_result": search_result,
            "query": query
        })
    
    return render(request, "blog/search.html", {
        "search_result": "No results found!"
    })
from django.shortcuts import render, HttpResponse , redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login(request):
    return HttpResponse("placeholder for users to log in.")

def new(request):
    return HttpResponse("placeholder for users to create a new user record.")

def users_(request):
    return HttpResponse("placeholder display all the list of users later.")

def blogs(reuqest):
    return redirect('/blogs')
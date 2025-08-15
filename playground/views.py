from django.shortcuts import render
from django.http import  HttpResponse

def calculate():
    x = 1
    y = 2
    return x

# Create your views here.
# Request handler 
def say_hello( request ):
    calculate()
    return render( request, "hello.html", { 'name': 'jerks' })

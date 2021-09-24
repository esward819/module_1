from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.
def hello_view(request) -> HttpResponse:
    return HttpResponse("Hello World")



def near_hundred(request, n):
    return HttpResponse(n >= 90 and n <= 110) or (n >= 190 and n <= 210)


def string_splosion(request, str):
    result = ""
    for i in range(len(str)):
        result = result + str[:i+1]
    return HttpResponse(result)


def cat_dog(request, str):
    return HttpResponse(str.count('cat') == str.count('dog'))

    
def lone_sum(request, a, b, c):
    sum = 0
    sum += a if a not in [b,c] else 0
    sum += b if b not in [a,c] else 0
    sum += c if c not in [a,b] else 0
    return HttpResponse(sum)

def hey_you(request, name) -> HttpResponse:
    return HttpResponse(f"Hello, {name}!")

def how_old(request, end, birthyear) -> HttpResponse:
    return HttpResponse(end - birthyear)

def Can_I_Take_Your_Order(request, burgers, fries, drinks) -> HttpResponse:
    return HttpResponse(float(4.5 * burgers) + float(1.5 * fries) + float(1 * drinks))
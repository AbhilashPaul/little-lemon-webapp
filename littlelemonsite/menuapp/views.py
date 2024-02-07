from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def menu(request): 
    return HttpResponse("This is the menu page.")


def menu_salads(request): 
    return HttpResponse("This is the salads menu page.")
 
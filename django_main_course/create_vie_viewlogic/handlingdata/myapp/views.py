from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from datetime import datetime

def say_hello(Request):
    return HttpResponse("Hello World")

def homePage(Request):
    return HttpResponse("Welcome to little lemon home page")


def display_date(Request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)

def menu(Request):
    text = """ <h1 style="color:blue;">This is little lemon again!!!</h1> """
    return HttpResponse(text)

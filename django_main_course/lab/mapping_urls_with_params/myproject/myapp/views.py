from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def drinks(request, drink_name):

    drink = {
        'tea':'type of coffee',
        'mocha':'type of beverage',
        'lemonade':'type of refreshment'
    }

    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h1>{drink_name} </h1>"+ choice_of_drink)


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def menuitems(request, dish):
    items = {
        'achu':'A dish consisting of pounded cocoyams and a red palm oil soup, served with cow skin, oxtail, tripe, and steamed eggplant',
        'afang':'A vegetable soup which has its origin from the Efik people in the southeast of Nigeria',
        'akara':'A Yoruba food made from peeled beans made into balls and deep-fried, known as Koose in Hausa and Ghana, can be eaten as a snack, but is often coupled with hausa koko as part of a breakfast meal.'
    }

    description = items[dish]

    return HttpResponse(f"<h1> {dish} </h1>"+ description)

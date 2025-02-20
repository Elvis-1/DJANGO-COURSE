Relevant code for settings.py
STATIC_URL = 'static/'

STATICFILES_DIRS = ["myproject/static",]

templates/menu.html

{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> Menu</p>
<p> This is a Menu page for Little Lemon </p>
{% endblock %}

templates/index.html

{% extends 'base.html'%}
{% load static %}
{% block content%}
<p> Home</p>
<p> This is the Home page for Little Lemon </p>
{% endblock %}

templates/book.html

{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> Book</p>
<p> This is a Booking page for Little Lemon </p>
{% endblock %}

templates/about.html

{% extends 'base.html' %}
{% load static %}
{% block content %}
<p> About Us</p>
<p> This is an About page for Little Lemon </p>

{% endblock %}

Relevant code for templates/base.html

    <!-- Add include tag -->
    {% include 'partials/_header.html' %}


    <main>
        <!-- Begin block content --> 

        {% block content%}
        {% endblock %}
        
        <!-- End block content -->
    </main>


    templates/partials/_header.html


{% load static %}
<footer style="background-color: #EE9972; "></footer>
<header>
  <img src="{% static 'img/logo.png' %}" />
</header>
  <nav>
    <ul>
      <li><a href="{% url 'home' %}">Home</a></li>
      <li><a href="{% url 'about' %}">About</a></li>
      <li><a href="{% url 'menu' %}">Menu</a></li>
      <li><a href="{% url 'book' %}">Book</a></li> 
    </ul>
  </nav>

  views.py
  
  from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')
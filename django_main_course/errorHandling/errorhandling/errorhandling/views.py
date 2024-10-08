from django.http import HttpResponse, HttpResponseNotFound


def handler404(request, exception):
    return HttpResponse("404: Page not found")

def home(request):
    return HttpResponseNotFound("The little lemon!") # HttpResponse("The little lemon!")



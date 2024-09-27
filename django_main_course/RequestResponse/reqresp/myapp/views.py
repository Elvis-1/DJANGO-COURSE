from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    path = request.path
    response = HttpResponse('This works!!!')
    return    response #HttpResponse(path,content_type ='text/html', charset = 'utf-8')

def home2(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    userAgent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20
    msg = f"""
<br>
<br>path:{path}
<br>method:{method}
<br>scheme:{scheme}
<br>address:{address}
<br>path info:{path_info}
<br>user agent: {userAgent}
<br>response headers: {response.headers}
"""

 

    return HttpResponse(msg,content_type ='text/html', charset = 'utf-8')
   # response #HttpResponse(path,content_type ='text/html', charset = 'utf-8')

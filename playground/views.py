from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# take request and return response
# request -> response


# pull data from db
# transform
# send email
def sayHello(request):
    return render(request, 'hello.html', {'name': 'Senura'})

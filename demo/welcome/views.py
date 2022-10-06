# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  # return HttpResponse("this is the testng index page")
  context = {
    "first_name": "Achyut",
    "last_name": "Kadam"
  }
  return render(request, 'index.html', context)

def about(request):
  return render(request, 'about.html')

def contact(request):
  return render(request, 'contact.html')

def services(request):
  return render(request, 'services.html')

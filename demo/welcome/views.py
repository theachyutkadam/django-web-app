# from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from welcome.models import Contact

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
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    desc = request.POST.get('desc')

    contact = Contact(name=name, email=email, contact=contact, desc=desc, date=datetime.today())
    contact.save()

  return render(request, 'contact.html')

def services(request):
  return render(request, 'services.html')

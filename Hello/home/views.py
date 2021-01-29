from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable":"This is sent"
    }
    return render (request, 'index.html', context)
def django(request):
    return render (request, 'django.html')
def flask(request):
    return render (request, 'flask.html')
def JS(request):
    return render (request, 'JS.html')
def reactJS(request):
    return render (request, 'reactJS.html')
def AngJS(request):
    return render (request, 'AngJS.html')
def NextJS(request):
    return render (request, 'NextJS.html')
def Forms(request):
    if request.method== "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name=name,email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Congrats you have been registered')
    return render (request, 'form.html')
from django.shortcuts import render, HttpResponse
from datetime import datetime
from new_project.models import Contact
from django.contrib import messages

def index (request):
    context = {
        "variable" : "this is sent"
    }
    
    return render(request , 'index.html',context)
    

def about (request):
    return render(request , 'About.html')

def project (request):
    return render(request , 'Project.html')

def contact (request):
    if request.method == "POST":
        firstName = request.POST.get("firstName")
        lastName = request.POST.get("lastName")       
        email = request.POST.get("email")
        country = request.POST.get("country")
        desc = request.POST.get("desc")
        contact = Contact(firstName=firstName, lastName=lastName, email=email, country=country, desc= desc, date=datetime.today())


        contact.save()
        messages.success(request, 'Action completed successfully!')

    return render(request , 'contact.html')

def test (request):
    return render(request , 'test.html')

# Create your views here.

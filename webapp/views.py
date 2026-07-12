from django.shortcuts import render,redirect,get_object_or_404
from webapp.models import *

# Create your views here.


def home(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')

def academics(request):
    return render(request, 'academics.html')

def admission(request):
    return render(request, 'admission.html')



def contact_view(request):
    if request.method == 'POST':
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            message = request.POST['message'],
            category='General',  # or get it from a form field

        )
        mycontact.save()
        return render(request, 'contact.html')
    
    else:
        return render(request, 'contact.html')
    
    
def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html', {'all': all})
    
    
def delete(request,id):
    mycontact = Contact.objects.get(id = id)
    mycontact.delete()
    return redirect('/show')

def edit(request, id):
    editappointment = get_object_or_404(Contact, id=id)

    if request.method == "POST":
        editappointment.name = request.POST["name"]
        editappointment.email = request.POST["email"]
        editappointment.message = request.POST["message"]
        editappointment.save()
        return redirect("show")  # or redirect('/show/')

    return render(request, "contact.html", {
        "editappointment": editappointment
    })

def studentlife(request):
    return render(request, 'studentlife.html')


def facilities(request):
    return render(request, 'facilities.html')


